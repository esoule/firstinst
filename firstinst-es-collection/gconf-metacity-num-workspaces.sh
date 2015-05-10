#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

##
## Set the default number of workspaces to 4
##

xmlfile=`mktemp /tmp/apps-metacity-general-num_workspaces.XXXXXXXXXX.xml`

if [ -z "${xmlfile}" ] ; then
    exit 1
fi

cat <<"___XMLFILE___" >${xmlfile}
<gconfentryfile>
  <entrylist base="/apps/metacity/general">
    <entry>
      <key>num_workspaces</key>
      <schema_key>/schemas/apps/metacity/general/num_workspaces</schema_key>
      <value>
        <int>4</int>
      </value>
    </entry>
  </entrylist>
</gconfentryfile>

___XMLFILE___

gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.admin.defaults --load ${xmlfile}
rm -f ${xmlfile}

