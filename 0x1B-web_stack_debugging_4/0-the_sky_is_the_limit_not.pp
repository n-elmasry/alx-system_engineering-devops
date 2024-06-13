# fix our stack

exec { 'debugging--for-nginx':
  command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}
# Restart Nginx
exec { 'nginx-restart':
  command => '/usr/sbin/service nginx restart',
}
