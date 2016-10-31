import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('inventory').get_hosts('non-pci')


# This test will run on both debian:jessie and centos:7 images
# @pytest.mark.docker_images("debian:jessie", "centos:7")
# def test_multiple(Process):
#     assert Process.get(pid=1).comm == "tail"


@pytest.mark.docker_images("node-b")
def test_passwd_file(File):
    passwd = File("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644


@pytest.mark.docker_images("node-b")
# @pytest.mark.env("group1")
def test_maxdays_entry(File):
    login_defs = File("/etc/login.defs")
    assert login_defs.contains("PASS_MAX_DAYS")
    # assert login_defs.user == "root"
    # assert login_defs.group == "root"
    # assert login_defs.mode == 0o644
