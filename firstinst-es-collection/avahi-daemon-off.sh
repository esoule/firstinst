#!/bin/bash
source /usr/lib/firstinst/firstinst-functions
##
## disable avahi-daemon in both Live and hard drive
##
/sbin/chkconfig --level 345 avahi-daemon off
