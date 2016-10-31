import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('inventory').get_hosts('pci')


# @pytest.mark.docker_images("centos:7")
@pytest.mark.docker_images("node-b")
def test_pci_useradd_file(File, Command):
    cmd = Command("hostname")
    useradd = File("/etc/default/useradd")
    print("%s", useradd.content_string)
    print("Hostname: %s", cmd.stdout)
    assert useradd.contains("INACTIVE=-1")
    assert useradd.user == "root"
    assert useradd.group == "root"
    assert useradd.mode == 0o644
