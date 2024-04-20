# Create a Puppet Manifest that kills
# a process called killmenow
# use the exec resource
# use the pkill command

exec { 'killmenow':
  command    => '/usr/bin/pkill killmenow'
}
