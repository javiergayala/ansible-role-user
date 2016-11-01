import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('inventory').get_hosts('pci')


# @pytest.mark.docker_images("centos:7")
@pytest.mark.docker_images("node-a")
@pytest.mark.parametrize("username", ["deployment", "user1"])
def test_pci_user_creation(User, File, username):
    userchk = User(username)
    sshauthkey = File('/home/%s/.ssh/authorized_keys' % username)
    assert userchk.exists
    assert userchk.name == username
    assert userchk.home == "/home/%s" % username
    assert sshauthkey.exists
    assert sshauthkey.mode == 0o600
    assert sshauthkey.user == username
    assert sshauthkey.group == username
    assert sshauthkey.contains("RdK8jlqm8tehUc9c9WhQ==")


@pytest.mark.docker_images("node-a")
def test_sudoers(File):
    sudoersfile = File('/etc/sudoers')
    assert sudoersfile.contains("deployment  ALL=(ALL)  NOPASSWD:ALL")
