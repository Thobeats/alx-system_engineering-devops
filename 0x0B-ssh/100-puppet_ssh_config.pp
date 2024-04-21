# set up your client SSH configuration file
# so that you can connect to a server without
# typing a password.
file {'/etc/ssh/ssh_config':
  content     => 'Host 54.237.67.242
                    PasswordAuthentication no
                    IdentityFile ~/.ssh/school'
}