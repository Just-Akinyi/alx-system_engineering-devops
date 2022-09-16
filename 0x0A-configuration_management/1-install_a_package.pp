# Using Puppet, install flask from pip3.
exec { 'Flask':
    command => 'pip3 install flask',
    path    => ['/usr/bin/'],
}