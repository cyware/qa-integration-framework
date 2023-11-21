"""
Copyright (C) 2015-2023, Cyware Inc.
Created by Cyware, Inc. <info@cyware.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import os
import sys

from cyware_testing.constants.platforms import WINDOWS

from . import CYWARE_PATH
from cyware_testing.constants.paths.api import CYWARE_API_FOLDER_PATH, CYWARE_API_SECURITY_FOLDER_PATH


if sys.platform == WINDOWS:
    BASE_CONF_PATH = CYWARE_PATH
else:
    BASE_CONF_PATH = os.path.join(CYWARE_PATH, 'etc')

CYWARE_CLIENT_KEYS_PATH = os.path.join(BASE_CONF_PATH, 'client.keys')
SHARED_CONFIGURATIONS_PATH = os.path.join(BASE_CONF_PATH, 'shared')
CYWARE_CONF_PATH = os.path.join(BASE_CONF_PATH, 'ossec.conf')
CYWARE_LOCAL_INTERNAL_OPTIONS = os.path.join(BASE_CONF_PATH, 'local_internal_options.conf')
ACTIVE_RESPONSE_CONFIGURATION = os.path.join(SHARED_CONFIGURATIONS_PATH, 'ar.conf')
AR_CONF = os.path.join(SHARED_CONFIGURATIONS_PATH, 'ar.conf')
CUSTOM_RULES_PATH = os.path.join(BASE_CONF_PATH, 'rules')
CUSTOM_RULES_FILE = os.path.join(CUSTOM_RULES_PATH, 'local_rules.xml')

# Cyware API configurations path
CYWARE_API_CONFIGURATION_PATH = os.path.join(CYWARE_API_FOLDER_PATH, 'configuration', 'api.yaml')
CYWARE_SECURITY_CONFIGURATION_PATH = os.path.join(CYWARE_API_SECURITY_FOLDER_PATH, 'security.yaml')
