#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## /etc/pam.d/gdm-password
##
if [ -s /etc/pam.d/gdm-password ] ; then
    sed -i -e '1s/^/auth        required      pam_succeed_if.so user != root quiet\n\n/'    /etc/pam.d/gdm-password
    /sbin/restorecon /etc/pam.d/gdm-password
fi
