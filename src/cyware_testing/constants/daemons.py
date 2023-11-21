# Copyright (C) 2015-2023, KhulnaSoft Ltd.
# Created by Cyware, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

AGENT_DAEMON = 'cyware-agentd'
AGENTLESS_DAEMON = 'cyware-agentlessd'
ANALYSISD_DAEMON = 'cyware-analysisd'
API_DAEMON = 'cyware-apid'
CLUSTER_DAEMON = 'cyware-clusterd'
CSYSLOG_DAEMON = 'cyware-csyslogd'
EXEC_DAEMON = 'cyware-execd'
INTEGRATOR_DAEMON = 'cyware-integratord'
MAIL_DAEMON = 'cyware-maild'
MODULES_DAEMON = 'cyware-modulesd'
MONITOR_DAEMON = 'cyware-monitord'
LOGCOLLECTOR_DAEMON = 'cyware-logcollector'
REMOTE_DAEMON = 'cyware-remoted'
SYSCHECK_DAEMON = 'cyware-syscheckd'
CYWARE_DB_DAEMON = 'cyware-db'

CYWARE_AGENT_DAEMONS = [AGENT_DAEMON,
                       EXEC_DAEMON,
                       MODULES_DAEMON,
                       LOGCOLLECTOR_DAEMON,
                       SYSCHECK_DAEMON]

CYWARE_MANAGER_DAEMONS = [AGENTLESS_DAEMON,
                         ANALYSISD_DAEMON,
                         API_DAEMON,
                         CLUSTER_DAEMON,
                         CSYSLOG_DAEMON,
                         EXEC_DAEMON,
                         INTEGRATOR_DAEMON,
                         LOGCOLLECTOR_DAEMON,
                         MAIL_DAEMON,
                         MODULES_DAEMON,
                         MONITOR_DAEMON,
                         REMOTE_DAEMON,
                         SYSCHECK_DAEMON,
                         CYWARE_DB_DAEMON]

API_DAEMONS_REQUIREMENTS = [API_DAEMON,
                            CYWARE_DB_DAEMON,
                            EXEC_DAEMON,
                            ANALYSISD_DAEMON,
                            REMOTE_DAEMON,
                            MODULES_DAEMON]

CYWARE_AGENT = 'cyware-agent'
CYWARE_MANAGER = 'cyware-manager'

CYWARE_AGENT_WIN = 'cyware-agent.exe'
