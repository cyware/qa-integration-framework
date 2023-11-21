# Copyright (C) 2015-2023, KhulnaSoft Ltd.
# Created by Cyware, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os

from cyware_testing.tools.socket_controller import SocketController
from cyware_testing.constants.paths.sockets import QUEUE_SOCKETS_PATH, CYWARE_DB_SOCKET_PATH, \
                                                  MODULESD_C_INTERNAL_SOCKET_PATH


def delete_sockets(path=None):
    """Delete a list of Cyware socket files or all of them if None is specified.

    Args:
        path (list, optional): Absolute socket path. Default `None`.
    """
    try:
        if path is None:
            path = QUEUE_SOCKETS_PATH
            for file in os.listdir(path):
                os.remove(os.path.join(path, file))
            if os.path.exists(CYWARE_DB_SOCKET_PATH):
                os.remove(CYWARE_DB_SOCKET_PATH)
            if os.path.exists(MODULESD_C_INTERNAL_SOCKET_PATH):
                os.remove(MODULESD_C_INTERNAL_SOCKET_PATH)
        else:
            for item in path:
                os.remove(item)
    except FileNotFoundError:
        pass

def send_request_socket(query, socket_path=CYWARE_DB_SOCKET_PATH):
    """Send queries request to socket in the argument.

    Args:
        query (str): query request command. For example `agent {agent.id} rootcheck delete`.
        socket_path (str): by default use wdb socket.
    Returns:
        list: Query response data.
    """
    controller = SocketController(socket_path)
    controller.send(query, size=True)
    response = controller.receive(size=True)
    controller.close()

    return response
