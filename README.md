# javiergayala.users

![Molecule](https://github.com/javiergayala/ansible-role-user/workflows/Molecule/badge.svg) ![Ansible Role](https://img.shields.io/ansible/role/48462?logo=ansible) ![Ansible Role](https://img.shields.io/ansible/role/d/48462) ![Ansible Quality Score](https://img.shields.io/ansible/quality/48462) ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/javiergayala/ansible-role-user?sort=semver) ![GitHub Release Date](https://img.shields.io/github/release-date/javiergayala/ansible-role-user)

This is an opinionated role that creates users on servers.

## Role Variables

- `users_list`: list containing dictionaries of users to add

  - `name`: username to create
  - `groups`: comma delimited list of secondary groups. Defaults to none.
  - `ssh_key`: text string containing the user's public ssh key which will be placed in `/home/$USER/.ssh/authorized_keys`
  - `sudoers`: if set to `yes`, user will be added to the server's sudoers file.
  - `sudo_opts`: dictionary containing options to use for the sudoers file.

    - `passwordless`: (Boolean) defaults to "`False`". Set to "`True`" to allow `sudo` commands to not prompt for a password.
    - `hosts`: defaults to `ALL`. Hosts that user is allowed to run `sudo` on.
    - `run_as`: defaults to `(ALL)`. Users allowed to run sudo commands as.
    - `commands`: defaults to `ALL`. Commands user is allowed to run with `sudo`.
    - `requiretty`: (Boolean) not set by default. Set to `False` to disable the requirement for a TTY when using sudo.

  - `user_sshkey_exclusive`: defaults to `no`. Setting to `yes` tells ansible to manage the keys in the `authorized_keys` file, and removes any not defined in the play.

  - `use_os_prompt`: defaults to `no`. Setting to `yes` or `True` will make it so that this user does **NOT** use the specialized bash prompt. This is useful for service accounts, such as the `jenkins` or `rswebteam` deployment account, or any accounts that do not use a `TTY`.

```yml
users_list:
  - name: deployment
    groups: apache
    ssh_key: >
      ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGY
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      RdK8jlqm8tehUc9c9WhQ== vagrant insecure public key
    sudoers: "yes"
    sudo_opts:
      passwordless: "True"
      hosts: "ALL"
      run_as: "(ALL)"
      commands: "ALL"
      requiretty: "False"
    use_os_prompt: "yes"
  - name: user1
    ssh_key: https://github.com/javiergayala.keys
    sudoers: "no"
  - name: user2
```

## Example Playbook

```yml
- hosts: servers
  roles:
    - { role: javiergayala.users, users_list: [{ name: user1 }] }
```

## Testing

You will need the following in order test and run this role:

- [Ansible](http://docs.ansible.com/ansible/intro_installation.html)
- [Docker](https://docs.docker.com/engine/installation/)
- Python modules listed in the `pip-requirements.txt` file
- [Molecule](https://molecule.readthedocs.io/)

It is highly recommended that you use a virtualenv for testing:

```bash
PYENV_HOME=$WORKSPACE/.pyenv/

# Delete previously built virtualenv
if [ -d $PYENV_HOME ]; then
    rm -rf $PYENV_HOME
fi

# Create virtualenv and install necessary packages
virtualenv --no-site-packages $PYENV_HOME
. $PYENV_HOME/bin/activate
pip install -r pip-requirements.txt

molecule test --all
```

## License

BSD

## Author Information

Javier Ayala [javier.g.ayala@gmail.com](mailto:javier.g.ayala@gmail.com)
