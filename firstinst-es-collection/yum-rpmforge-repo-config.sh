#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## /etc/yum.repos.d/rpmforge.repo
##
if [ -s /etc/yum.repos.d/rpmforge.repo ] ; then
    sed -i -e 's,^\(enabled\s*=\s*\)1,\1''0,g' /etc/yum.repos.d/rpmforge.repo
    sed -i -e '/gpgcheck/a exclude=sqlite*' /etc/yum.repos.d/rpmforge.repo
    /sbin/restorecon /etc/yum.repos.d/rpmforge.repo
fi
