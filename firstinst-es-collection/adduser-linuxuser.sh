#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

####
#### create linuxuser user as uid 500 / gid 500
#### and allow the user to access serial ports
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

user_name=linuxuser
comment='Linux User'
extra_groups=dialout,users,uucp
login_shell=/bin/bash
passwd_options='-d'

for n in `seq 500 539` ; do
    user_id=$n
    group_id=$n

    user_added=

    do_add_user
    if [ -n "${user_added}" ] ; then
        break
    fi

done
