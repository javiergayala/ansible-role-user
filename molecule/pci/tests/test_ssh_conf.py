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


@pytest.mark.parametrize('config_line', [
  'PubkeyAuthentication yes',
  'ChallengeResponseAuthentication no',
  'PasswordAuthentication no',
  'UsePAM yes',
  'ClientAliveInterval 300',
  'ClientAliveCountMax 3'
])
def test_sshd_conf(host, config_line):
    sshd_conf = host.file('/etc/ssh/sshd_config')
    regextest = re.escape(config_line)
    assert sshd_conf.contains('^{}$'.format(regextest))
