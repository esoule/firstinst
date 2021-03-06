#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

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

exit 0
