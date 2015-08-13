
Source101:      firstinst-es-collection.macros

%include %{SOURCE101}

Name:           firstinst-developers-developers
Version:        1.4
Release:        4%{?dist}

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source200:      developers-developers.sh

Summary:        scripts that create developers group %firstinst_summary_suffix

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
Scripts that create developers group.

See also: package os-tweaks-sudo-developers grants the
developers group to run certain things (iotop, networking)
as root.

%firstinst_this_package_contains_text

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}

%_fi_inst_dir     firstinst-early-02
%_fi_inst_file    firstinst-early-02        420    developers-developers.sh

%files
%defattr(-,root,root,-)
%_fi_file_entry   firstinst-early-02        420    developers-developers.sh

%changelog
* Wed Aug 12 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.4-4
- move LiveCD user adjustments to livesys-service package

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
