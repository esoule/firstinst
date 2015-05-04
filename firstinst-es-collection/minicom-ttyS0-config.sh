#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## /etc/minirc.dfl
##

cat <<"___FILE1___" >/etc/minirc.dfl
# Machine-generated file - use "minicom -s" to change parameters.
pu port             /dev/ttyS0
pu minit            
pu mreset           
pu mhangup          
pu statusline       enabled
pu rtscts           No 
pu xonxoff          No 
___FILE1___

chmod 0644 /etc/minirc.dfl
/sbin/restorecon /etc/minirc.dfl

