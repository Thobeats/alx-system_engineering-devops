# Install flask using pip3
package { 'flask_installation':
  name     => 'flask',
  ensure   => '2.1.0',
  provider => 'pip3'
}
