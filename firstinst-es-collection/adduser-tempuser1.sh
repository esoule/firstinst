#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

####
#### create tempuser1 as user whose ID is between 10000 and 19999
#### and lock it
####

if is_liveimg_run ; then
    exit 0
fi

name=tempuser1
comment='Temp User 1'

nsecs=$( /bin/date '+%N' )
uid=$( echo "( ( $nsecs % 10000 ) + 10000 )" | /usr/bin/bc )
gid=$uid

if [ -z "$uid" ] ; then
    exit 0
fi

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
            --groups users                                        \
            --shell /sbin/nologin --uid $uid  $name

    /usr/bin/passwd -l $name        >/dev/null

fi

