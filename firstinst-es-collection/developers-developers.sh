#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## add group developers, if missing
##
{ /usr/bin/getent group developers >/dev/null ; } || /usr/sbin/groupadd -r developers

