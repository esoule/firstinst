#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

## /etc/xdg/autostart/gpk-update-icon.desktop
cat <<"____EOF" >>/etc/xdg/autostart/gpk-update-icon.desktop

X-GNOME-Autostart-enabled=false
____EOF

/sbin/restorecon /etc/xdg/autostart/gpk-update-icon.desktop

