#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## add user centoslive to groups
## allow group developers to run any command on LiveCD
##
if is_liveimg_run ; then
    usermod --append --groups developers centoslive || :
    usermod --append --groups dialout centoslive || :
    usermod --append --groups users centoslive || :
    usermod --append --groups uucp centoslive || :
    usermod --append --groups wireshark centoslive || :
    if [ -s /etc/sudoers.d/developers ] ; then
        echo "" >>/etc/sudoers.d/developers
        echo "%developers ALL = (ALL) NOPASSWD: ALL" >>/etc/sudoers.d/developers
        /sbin/restorecon /etc/sudoers.d/developers
    fi
fi

