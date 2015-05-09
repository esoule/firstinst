#!/bin/bash
source /usr/lib/firstinst/firstinst-functions
##
## disable nginx for both LiveCD and hard drive
##
/sbin/chkconfig nginx off
