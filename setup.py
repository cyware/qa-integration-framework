"""
Copyright (C) 2015-2023, Cyware Inc.
Created by Cyware, Inc. <info@cyware.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import shutil

from pathlib import Path
from setuptools import setup, find_packages
from typing import List


# Extra data.
package_data_list = [
    'data/all_disabled_ossec.conf',
    'data/analysis_alert.json',
    'data/analysis_alert_windows.json',
    'data/mitre_event.json',
    'data/keepalives.txt',
    'data/rootcheck.txt',
    'data/statistics_template/agent_statistics_format_test_module/cyware-analysisd_template.json',
    'data/statistics_template/agent_statistics_format_test_module/cyware-remoted_template.json',
    'data/statistics_template/manager_statistics_format_test_module/cyware-analysisd_template.json',
    'data/statistics_template/manager_statistics_format_test_module/cyware-db_template.json',
    'data/statistics_template/manager_statistics_format_test_module/cyware-remoted_template.json'
]

# Entry point scripts.
scripts_list = []


def get_install_requires() -> List[str]:
    """Returns requirements.txt parsed to a list"""
    fname = Path(__file__).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets


setup(
    name='cyware_testing',
    version='4.8.0',
    description='Cyware testing utilities to help programmers automate tests',
    url='https://github.com/cyware',
    author='Cyware',
    author_email='hello@cyware.com',
    license='GPLv2',
    packages=find_packages(where='src'),
    package_dir={'cyware_testing': 'src/cyware_testing'},
    package_data={'cyware_testing': package_data_list},
    python_requires='>=3.8',
    install_requires=get_install_requires(),
    entry_points={'console_scripts': scripts_list},
    include_package_data=True,
    zip_safe=False
)

# Clean build files
shutil.rmtree('src/dist', ignore_errors=True)
shutil.rmtree('src/build', ignore_errors=True)
shutil.rmtree('src/cyware_testing.egg-info', ignore_errors=True)
