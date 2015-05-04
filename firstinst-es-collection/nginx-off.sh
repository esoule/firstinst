#!/bin/bash
source /etc/firstinst/firstinst-functions
##
## disable nginx for both LiveCD and hard drive
##
/sbin/chkconfig nginx off
