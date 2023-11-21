# Copyright (C) 2015-2023, KhulnaSoft Ltd.
# Created by Cyware, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import platform
import psutil
import subprocess
import sys
import time
from typing import Union

from cyware_testing.constants.daemons import CLUSTER_DAEMON, API_DAEMON, CYWARE_AGENT, CYWARE_MANAGER, CYWARE_AGENT_WIN
from cyware_testing.constants.paths.binaries import BIN_PATH, CYWARE_CONTROL_PATH
from cyware_testing.constants.paths.sockets import CYWARE_SOCKETS, CYWARE_OPTIONAL_SOCKETS
from cyware_testing.constants.paths.variables import VAR_RUN_PATH, VERSION_FILE
from cyware_testing.constants.platforms import MACOS, SOLARIS, WINDOWS

from . import sockets


def get_service() -> str:
    """
    Retrieves the name of the Cyware service running on the current platform.

    Returns:
        str: The name of the Cyware service. It can be either 'cyware-manager'
             or 'cyware-agent'.

    Raises:
        subprocess.CalledProcessError: If an error occurs while executing the
                                       subprocess to obtain the service name.

    """
    if platform.system() in ['Windows', WINDOWS]:
        return CYWARE_AGENT

    else:  # Linux, sunos5, darwin, aix...
        service = subprocess.check_output([
            CYWARE_CONTROL_PATH, "info", "-t"
        ], stderr=subprocess.PIPE).decode('utf-8').strip()

    return CYWARE_MANAGER if service == 'server' else CYWARE_AGENT


def get_version() -> str:
    """
    Retrieves the version of the Cyware software installed on the current platform.

    Returns:
        str: The version of the Cyware software.

    Raises:
        FileNotFoundError: If the VERSION file cannot be found on Windows.
        subprocess.CalledProcessError: If an error occurs while executing the
                                       subprocess to obtain the version.
    """

    if platform.system() in ['Windows', WINDOWS]:
        with open(VERSION_FILE, 'r') as f:
            version = f.read()
            return version[:version.rfind('\n')]

    else:  # Linux, sunos5, darwin, aix...
        return subprocess.check_output([
            CYWARE_CONTROL_PATH, "info", "-v"
        ], stderr=subprocess.PIPE).decode('utf-8').rstrip()


def control_service(action, daemon=None, debug_mode=False):
    """Perform the stop, start and restart operation with Cyware.

    It takes care of the current OS to interact with the service and the type of installation (agent or manager).

    Args:
        action ({'stop', 'start', 'restart'}): Action to be done with the service/daemon.
        daemon (str, optional): Name of the daemon to be controlled. None for the whole Cyware service. Default `None`.
        debug_mode (bool, optional) : Run the specified daemon in debug mode. Default `False`.
    Raises:
        ValueError: If `action` is not contained in {'start', 'stop', 'restart'}.
        ValueError: If the result is not equal to 0.
    """
    valid_actions = ('start', 'stop', 'restart')
    if action not in valid_actions:
        raise ValueError(f'action {action} is not one of {valid_actions}')

    if sys.platform == WINDOWS:
        if action == 'restart':
            control_service('stop')
            control_service('start')
            result = 0
        else:
            error_109_windows_retry = 3
            for _ in range(error_109_windows_retry):
                command = subprocess.run(
                    ["net", action, "CywareSvc"], stderr=subprocess.PIPE)
                result = command.returncode
                if result != 0:
                    if action == 'stop' and 'The Cyware service is not started.' in command.stderr.decode():
                        result = 0
                        break
                    if action == 'start' and 'The requested service has already been started.' \
                       in command.stderr.decode():
                        result = 0
                        break
                    elif "System error 109 has occurred" not in command.stderr.decode():
                        break
    else:  # Default Unix
        if daemon is None:
            if sys.platform == MACOS or sys.platform == SOLARIS:
                result = subprocess.run(
                    [CYWARE_CONTROL_PATH, action]).returncode
            else:
                result = subprocess.run(
                    ['service', get_service(), action]).returncode
            action == 'stop' and sockets.delete_sockets()
        else:
            if action == 'restart':
                control_service('stop', daemon=daemon)
                control_service('start', daemon=daemon)
            elif action == 'stop':
                processes = []

                for proc in psutil.process_iter():
                    try:
                        if daemon in [CLUSTER_DAEMON, API_DAEMON]:
                            for file in os.listdir(VAR_RUN_PATH):
                                if daemon in file:
                                    pid = file.split("-")
                                    pid = pid[2][0:-4]
                                    if pid == str(proc.pid):
                                        processes.append(proc)
                        elif daemon in proc.name() or daemon in ' '.join(proc.cmdline()):
                            processes.append(proc)
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
                try:
                    for proc in processes:
                        proc.terminate()

                    _, alive = psutil.wait_procs(processes, timeout=5)

                    for proc in alive:
                        proc.kill()
                except psutil.NoSuchProcess:
                    pass

                sockets.delete_sockets(CYWARE_SOCKETS[daemon])
            else:
                daemon_path = BIN_PATH
                start_process = [
                    f'{daemon_path}/{daemon}'] if not debug_mode else [f'{daemon_path}/{daemon}', '-dd']
                subprocess.check_call(start_process)
            result = 0

    if result != 0:
        raise ValueError(
            f"Error when executing {action} in daemon {daemon}. Exit status: {result}")


