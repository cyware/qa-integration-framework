# Copyright (C) 2015-2023, KhulnaSoft Ltd.
# Created by Cyware, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
from pathlib import Path

from . import global_parameters


DATA_PATH = Path(Path(__file__).parent, 'data')
SCRIPTS_PATH = Path(Path(__file__).parent, 'scripts')

session_parameters = global_parameters.GlobalParameters()
