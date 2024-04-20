# Install flask using pip3
class flask {

  package {'werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3'
  }

  package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3'
  }
}

include flask