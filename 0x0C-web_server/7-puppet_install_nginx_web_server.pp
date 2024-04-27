# Install Nginx
package { 'nginx':
    ensure => installed,
}

# Ensure the directory exists
file { '/etc/nginx/sites-available':
    ensure => directory,
}

# Create or manage the content of the default file
file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => template('nginx/default.erb'),
}

# Manage the redirect line in the default file
file_line { 'redirect_me':
    ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    require => File['/etc/nginx/sites-available/default'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}
