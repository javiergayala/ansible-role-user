import os
import pytest
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("username", ["deployment"])
def test_pci_user_creation(host, username):
    userchk = host.user(username)
    sshauthkey = host.file('/home/%s/.ssh/authorized_keys' % username)
    assert userchk.exists
    assert userchk.name == username
    assert userchk.home == "/home/%s" % username
    assert userchk.groups == ['deployment', 'sudo']
    assert sshauthkey.exists
    assert sshauthkey.mode == 0o600
    assert sshauthkey.user == username
    assert sshauthkey.group == username
    assert sshauthkey.contains("RdK8jlqm8tehUc9c9WhQ==")


@pytest.mark.parametrize('config_line', [
    'deployment',
])
def test_sudoers(host, config_line):
    sudoersfile = host.file('/etc/sudoers')
    regextest = re.escape(config_line)
    assert sudoersfile.contains('^{}'.format(regextest))
