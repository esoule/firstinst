#!/bin/bash
source /etc/firstinst/firstinst-functions

##
## do not show all valid user accounts in gnome login
## workaround for rhbz #666220
## (see http://blog.toracat.org/2011/01/gnome-login-shows-all-valid-user-accounts-disable-it/ )
##

xmlfile=`mktemp /tmp/apps-gdm.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/apps/gdm/simple-greeter">
    <entry>
      <key>disable_user_list</key>
      <schema_key>/schemas/apps/gdm/simple-greeter/disable_user_list</schema_key>
      <value>
        <bool>true</bool>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

