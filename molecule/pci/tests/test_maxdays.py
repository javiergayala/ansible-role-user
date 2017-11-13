import os
import re
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644


@pytest.mark.parametrize('config_line', [
  'PASS_MAX_DAYS 90',
])
def test_maxdays_entry(host, config_line):
    login_defs = host.file("/etc/login.defs")
    regextest = re.escape(config_line)
    print '^{}$'.format(regextest)
    assert login_defs.contains('{}'.format(regextest))
