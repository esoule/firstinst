#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

xmlfile=`mktemp /tmp/apps-gnome-terminal-default-profile-preferences.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/apps/gnome-terminal/profiles/Default">
    <entry>
      <key>default_size_columns</key>
      <schema_key>/schemas/apps/gnome-terminal/profiles/Default/default_size_columns</schema_key>
      <value>
        <int>80</int>
      </value>
    </entry>
    <entry>
      <key>default_size_rows</key>
      <schema_key>/schemas/apps/gnome-terminal/profiles/Default/default_size_rows</schema_key>
      <value>
        <int>40</int>
      </value>
    </entry>
    <entry>
      <key>scrollback_lines</key>
      <schema_key>/schemas/apps/gnome-terminal/profiles/Default/scrollback_lines</schema_key>
      <value>
        <int>5000</int>
      </value>
    </entry>
    <entry>
      <key>use_custom_default_size</key>
      <schema_key>/schemas/apps/gnome-terminal/profiles/Default/use_custom_default_size</schema_key>
      <value>
        <bool>true</bool>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

