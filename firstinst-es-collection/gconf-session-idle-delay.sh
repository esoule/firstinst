#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## Regard the computer as idle after 1 hour
##

xmlfile=`mktemp /tmp/gnome-session-idle_delay.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/desktop/gnome/session">
    <entry>
      <key>idle_delay</key>
      <schema_key>/schemas/desktop/gnome/session/idle_delay</schema_key>
      <value>
        <int>60</int>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

