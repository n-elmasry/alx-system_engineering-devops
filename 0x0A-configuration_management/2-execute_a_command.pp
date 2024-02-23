# a manifest that kills a process named killmenow.
exec {'killmenow':
    command => 'pkill killmenow',
    path    => '/user/bin/pkill '
}
