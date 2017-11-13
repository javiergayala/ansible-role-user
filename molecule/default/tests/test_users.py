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
    assert not userchk.exists
    assert not sshauthkey.exists


@pytest.mark.parametrize("username", ["jenkins"])
def test_prompt_ignore_user(host, username):
    userchk = host.user(username)
    bash_prompt = host.file('/etc/profile.d/Z99-bash_prompt.sh')
    assert userchk.exists
    assert bash_prompt.contains(re.escape('jenkins'))
