import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('inventory').get_hosts('non-pci')


# @pytest.mark.docker_images("centos:7")
@pytest.mark.docker_images("node-c")
def test_bash_prompt(File, Command):
    cmd = Command("hostname")
    prompt = File("/etc/profile.d/Z99-bash_prompt.sh")
    test_string = """
    PS1="\[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;196m\]\u\
    [$(tput sgr0)\]\[\033[38;5;15m\]@\h-\[$(tput sgr0)\]
    \[\033[38;5;14m\]TEST\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput bold)\]
    \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;46m\]|DEV|
    \[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;15m\]:\n\[$(tput sgr0)\]
    \[\033[38;5;6m\][\w]\[$(tput bold)\]\[$(tput sgr0)\]\[\033[38;5;46m\]>
    \[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]"
    """
    print("%s", prompt.content_string)
    print("Hostname: %s", cmd.stdout)
    assert prompt.contains(test_string)
    assert prompt.user == "root"
    assert prompt.group == "root"
    assert prompt.mode == 0o644
