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
      <key>cities</key>
      <schema_key>/schemas/apps/clock_applet/prefs/cities</schema_key>
      <value>
        <list type="string">
            <value>
              <string>&lt;location name=&quot;&quot; city=&quot;Montreal&quot; timezone=&quot;America/Toronto&quot; latitude=&quot;45.466667&quot; longitude=&quot;-73.750000&quot; code=&quot;CYUL&quot; current=&quot;true&quot;/&gt;</string>
            </value>
        </list>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

