# Copyright (C) 2015-2023, KhulnaSoft Ltd.
# Created by Cyware, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import random
from typing import List

from cyware_testing.constants.paths.configurations import CYWARE_CLIENT_KEYS_PATH
from cyware_testing.utils import file


def add_client_keys_entry(agent_id, agent_name, agent_ip='any', agent_key=None) -> None:
    """Add new entry to client keys file. If the agent_id already exists, this will be overwritten.

    Args:
        agent_id (str): Agent identifier.
        agent_name (str): Agent name.
        agent_ip (str): Agent ip.
        agent_key (str): Agent key.
    """
    registered_client_key_entries_dict = {}

    # Generate new key if necessary
    if agent_key is None:
        agent_key = ''.join(random.choice('0123456789abcdef') for i in range(64))

    # Read client keys data
    with open(CYWARE_CLIENT_KEYS_PATH, 'r') as client_keys:
        registered_client_key_entries_str = client_keys.readlines()

    # Process current client key entries
    for client_key_entry in registered_client_key_entries_str:
        _agent_id, _agent_name, _agent_ip, _agent_key = client_key_entry.split()
        registered_client_key_entries_dict[_agent_id] = f"{_agent_id} {_agent_name} {_agent_ip} {_agent_key}"

    # Add the new client key entry
    registered_client_key_entries_dict[agent_id] = f"{agent_id} {agent_name} {agent_ip} {agent_key}"

    # Save new client keys content
    with open(CYWARE_CLIENT_KEYS_PATH, 'w') as client_keys:
        for _, client_key_entry in registered_client_key_entries_dict.items():
            client_keys.write(f"{client_key_entry}\n")


def delete_client_keys_entry(agent_id) -> None:
    """Delete an entry from client keys file.

    Args:
        agent_id (str): Agent identifier.
    """
    registered_client_key_entries_dict = {}

    # Read client keys data
    with open(CYWARE_CLIENT_KEYS_PATH, 'r') as client_keys:
        registered_client_key_entries_str = client_keys.readlines()

    # Process current client key entries
    for client_key_entry in registered_client_key_entries_str:
        _agent_id, _agent_name, _agent_ip, _agent_key = client_key_entry.split()
        registered_client_key_entries_dict[_agent_id] = f"{_agent_id} {_agent_name} {_agent_ip} {_agent_key}"

    # Remove client key entry
    registered_client_key_entries_dict.pop(agent_id, None)

    # Save new client keys content
    with open(CYWARE_CLIENT_KEYS_PATH, 'w') as client_keys:
        for _, client_key_entry in registered_client_key_entries_dict.items():
            client_keys.write(f"{client_key_entry}\n")


def get_client_keys(path: str = CYWARE_CLIENT_KEYS_PATH) -> List[dict]:
    """Get client keys from a file.

    Args:
        path (str, optional): Path to the file containing the client keys.
            Defaults to CYWARE_CLIENT_KEYS_PATH.

    Returns:
        List[dict]: A list of dictionaries representing the client keys.
            Each dictionary contains the following keys: 'id', 'name', 'ip', and 'key'.
    """
    if not file.exists_and_is_file(path):
        return [{'id': 100, 'name': 'ubuntu-agent', 'ip': 'any', 'key': 'TopSecret'}]

    keys = []
    for line in file.read_file_lines(path):
        (id, name, ip, key) = line.replace('\n', '').split(' ')
        keys.append({'id': id, 'name': name, 'ip': ip, 'key': key})

    return keys
