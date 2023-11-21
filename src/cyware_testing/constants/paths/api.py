"""
Copyright (C) 2015-2023, Cyware Inc.
Created by Cyware, Inc. <info@cyware.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import os

from . import CYWARE_PATH

# API paths that do not fit in `configurations`

# Folders
CYWARE_API_FOLDER_PATH = os.path.join(CYWARE_PATH, 'api')
CYWARE_API_CONFIGURATION_FOLDER_PATH = os.path.join(CYWARE_API_FOLDER_PATH, 'configuration')
CYWARE_API_SECURITY_FOLDER_PATH = os.path.join(CYWARE_API_CONFIGURATION_FOLDER_PATH, 'security')
CYWARE_API_SCRIPTS_FOLDER_PATH = os.path.join(CYWARE_API_FOLDER_PATH, 'scripts')

# API scripts paths
CYWARE_API_SCRIPT = os.path.join(CYWARE_API_SCRIPTS_FOLDER_PATH, 'cyware-apid.py')

# Databases paths
RBAC_DATABASE_PATH = os.path.join(CYWARE_API_SECURITY_FOLDER_PATH, 'rbac.db')

# SSL paths
CYWARE_API_CERTIFICATE = os.path.join(CYWARE_API_CONFIGURATION_FOLDER_PATH, 'ssl', 'server.crt')
