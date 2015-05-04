#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## /etc/yum.repos.d/epel.repo
##
if [ -s /etc/yum.repos.d/epel.repo ] ; then
    sed -i -e '/gpgcheck/a exclude=wine*' /etc/yum.repos.d/epel.repo
    /sbin/restorecon /etc/yum.repos.d/epel.repo
fi
