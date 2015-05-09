#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## Store GConf-based admin customizations, part 2
##
/bin/chmod -R u=rwX,g=rX,o=rX /etc/gconf/gconf.xml.admin.defaults
echo 'xml:readonly:/etc/gconf/gconf.xml.admin.defaults' >/etc/gconf/2/local-defaults.path
/sbin/restorecon /etc/gconf/2/local-defaults.path
/sbin/restorecon -r /etc/gconf/gconf.xml.admin.defaults

