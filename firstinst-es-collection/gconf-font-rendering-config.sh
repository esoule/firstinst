#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## enable subpixel rendering, full hinting
## WARNING: cannot set 96 DPI, because this
## makes gnome-appearance-properties crash with BadAlloc X error
##

xmlfile=`mktemp /tmp/gnome-font_rendering.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/desktop/gnome/font_rendering">
    <entry>
      <key>antialiasing</key>
      <schema_key>/schemas/desktop/gnome/font_rendering/antialiasing</schema_key>
      <value>
        <string>rgba</string>
      </value>
    </entry>
    <entry>
      <key>hinting</key>
      <schema_key>/schemas/desktop/gnome/font_rendering/hinting</schema_key>
      <value>
        <string>full</string>
      </value>
    </entry>
    <entry>
      <key>rgba_order</key>
      <schema_key>/schemas/desktop/gnome/font_rendering/rgba_order</schema_key>
      <value>
        <string>rgb</string>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

