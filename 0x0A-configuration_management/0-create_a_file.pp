# This manifest ensures the existence of a file at '/etc/school'
# with specific permision, owner, group and content.
file { '/tmp/school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
