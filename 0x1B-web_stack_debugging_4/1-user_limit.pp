# 1-user_limit.pp

user { 'holberton':
  ensure     => present,
  shell      => '/bin/bash',
  managehome => true,
  groups     => ['sudo'],
}

exec { 'increase-open-file-limit':
  command => 'ulimit -n 4096',
  user    => 'holberton',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
  unless  => 'ulimit -n | grep -q 4096',
}
