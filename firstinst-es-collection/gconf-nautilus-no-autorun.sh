#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

xmlfile=`mktemp /tmp/nautilus-no-autorun.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/apps/nautilus/preferences">
    <entry>
      <key>media_automount</key>
      <schema_key>/schemas/apps/nautilus/preferences/media_automount</schema_key>
      <value>
        <bool>false</bool>
      </value>
    </entry>
    <entry>
      <key>media_automount_open</key>
      <schema_key>/schemas/apps/nautilus/preferences/media_automount_open</schema_key>
      <value>
        <bool>false</bool>
      </value>
    </entry>
    <entry>
      <key>media_autorun_never</key>
      <schema_key>/schemas/apps/nautilus/preferences/media_autorun_never</schema_key>
      <value>
        <bool>true</bool>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}
