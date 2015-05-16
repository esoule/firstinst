#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

launchers='vinagre.desktop gnome-nautilus.desktop gnome-terminal.desktop gedit.desktop'

( cd /usr/share/applications/ && /usr/bin/install -m 0755 $launchers /home/centoslive/Desktop/ )

