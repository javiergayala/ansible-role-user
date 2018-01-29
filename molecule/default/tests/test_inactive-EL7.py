import os
import re
import pytest

import testinfra.utils.ansible_runner

# testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
#     os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ansible-user-default')


@pytest.mark.parametrize('config_line', [
  'INACTIVE=-1',
])
def test_pci_useradd_file(host, config_line):
    useradd = host.file("/etc/default/useradd")
    regextest = re.escape(config_line)
    assert useradd.contains('^{}$'.format(regextest))
    assert useradd.user == "root"
    assert useradd.group == "root"
    assert useradd.mode == 0o644