def check_daemon_status(target_daemon=None, running_condition=True, timeout=10, extra_sockets=[]):
    """Wait until Cyware daemon's status matches the expected one. If timeout is reached and the status didn't match,
       it raises a TimeoutError.

    Args:
        target_daemon (str, optional):  Cyware daemon to check. Default `None`. None means all.
        running_condition (bool, optional): True if the daemon is expected to be running False
            if it is expected to be stopped. Default `True`.
        timeout (int, optional): Timeout value for the check. Default `10` seconds.
        extra_sockets (list, optional): Additional sockets to check. They may not be present in default configuration.

    Raises:
        TimeoutError: If the daemon status is wrong after timeout seconds.
    """
    condition_met = False
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < timeout and not condition_met:
        if sys.platform == WINDOWS:
            condition_met = check_if_process_is_running(CYWARE_AGENT_WIN) == running_condition
        else:
            control_status_output = subprocess.run([CYWARE_CONTROL_PATH, 'status'],
                                                   stdout=subprocess.PIPE).stdout.decode()
            condition_met = True
            for lines in control_status_output.splitlines():
                daemon_status_tokens = lines.split()
                current_daemon = daemon_status_tokens[0]
                daemon_status = ' '.join(daemon_status_tokens[1:])
                daemon_running = daemon_status == 'is running...'
                if current_daemon == target_daemon or target_daemon is None:
                    if current_daemon in CYWARE_SOCKETS.keys():
                        socket_set = {path for path in CYWARE_SOCKETS[current_daemon]}
                    else:
                        socket_set = set()
                    # We remove optional sockets and add extra sockets to the set to check
                    socket_set.difference_update(CYWARE_OPTIONAL_SOCKETS)
                    socket_set.update(extra_sockets)
                    # Check specified socket/s status
                    for socket in socket_set:
                        if os.path.exists(socket) != running_condition:
                            condition_met = False
                    if daemon_running != running_condition:
                        condition_met = False
        if not condition_met:
            time.sleep(1)
        elapsed_time = time.time() - start_time

    if not condition_met:
        raise TimeoutError(f"{target_daemon} does not meet condition: running = {running_condition}")
    return condition_met


def check_if_process_is_running(process_name):
    """Check if process is running.

    Args:
        process_name (str): Name of process.

    Returns
        boolean: True if process is running, False otherwise.
    """
    is_running = False
    try:
        is_running = process_name in (p.name() for p in psutil.process_iter())
    except psutil.NoSuchProcess:
        pass

    return is_running


def search_process_by_command(search_cmd: str) -> Union[psutil.Process, None]:
    """Search a process by its command

    Args:
        search_cmd (str): Name of the command to be fetched.

    Returns:
        proc (psutil.Process | None): First occurrence of the process object matching the `search_cmd` or
            None if no process has been found.
    """
    if not isinstance(search_cmd, str):
        TypeError(f"`search_cmd` must be a str, but a {type(search_cmd)} was passed.")
    if search_cmd == '':
        TypeError('`search_cmd` must not be an empty string.')

    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        command = next((command for command in process.cmdline() if search_cmd in command), None)
        if command:
            return process
