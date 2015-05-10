#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

xmlfile=`mktemp /tmp/apps-panel-applets-clock-prefs.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/apps/panel/applets/clock/prefs">
    <entry>
      <key>format</key>
      <schema_key>/schemas/apps/clock_applet/prefs/format</schema_key>
      <value>
        <string>24-hour</string>
      </value>
    </entry>
    <entry>
      <key>show_date</key>
      <schema_key>/schemas/apps/clock_applet/prefs/show_date</schema_key>
      <value>
        <bool>true</bool>
      </value>
    </entry>
    <entry>
      <key>show_seconds</key>
      <schema_key>/schemas/apps/clock_applet/prefs/show_seconds</schema_key>
      <value>
        <bool>true</bool>
      </value>
    </entry>
    <entry>
      <key>show_temperature</key>
      <schema_key>/schemas/apps/clock_applet/prefs/show_temperature</schema_key>
      <value>
        <bool>false</bool>
      </value>
    </entry>
    <entry>
      <key>show_weather</key>
      <schema_key>/schemas/apps/clock_applet/prefs/show_weather</schema_key>
      <value>
        <bool>false</bool>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

