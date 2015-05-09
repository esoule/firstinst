#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## require NetworkManager apply both /etc/sysctl.conf and /etc/sysctl.d/*
## workaround for rhbz #1213118
##
if [ -s /etc/rc.d/init.d/NetworkManager ] ; then
    sed -i -e 's,sysctl [-]e [-]p /etc/sysctl\.conf,apply_sysctl,g' /etc/rc.d/init.d/NetworkManager
    /sbin/restorecon /etc/rc.d/init.d/NetworkManager
fi

