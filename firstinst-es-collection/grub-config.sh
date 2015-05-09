#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

if is_liveimg_run ; then
    exit 0
fi

if [ -f /boot/grub/grub.conf -a -s /boot/grub/grub.conf ] ; then
    cp --archive /boot/grub/grub.conf /boot/grub/grub.conf.centos-livecd-scripts.orig

    sed -i -e 's!^\s*hiddenmenu\s*$!!;'    \
        -e 's!^\s*timeout=[0-9]\+\s*$!timeout=10!;'    \
        -e 's!title anaconda bluesky!title CentOS 6!;'    \
        -e 's!^\(\s*kernel.*\)\brhgb\b\(.*\)$!\1vga=791\2!;'    \
        /boot/grub/grub.conf

    chmod 0600 /boot/grub/grub.conf
    /sbin/restorecon /boot/grub/grub.conf
fi

exit 0
