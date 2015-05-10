
Source101:      firstinst-es-collection.macros

%include %{SOURCE101}

Name:           firstinst-firewall-config
Version:        1.3
Release:        4%{?dist}

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source200:      firewall-config.sh

Source4501:     system-config-firewall.txt
Source4502:     iptables-local-ipv4-filter-forward.txt
Source4503:     iptables-local-ipv4-filter-nfs.txt
Source4504:     iptables-local-ipv4-filter-ntp.txt
Source4505:     ip6tables-config.txt
Source4506:     ip6tables.txt
Source4507:     iptables-config.txt
Source4508:     iptables.txt

Summary:        scripts that apply predefined firewall configuration %firstinst_summary_suffix

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
Scripts that apply predefined firewall configuration (allow
NFS server, IPv4 forwarding, synergy, iperf server) during
first boot of the installed system.

%firstinst_this_package_contains_text

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}

%_fi_inst_dir     firstinst-early-02
%_fi_inst_file    firstinst-early-02        250    firewall-config.sh

install -dm 0755 ${RPM_BUILD_ROOT}%{firstinsthome}/firewall-config
install -pm 0600 %{SOURCE4501} ${RPM_BUILD_ROOT}%{firstinsthome}/firewall-config
install -pm 0600 %{SOURCE4502} ${RPM_BUILD_ROOT}%{firstinsthome}/firewall-config
install -pm 0600 %{SOURCE4503} ${RPM_BUILD_ROOT}%{firstinsthome}/firewall-config
install -pm 0600 %{SOURCE4504} ${RPM_BUILD_ROOT}%{firstinsthome}/firewall-config
install -pm 0600 %{SOURCE4505} ${RPM_BUILD_ROOT}%{firstinsthome}/firewall-config
install -pm 0600 %{SOURCE4506} ${RPM_BUILD_ROOT}%{firstinsthome}/firewall-config
install -pm 0600 %{SOURCE4507} ${RPM_BUILD_ROOT}%{firstinsthome}/firewall-config
install -pm 0600 %{SOURCE4508} ${RPM_BUILD_ROOT}%{firstinsthome}/firewall-config

%files
%defattr(-,root,root,-)
%_fi_file_entry   firstinst-early-02        250    firewall-config.sh
%defattr(0600,root,root,-)
%{firstinsthome}/firewall-config/*.txt

%changelog
* Sun May 10 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.3-4
- split packages into separate spec files

* Sat May  9 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.2-3
- move all items to /usr/lib/firstinst, and scripts
  to /usr/libexec/firstinst

* Thu May  7 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.1-2
- do not initialize etckeeper in /etc if initialized during
  live image generation
- make second etckeeper commit only if git repository was
  initialized

* Thu May  7 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-2
- Provide better package descriptions

* Tue May  5 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package
