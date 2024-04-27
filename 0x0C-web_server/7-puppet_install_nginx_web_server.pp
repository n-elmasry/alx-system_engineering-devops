# install Nginx
package { 'nginx':
    ensure => installed,

}

file { '/var/www/html/index.html':
    content => 'Hello World!',
}

file_line { 'redirect_me':
    ensure => present,
    path => '/etc/nginx/sites-available/default',
    line => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    require => Package['nginx'],

}
service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
}
