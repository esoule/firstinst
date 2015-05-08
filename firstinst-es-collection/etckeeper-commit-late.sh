#!/bin/bash
source /etc/firstinst/firstinst-functions

if [ ! -x /usr/bin/etckeeper ] ; then
    exit 0
fi

if [ ! -d /etc/.git ] ; then
## NOTE: etckeeper initialization was not done
    exit 0
fi

# workaround for "fatal: $HOME is not set"
if [ -z "$HOME" ] ; then
    export HOME=/root
fi

/usr/bin/etckeeper commit "Second commit"    >/dev/null

if ! is_liveimg_run ; then
    /usr/bin/etckeeper vcs gc    >/dev/null
fi

exit 0
