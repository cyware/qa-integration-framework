# Copyright (C) 2015-2023, KhulnaSoft Ltd.
# Created by Cyware, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2


# Callback patterns to find events in log file.
MODULESD_CONFIGURATION_ERROR = r".*ERROR: {error_type} content for tag '{tag}' at module '{integration}'."
MODULESD_STARTED = r".*INFO: Module {integration} started."
