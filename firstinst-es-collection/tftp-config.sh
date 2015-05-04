#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## move tftp home directory to /srv/tftpboot
##
mkdir /srv/tftpboot
/usr/bin/chcon -u system_u -r object_r -t tftpdir_rw_t /srv/tftpboot
if [ -s /etc/xinetd.d/tftp ] ; then
    sed -i -e 's!/var/lib/tftpboot!/srv/tftpboot!g' /etc/xinetd.d/tftp
    /sbin/restorecon /etc/xinetd.d/tftp
fi

