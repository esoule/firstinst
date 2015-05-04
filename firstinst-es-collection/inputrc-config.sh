#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## /etc/inputrc
##
if [ -s /etc/inputrc ] ; then
    sed -i -e 's!#set bell-style none!set bell-style none!;' /etc/inputrc

cat <<"____EOF" >>/etc/inputrc

$if mode=emacs
# for PuTTY
"\eOC": forward-word
"\eOD": backward-word
$endif
____EOF

    /sbin/restorecon /etc/inputrc
fi
