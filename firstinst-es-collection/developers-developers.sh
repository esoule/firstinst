#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## add group developers, if missing
## see /etc/sudoers.d/developers above
##
{ /usr/bin/getent group developers >/dev/null ; } || /usr/sbin/groupadd -r developers

##
## add user centoslive to groups
## allow group developers to run any command on LiveCD
##
if is_liveimg_run ; then
    usermod --append --groups developers,dialout,users,uucp,wireshark centoslive
    if [ -s /etc/sudoers.d/developers ] ; then
        echo "" >>/etc/sudoers.d/developers
        echo "%developers ALL = (ALL) NOPASSWD: ALL" >>/etc/sudoers.d/developers
        /sbin/restorecon /etc/sudoers.d/developers
    fi
fi

