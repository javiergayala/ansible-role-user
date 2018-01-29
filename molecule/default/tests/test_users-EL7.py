"""Test user creation and sudoers setup."""
import os
import pytest
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ansible-user-default')


@pytest.mark.parametrize("username", ["deployment"])
def test_pci_user_creation(host, username):
    """Test that a user is NOT created (for PCI purposes).

    Parameters
    ----------
    host : object
        Description of parameter `host`.
    username : string
        The username that is created.

    Asserts
    -------
    userchk
        User does not exist.
    sshauthkey
        User's SSH Auth Key does not exist.

    """
    userchk = host.user(username)
    sshauthkey = host.file('/home/%s/.ssh/authorized_keys' % username)
    assert not userchk.exists
    assert not sshauthkey.exists


@pytest.mark.parametrize("username", ["jenkins"])
def test_prompt_ignore_user(host, username):
    """Test that a user does NOT get our special/fancy prompt.

    Parameters
    ----------
    host : object
        Description of parameter `host`.
    username : string
        The username that we want to test against.

    Asserts
    -------
    userchk
        User does exist.
    bash_prompt
        User's name is listed for ignore.

    """
    userchk = host.user(username)
    bash_prompt = host.file('/etc/profile.d/Z99-bash_prompt.sh')
    assert userchk.exists
    assert bash_prompt.contains(re.escape('jenkins'))


@pytest.mark.parametrize("username", ["rswebteam"])
def test_sudoers_setup_EL7(host, username):
    """Test that a user is setup with `sudo` access.

    Parameters
    ----------
    host : object
        Description of parameter `host`.
    username : string
        The username that is tested.

    Asserts
    -------
    userchk
        User does exist.
    sudoersfile
        User's sudoers file exists.
        User's sudoers file contains sudo privileges.

    """
    userchk = host.user(username)
    sudoersfile = host.file('/etc/sudoers.d/99-%s' % username)
    sudoline = ('%s ALL=(ALL) ALL' % username)
    assert userchk.exists
    assert sudoersfile.exists
    assert sudoersfile.contains(sudoline)


@pytest.mark.parametrize("username", ["rswebteam"])
def test_sudoers_tty_EL7(host, username):
    """Test that a user is setup with `sudo` access, and requires a tty.

    Parameters
    ----------
    host : object
        Description of parameter `host`.
    username : string
        The username that is tested.

    Asserts
    -------
    userchk
        User does exist.
    sudoersfile
        User's sudoers file exists.
        User's sudoers file contains sudo privileges.
        User's sudoers file does not disable `requiretty`.

    """
    userchk = host.user(username)
    sudoersfile = host.file('/etc/sudoers.d/99-%s' % username)
    sudoline = ('%s ALL=(ALL) ALL' % username)
    notty = ('Defaults:%s !requiretty' % username)
    assert userchk.exists
    assert sudoersfile.exists
    assert sudoersfile.contains(sudoline)
    assert not sudoersfile.contains(notty)


@pytest.mark.parametrize("username", ["rswebnotty"])
def test_sudoers_notty_EL7(host, username):
    """Test that a user is setup with `sudo` access, without requiring a tty.

    Parameters
    ----------
    host : object
        Description of parameter `host`.
    username : string
        The username that is tested.

    Asserts
    -------
    userchk
        User does exist.
    sudoersfile
        User's sudoers file exists.
        User's sudoers file contains sudo privileges.
        User's sudoers file disables `requiretty`.

    """
    userchk = host.user(username)
    sudoersfile = host.file('/etc/sudoers.d/99-%s' % username)
    sudoline = ('%s ALL=(ALL) NOPASSWD:ALL' % username)
    notty = ('Defaults:%s !requiretty' % username)
    assert userchk.exists
    assert sudoersfile.exists
    assert sudoersfile.contains(sudoline)
    assert sudoersfile.contains(notty)


@pytest.mark.parametrize("username", ["rswebnopw"])
def test_sudoers_nopw_setup_EL7(host, username):
    """Test that a user is setup with passwordless `sudo` access.

    Parameters
    ----------
    host : object
        Description of parameter `host`.
    username : string
        The username that is tested.

    Asserts
    -------
    userchk
        User does exist.
    sudoersfile
        User's sudoers file exists.
        User's sudoers file contains sudo privileges without a password.

    """
    userchk = host.user(username)
    sudoersfile = host.file('/etc/sudoers.d/99-%s' % username)
    sudoline = ('%s ALL=(ALL) NOPASSWD:ALL' % username)
    assert userchk.exists
    assert sudoersfile.exists
    assert sudoersfile.contains(sudoline)
