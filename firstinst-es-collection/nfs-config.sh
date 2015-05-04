#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## /etc/sysconfig/nfs
##
if [ -s /etc/sysconfig/nfs ] ; then
    sed -i -e 's,^\s*#\s*\(RQUOTAD_PORT\|LOCKD_TCPPORT\|LOCKD_UDPPORT\|MOUNTD_PORT\|STATD_PORT\|STATD_OUTGOING_PORT\)=,\1=,' /etc/sysconfig/nfs
    /sbin/restorecon /etc/sysconfig/nfs
fi

