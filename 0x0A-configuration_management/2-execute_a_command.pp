# a manifest that kills a process named killmenow.
exec {'killmenow',
    command => '/user/bin/pkill -f killmenow'
}
