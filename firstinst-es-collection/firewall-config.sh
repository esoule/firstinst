#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## /etc/sysconfig/iptables, system-config-firewall et al
##
## NOTE: have to do it here, because kickstart firewall
## option is not giving the expected result for LiveCD
## and, also, not all rules can be specified that way
##
install -d -m 0700 /etc/sysconfig/iptables-local
for fn in ipv4-filter-{forward,nfs,ntp} ; do
    install -p -m 0600 /usr/lib/firstinst/firewall-config/iptables-local-${fn}.txt    \
        /etc/sysconfig/iptables-local/${fn}
done
/sbin/restorecon -r /etc/sysconfig/iptables-local
for fn in system-config-firewall {ip,ip6}tables{,-config} ; do
    install -p -m 0600 /usr/lib/firstinst/firewall-config/${fn}.txt    \
        /etc/sysconfig/${fn}
    /sbin/restorecon /etc/sysconfig/${fn}
done

