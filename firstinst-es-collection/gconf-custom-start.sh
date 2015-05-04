#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## Store GConf-based admin customizations, part 1
## See https://docs.oracle.com/cd/E36784_01/html/E36853/glmrh.html
## "Customizing GConf Based Optimizations"
##
install -d -m 0755 /etc/gconf/gconf.xml.admin.defaults

