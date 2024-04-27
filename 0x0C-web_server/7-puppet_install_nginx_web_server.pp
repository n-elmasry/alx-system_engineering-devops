# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Update the default HTML file
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
}

# Add the rewrite rule to the default Nginx configuration
file_line { 'redirect_me':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
}
