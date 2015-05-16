#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

####
#### create linuxuser user as uid 1001 / gid 1001
#### and allow the user to access serial ports
####

if is_liveimg_run ; then
    exit 0
fi

name=linuxuser
comment='Linux User'

uid=1001
gid=1001

group_exists=
user_exists=

if { /usr/bin/getent group $name >/dev/null ; } ; then
    group_exists=1
fi

if { /usr/bin/getent group $gid >/dev/null ; } ; then
    group_exists=1
fi

if { /usr/bin/getent passwd $name >/dev/null ; } ; then
    user_exists=1
fi

if { /usr/bin/getent passwd $uid >/dev/null ; } ; then
    user_exists=1
fi

if [ -z "$group_exists" -a -z "$user_exists" ] ; then
    /usr/sbin/groupadd --gid $gid $name

    /usr/sbin/useradd --comment "$comment" --gid $name            \
            --groups dialout,users,uucp                           \
            --shell /bin/bash --uid $uid  $name

    /usr/bin/passwd -d $name        >/dev/null

fi
