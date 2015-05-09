#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

xmlfile=`mktemp /tmp/update-icon-frequency_get_updates.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/apps/gnome-packagekit/update-icon">
    <entry>
      <key>frequency_get_updates</key>
      <schema_key>/schemas/apps/gnome-packagekit/update-icon/frequency_get_updates</schema_key>
      <value>
        <int>0</int>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

