#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

xmlfile=`mktemp /tmp/apps-nautilus-preferences.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/apps/nautilus/preferences">
    <entry>
      <key>date_format</key>
      <schema_key>/schemas/apps/nautilus/preferences/date_format</schema_key>
      <value>
        <string>iso</string>
      </value>
    </entry>
    <entry>
      <key>default_folder_viewer</key>
      <schema_key>/schemas/apps/nautilus/preferences/default_folder_viewer</schema_key>
      <value>
        <string>list_view</string>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

