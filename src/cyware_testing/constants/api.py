"""
Copyright (C) 2015-2023, Cyware Inc.
Created by Cyware, Inc. <info@cyware.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
# API basic information
CONFIGURATION_TYPES = ('base', 'security')
CYWARE_API_PROTOCOL = 'https'
CYWARE_API_HOST = 'localhost'
CYWARE_API_PORT = '55000'
CYWARE_API_USER = 'cyware'
CYWARE_API_PASSWORD = 'cyware'

# API routes
LOGIN_ROUTE = '/security/user/authenticate'
RULES_FILES_ROUTE = '/rules/files'
AGENTS_ROUTE = '/agents'
SYSCOLLECTOR_OS_ROUTE = '/experimental/syscollector/os'
MANAGER_INFORMATION_ROUTE = '/manager/info'
GROUPS_ROUTE = '/groups'
CDB_LIST_ROUTE = '/lists/files'
DAEMONS_STATS_ROUTE = '/manager/daemons/stats'
# RBAC routes
USERS_ROUTE = '/security/users'
ROLES_ROUTE = '/security/roles'
POLICIES_ROUTE = '/security/policies'
RULES_ROUTE = '/security/rules'
RESOURCE_ROUTE_MAP = {
    'user_ids': USERS_ROUTE,
    'role_ids': ROLES_ROUTE,
    'policy_ids': POLICIES_ROUTE,
    'rule_ids': RULES_ROUTE
}
TARGET_ROUTE_MAP = {
    'user_ids': 'users',
    'role_ids': 'roles',
    'policy_ids': 'policies',
    'rule_ids': 'rules'
}
