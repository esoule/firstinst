#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## /etc/yum/pluginconf.d/fastestmirror.conf
##
if [ -s /etc/yum/pluginconf.d/fastestmirror.conf ] ; then
    sed -i -e '/^#exclude/a exclude=facebook,uottawa' /etc/yum/pluginconf.d/fastestmirror.conf
    /sbin/restorecon /etc/yum/pluginconf.d/fastestmirror.conf
fi

