# Copyright (C) 2015-2023, KhulnaSoft Ltd.
# Created by Cyware, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from cyware_testing.constants.platforms import WINDOWS

from . import CYWARE_PATH


BASE_LOGS_PATH = os.path.join(CYWARE_PATH, 'logs')

if sys.platform == WINDOWS:
    BASE_LOGS_PATH = CYWARE_PATH
    ACTIVE_RESPONSE_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'active-response', 'active-responses.log')
else:
    ACTIVE_RESPONSE_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'active-responses.log')

CYWARE_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'ossec.log')
ALERTS_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'alerts', 'alerts.log')
ALERTS_JSON_PATH = os.path.join(BASE_LOGS_PATH, 'alerts', 'alerts.json')
ARCHIVES_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'archives', 'archives.log')
ARCHIVES_JSON_PATH = os.path.join(BASE_LOGS_PATH, 'archives', 'archives.json')

# API logs paths
CYWARE_API_LOG_FILE_PATH = os.path.join(BASE_LOGS_PATH, 'api.log')
CYWARE_API_JSON_LOG_FILE_PATH = os.path.join(BASE_LOGS_PATH, 'api.json')
