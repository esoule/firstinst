#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## add user liveuser to groups
## allow group developers to run any command on LiveCD
##
if is_liveimg_run ; then
    usermod --append --groups developers liveuser || :
    usermod --append --groups dialout liveuser || :
    usermod --append --groups users liveuser || :
    usermod --append --groups uucp liveuser || :
    usermod --append --groups wireshark liveuser || :
    if [ -s /etc/sudoers.d/developers ] ; then
        echo "" >>/etc/sudoers.d/developers
        echo "%developers ALL = (ALL) NOPASSWD: ALL" >>/etc/sudoers.d/developers
        /sbin/restorecon /etc/sudoers.d/developers
    fi
fi

