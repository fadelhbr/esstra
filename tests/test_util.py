# SPDX-FileCopyrightText: Copyright 2024-2025 Sony Group Corporation
# SPDX-License-Identifier: MIT

import pytest

from conftest import run_command

ESSTRA_UTIL = 'util/esstra'


@pytest.mark.util_test(serial="01")
def test_util_version_short():
    '''Test the `esstra -V` global option

    Command:
        $ esstra.py -V

    Expected Behaviour:
        Tool name and version are printed with exit code 0.
    '''
    stdout, stderr, return_code = run_command(f'{ESSTRA_UTIL} -V')
    assert return_code == 0
    assert 'ESSTRA Utility' in stdout


@pytest.mark.util_test(serial="02")
def test_util_version_long():
    '''Test the `esstra --version` global option

    Command:
        $ esstra.py --version

    Expected Behaviour:
        Tool name and version are printed with exit code 0.
    '''
    stdout, stderr, return_code = run_command(f'{ESSTRA_UTIL} --version')
    assert return_code == 0
    assert 'ESSTRA Utility' in stdout
