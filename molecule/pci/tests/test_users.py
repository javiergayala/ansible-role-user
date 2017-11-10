import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("username", ["deployment"])
def test_pci_user_creation(host, username):
    userchk = host.user(username)
    sshauthkey = host.file('/home/%s/.ssh/authorized_keys' % username)
    assert not userchk.exists
    assert not sshauthkey.exists
