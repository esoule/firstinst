#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

####
#### create tempuser1 as user whose ID is
#### between 10000 and 19999 and lock it
####

if is_liveimg_run ; then
    exit 0
fi

user_id=
group_id=
extra_groups=

do_add_user()
{

group_exists=
user_exists=

if { /usr/bin/getent group $user_name >/dev/null ; } ; then
    group_exists=1
fi

if { /usr/bin/getent group $group_id >/dev/null ; } ; then
    group_exists=1
fi

if { /usr/bin/getent passwd $user_name >/dev/null ; } ; then
    user_exists=1
fi

if { /usr/bin/getent passwd $user_id >/dev/null ; } ; then
    user_exists=1
fi

if [ -z "$group_exists" -a -z "$user_exists" ] ; then
    /usr/sbin/groupadd --gid $group_id $user_name

    /usr/sbin/useradd --comment "$comment" --gid $user_name       \
            --groups ${extra_groups}                              \
            --shell ${login_shell} --uid $user_id  $user_name

    user_added=1

    /usr/bin/passwd ${passwd_options} $user_name        >/dev/null

fi
return 0
}

user_name=tempuser1
comment='Temp User 1'
extra_groups=users
login_shell=/sbin/nologin
passwd_options='-l'

for n in `seq 1 20` ; do
    nsecs=$( /bin/date '+%N' )
    user_id=$( echo "( ( $nsecs % 10000 ) + 10000 )" | /usr/bin/bc )
    group_id=$user_id
    if [ -z "$user_id" ] ; then
        continue
    fi

    user_added=

    do_add_user
    if [ -n "${user_added}" ] ; then
        break
    fi

done
