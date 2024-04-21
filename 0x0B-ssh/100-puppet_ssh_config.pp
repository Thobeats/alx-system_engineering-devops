# set up your client SSH configuration file
# so that you can connect to a server without
# typing a password.
file {'/etc/ssh/school':
  content     => 'PasswordAuthentication no
  Identity ~/.ssh/school'
}