#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## Remove all firstinst services
##
SERVICE_NAMES='firstinst-early-02 firstinst-late-96 firstinst-late-98 firstinst-late-99'

for svc_name in ${SERVICE_NAMES} ; do
    /sbin/chkconfig ${svc_name} off
    /sbin/chkconfig --del ${svc_name}
done
