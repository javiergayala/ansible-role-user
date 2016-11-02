ansible-user
=========

This role creates the users needed on the servers for the rswebteam's users.

Role Variables
--------------

- ```raxusers```: list containing dictionaries of users to add
  - ```name```: username to create
  - ```groups```: comma delimited list of secondary groups. Defaults to none.
  - ```ssh_key```: text string containing the user's public ssh key which will be placed in ```/home/$USER/.ssh/authorized_keys```
  - ```sudoers```: if set to ```yes```, user will be added to the server's sudoers file.
- ```user_sshkey_exclusive```: defaults to ```no```. Setting to ```yes``` tells ansible to manage the keys in the ```authorized_keys``` file, and removes any not defined in the play.


    - raxusers:
      - name: deployment
        groups: apache
        ssh_key: >
          ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGY
          e7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoP
          kcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0z
          QPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbU
          vxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCz
          RdK8jlqm8tehUc9c9WhQ== vagrant insecure public key
        sudoers: yes
      - name: user1
        ssh_key: >
          ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGY
          e7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoP
          kcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0z
          QPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbU
          vxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCz
          RdK8jlqm8tehUc9c9WhQ== vagrant insecure public key
        sudoers: no
      - name: user2

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-user, raxusers: [{ name: user1 }] }

License
-------

BSD

Author Information
------------------

Javier Ayala
[jayala@rackspace.com](jayala@rackspace.com)
