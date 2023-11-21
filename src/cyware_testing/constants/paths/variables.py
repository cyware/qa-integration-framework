# Copyright (C) 2015-2023, Cyware Inc.
# Created by Cyware, Inc. <info@cyware.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from cyware_testing.constants.platforms import WINDOWS

from . import CYWARE_PATH


VAR_PATH = os.path.join(CYWARE_PATH, 'var')
VAR_RUN_PATH = os.path.join(VAR_PATH, 'run')

ANALYSISD_STATE = os.path.join(VAR_RUN_PATH, 'cyware-analysisd.state')

if sys.platform == WINDOWS:
    VERSION_FILE = os.path.join(CYWARE_PATH, 'VERSION')
else:
    VERSION_FILE = ''
