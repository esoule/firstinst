#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## /etc/vsftpd/vsftpd.conf
##
if [ -s /etc/vsftpd/vsftpd.conf ] ; then

cat <<"____EOF" >>/etc/vsftpd/vsftpd.conf

reverse_lookup_enable=NO
use_localtime=YES
____EOF

    /sbin/restorecon /etc/vsftpd/vsftpd.conf
fi    ## if [ -s /etc/vsftpd/vsftpd.conf ]

##
## move ftp home directory to /srv/ftp
##
mkdir /srv/ftp /srv/ftp/pub
/sbin/restorecon /srv/ftp /srv/ftp/pub
/usr/sbin/usermod --home=/srv/ftp ftp

