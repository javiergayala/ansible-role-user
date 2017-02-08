import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('inventory').get_hosts('non-pci')


# @pytest.mark.docker_images("centos:7")
@pytest.mark.docker_images("node-c")
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


@pytest.mark.docker_images("node-c")
def test_sudo_group(User):
    groupchk = User('deployment')
    assert groupchk.groups == ['deployment', 'sudo']


@pytest.mark.docker_images("node-c")
@pytest.mark.parametrize("username", ["user1", "user2"])
def test_secondary_group(User, username):
    groupchk = User(username)
    assert groupchk.groups == [username]


@pytest.mark.docker_images("node-c")
def test_sudoers(File):
    sudoersfile = File('/etc/sudoers')
    assert sudoersfile.contains("deployment  ALL=(ALL)  NOPASSWD:ALL")
