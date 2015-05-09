#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

cat <<"__GITCONFIG__" >/root/.gitconfig
[user]
	name = root at localhost
	email = root@localhost.localdomain
__GITCONFIG__

chmod 0644 /root/.gitconfig
/sbin/restorecon /root/.gitconfig
