#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

launchers='vinagre.desktop gnome-nautilus.desktop gnome-terminal.desktop gedit.desktop'

(
for f in ${launchers} ; do
    if [ -e /usr/share/applications/${f} ] ; then
        /usr/bin/install -m 0755 /usr/share/applications/${f} /home/liveuser/Desktop/
    fi
done
)
