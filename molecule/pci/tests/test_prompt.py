import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bash_prompt(host):
    prompt = host.file("/etc/profile.d/Z99-bash_prompt.sh")
    test_string = """
    PS1="\[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;196m\]\u\
    [$(tput sgr0)\]\[\033[38;5;15m\]@\h-\[$(tput sgr0)\]
    \[\033[38;5;14m\]TEST\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput bold)\]
    \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;196m\]|PROD|
    \[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;15m\]:\n\[$(tput sgr0)\]
    \[\033[38;5;6m\][\w]\[$(tput bold)\]\[$(tput sgr0)\]\[\033[38;5;46m\]>
    \[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]"
    """
    assert prompt.contains(test_string)
    assert prompt.user == "root"
    assert prompt.group == "root"
    assert prompt.mode == 0o644
