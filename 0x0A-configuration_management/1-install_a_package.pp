# Using Puppet, install flask from pip3.
package { 'Puppet-lint':
    ensure   => '2.1.1',
    provider => 'gem',
}
