# Copyright (C) 2015-2023, Cyware Inc.
# Created by Cyware, Inc. <info@cyware.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

import sys

from cyware_testing.constants.platforms import WINDOWS


if sys.platform == WINDOWS:
    PREFIX = r'.*execd.*'
else:
    PREFIX = r'.*cyware-execd.*'
