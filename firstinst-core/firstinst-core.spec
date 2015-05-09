
%define firstinsthome /usr/lib/firstinst
%define firstinstexec /usr/libexec/firstinst

Name:           firstinst-core
Version:        1.1
Release:        3%{?dist}
Summary:        First Install Scripts for CentOS

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source0:        firstinst-run-parts
Source1:        firstinst-functions

Source11:       firstinst-early-02
Source12:       firstinst-late-96
Source13:       firstinst-late-98
Source14:       firstinst-late-99

Source100:      COPYING
Source101:      README.md

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       bash, chkconfig, coreutils, initscripts

%description
First Install Scripts for CentOS

This project provides a framework for running a large number of small
installation scripts during first system boot as well as a collection of
such small installation scripts. Scripts are provided as rpm packages,
so that they may be referenced in package lists of OS install scripts.

%prep
%setup -q  -c -T
install -pm 0644 %{SOURCE0} .
install -pm 0644 %{SOURCE1} .

install -pm 0644 %{SOURCE11} .
install -pm 0644 %{SOURCE12} .
install -pm 0644 %{SOURCE13} .
install -pm 0644 %{SOURCE14} .

install -pm 0644 %{SOURCE100} .
install -pm 0644 %{SOURCE101} .

%build

%install
rm -rf ${RPM_BUILD_ROOT}

install -dm 0755 ${RPM_BUILD_ROOT}/etc/rc.d/init.d
install -dm 0755 ${RPM_BUILD_ROOT}%{firstinsthome}
install -dm 0755 ${RPM_BUILD_ROOT}%{firstinstexec}

install -pm 0644 firstinst-functions  ${RPM_BUILD_ROOT}%{firstinsthome}/firstinst-functions
install -pm 0755 firstinst-run-parts  ${RPM_BUILD_ROOT}%{firstinstexec}/firstinst-run-parts

for service_name in firstinst-early-00-live firstinst-late-97-live ; do
    install -dm 0755 ${RPM_BUILD_ROOT}%{firstinsthome}/${service_name}.d
done

for service_name in firstinst-early-02 firstinst-late-96 firstinst-late-98 firstinst-late-99 ; do
    install -dm 0755 ${RPM_BUILD_ROOT}%{firstinsthome}/${service_name}.d
    install -pm 0755 ${service_name}    ${RPM_BUILD_ROOT}/etc/rc.d/init.d/${service_name}
done

%clean
rm -rf $RPM_BUILD_ROOT

%post

/sbin/chkconfig --add firstinst-early-02
/sbin/chkconfig --add firstinst-late-96
/sbin/chkconfig --add firstinst-late-98
/sbin/chkconfig --add firstinst-late-99

%preun

/sbin/chkconfig --del firstinst-early-02 || :
/sbin/chkconfig --del firstinst-late-96 || :
/sbin/chkconfig --del firstinst-late-98 || :
/sbin/chkconfig --del firstinst-late-99 || :

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{firstinsthome}/firstinst-functions
%{firstinstexec}/firstinst-run-parts
%dir %{firstinsthome}/firstinst-early-00-live.d
%dir %{firstinsthome}/firstinst-early-02.d
%dir %{firstinsthome}/firstinst-late-96.d
%dir %{firstinsthome}/firstinst-late-97-live.d
%dir %{firstinsthome}/firstinst-late-98.d
%dir %{firstinsthome}/firstinst-late-99.d
/etc/rc.d/init.d/firstinst*

%changelog
* Sat May  9 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.1-3
- move all items to /usr/lib/firstinst, and scripts
  to /usr/libexec/firstinst

* Wed May  6 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-2
- add chkconfig, coreutils to Requires

* Sun May  3 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package

