
%define _fi_confdir %{_sysconfdir}/firstinst

Name:           livesys-service
Version:        1.0
Release:        1%{?dist}
Summary:        LiveCD service scripts

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source11:       livesys
Source12:       livesys-late

Source100:      COPYING
Source101:      README.md

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       bash, chkconfig, coreutils, initscripts

%description
LiveCD service scripts (extracted from kickstart files)

%prep
%setup -q  -c -T

install -pm 0644 %{SOURCE11} .
install -pm 0644 %{SOURCE12} .

install -pm 0644 %{SOURCE100} .
install -pm 0644 %{SOURCE101} .

%build

%install
rm -rf ${RPM_BUILD_ROOT}

install -dm 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}
install -dm 0755 ${RPM_BUILD_ROOT}/etc/rc.d/init.d

for service_name in livesys livesys-late ; do
    install -pm 0755 ${service_name}    ${RPM_BUILD_ROOT}/etc/rc.d/init.d/${service_name}
done

%clean
rm -rf $RPM_BUILD_ROOT

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

%changelog
* Wed May  6 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package
