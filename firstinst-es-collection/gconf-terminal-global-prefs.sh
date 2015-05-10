#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

xmlfile=`mktemp /tmp/apps-gnome-terminal-global-preferences.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/apps/gnome-terminal/global">
    <entry>
      <key>use_menu_accelerators</key>
      <schema_key>/schemas/apps/gnome-terminal/global/use_menu_accelerators</schema_key>
      <value>
        <bool>false</bool>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

