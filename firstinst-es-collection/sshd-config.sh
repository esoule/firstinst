#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## /etc/ssh/sshd_config
##
sed -i -e 's,#PermitRootLogin yes,PermitRootLogin no,;s,#UseDNS yes,UseDNS no,;' /etc/ssh/sshd_config
/sbin/restorecon /etc/ssh/sshd_config

##
## disable sshd for LiveCD run
##
if is_liveimg_run ; then
    /sbin/chkconfig --level 2345 sshd off
fi
