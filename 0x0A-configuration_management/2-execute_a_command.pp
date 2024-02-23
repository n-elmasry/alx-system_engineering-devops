# a manifest that kills a process named killmenow.
exec { 'killmenow',
    comman => '/user/bin/pkill -f killmenow'
}
