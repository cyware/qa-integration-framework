# Copyright (C) 2015-2023, Cyware Inc.
# Created by Cyware, Inc. <info@cyware.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os

from . import CYWARE_PATH


QUEUE_CLUSTER_PATH = os.path.join(CYWARE_PATH, 'queue', 'cluster')
QUEUE_DB_PATH = os.path.join(CYWARE_PATH, 'queue', 'db')
QUEUE_SOCKETS_PATH = os.path.join(CYWARE_PATH, 'queue', 'sockets')

ANALYSISD_ANALISIS_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'analysis')
ANALYSISD_QUEUE_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'queue')
AUTHD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'auth')
EXECD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'com')
LOGCOLLECTOR_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'logcollector')
LOGTEST_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'logtest')
MODULESD_WMODULES_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'wmodules')
MODULESD_DOWNLOAD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'download')
MODULESD_CONTROL_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'control')
MODULESD_KREQUEST_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'krequest')
MODULESD_C_INTERNAL_SOCKET_PATH = os.path.join(QUEUE_CLUSTER_PATH, 'c-internal.sock')
MONITORD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'monitor')
REMOTED_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'remote')
SYSCHECKD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'syscheck')
CYWARE_DB_SOCKET_PATH = os.path.join(QUEUE_DB_PATH, 'wdb')

CYWARE_SOCKETS = {
    'cyware-agentd': [],
    'cyware-apid': [],
    'cyware-agentlessd': [],
    'cyware-csyslogd': [],
    'cyware-analysisd': [
        ANALYSISD_ANALISIS_SOCKET_PATH,
        ANALYSISD_QUEUE_SOCKET_PATH
    ],
    'cyware-authd': [AUTHD_SOCKET_PATH],
    'cyware-execd': [EXECD_SOCKET_PATH],
    'cyware-logcollector': [LOGCOLLECTOR_SOCKET_PATH],
    'cyware-monitord': [MONITORD_SOCKET_PATH],
    'cyware-remoted': [REMOTED_SOCKET_PATH],
    'cyware-maild': [],
    'cyware-syscheckd': [SYSCHECKD_SOCKET_PATH],
    'cyware-db': [CYWARE_DB_SOCKET_PATH],
    'cyware-modulesd': [
        MODULESD_WMODULES_SOCKET_PATH,
        MODULESD_DOWNLOAD_SOCKET_PATH,
        MODULESD_CONTROL_SOCKET_PATH,
        MODULESD_KREQUEST_SOCKET_PATH
    ],
    'cyware-clusterd': [MODULESD_C_INTERNAL_SOCKET_PATH]
}

# These sockets do not exist with default Cyware configuration
CYWARE_OPTIONAL_SOCKETS = [
    MODULESD_KREQUEST_SOCKET_PATH,
    AUTHD_SOCKET_PATH
]
