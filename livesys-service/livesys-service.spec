
Source101:      firstinst-es-collection.macros

%include %{SOURCE101}

Name:           livesys-service
Version:        1.7
Release:        4%{?dist}
Summary:        LiveCD service scripts (for LiveCD runs only)

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source1:        COPYING
Source2:        README.md

Source201:      livesys-el6
Source202:      livesys-late-el6
Source203:      livesys-el7
Source204:      livesys-late-el7

Source301:      live-add-launchers-el6.sh
Source302:      live-add-launchers-el7.sh

Source401:      developers-live.sh

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       bash, chkconfig, coreutils, initscripts

%if 0%{?rhel} >= 6
%global _build_variant el%{?rhel}
%endif

%description
LiveCD service scripts (extracted from kickstart files)

This package contains the scripts that are run during the
LiveCD runs of CentOS. These files are of little use
on an installed system.

%prep
%setup -q  -c -T

install -pm 0644 %{SOURCE1} .
install -pm 0644 %{SOURCE2} .

%build

%install
rm -rf %{buildroot}

install -dm 0755 %{buildroot}%{_sysconfdir}
install -dm 0755 %{buildroot}/etc/rc.d/init.d

for service_name in livesys livesys-late ; do
    install -pm 0755 %{_sourcedir}/${service_name}-%{_build_variant}    %{buildroot}/etc/rc.d/init.d/${service_name}
done

%_fi_inst_dir                 firstinst-early-00-live
%_fi_inst_file_from           firstinst-early-00-live   100    live-add-launchers.sh    live-add-launchers-%{_build_variant}.sh
%_fi_inst_dir                 firstinst-early-02
%_fi_inst_file                firstinst-early-02        430    developers-live.sh

%clean
rm -rf %{buildroot}

%post

/sbin/chkconfig --add livesys
/sbin/chkconfig --add livesys-late

%preun

/sbin/chkconfig --del livesys || :
/sbin/chkconfig --del livesys-late || :

%files
%defattr(-,root,root,-)
%doc COPYING README.md
/etc/rc.d/init.d
%_fi_file_entry               firstinst-early-00-live   100    live-add-launchers.sh
%_fi_file_entry               firstinst-early-02        430    developers-live.sh

%changelog
* Wed Aug 12 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.7-4
- add preliminary EL7 support

* Wed Aug 12 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.6-3
- rename LiveCD username to match CentOS 7

* Wed Aug 12 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.5-3
- move LiveCD user adjustments from firstinst-developers-developers
- improve desktop launchers install script

* Sat May 16 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.4-3
- change hostname and create LiveCD user before running
  firstinst-early-00-live.d scripts
- add launchers to LiveCD user desktop

* Wed May 13 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.2-3
- run scripts from firstinst-early-00-live.d and
  firstinst-late-97-live.d subdirectories

* Mon May 11 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.1-3
- remove livesys services after they have been executed
- run liveinst using sudo, when clicking on desktop icon

* Sat May  9 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-3
- Remove cruft from spec file

* Thu May  7 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-2
- Provide better package descriptions

* Wed May  6 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package
