#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

anaconda_liveinst_utc_timezone_main()
{
	local patch_file=/usr/lib/firstinst/anaconda-liveinst-utc-timezone/anaconda-liveinst-utc-timezone.patch

	if ! is_liveimg_run ; then
		return 0
	fi

	cd /usr/lib/anaconda

	if ! /usr/bin/patch --dry-run -N -p1 --fuzz=0 -i ${patch_file} ; then
		return 0
	fi

	if /usr/bin/patch -b -z .001.orig -N -p1 --fuzz=0 -i ${patch_file} ; then
		mv iw/timezone_gui.pyc iw/timezone_gui.pyc.orig
		mv iw/timezone_gui.pyo iw/timezone_gui.pyo.orig
	fi

	return 0
}

( anaconda_liveinst_utc_timezone_main ; )
unset anaconda_liveinst_utc_timezone_main
