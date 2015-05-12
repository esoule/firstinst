
Source101:      firstinst-es-collection.macros

%include %{SOURCE101}

Name:           firstinst-gpk-update-icon-off
Version:        1.4
Release:        4%{?dist}

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source200:      gpk-update-icon-off.sh

Summary:        scripts that remove software update icon in GNOME %firstinst_summary_suffix

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
Scripts that remove software update icon in GNOME, for
all GNOME users, during first boot of the installed system.

%firstinst_this_package_contains_text

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}

%_fi_inst_dir     firstinst-early-02
%_fi_inst_file    firstinst-early-02        560    gpk-update-icon-off.sh

%files
%defattr(-,root,root,-)
%_fi_file_entry   firstinst-early-02        560    gpk-update-icon-off.sh

%changelog
* Mon May 11 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.4-4
- do not remove gpk-update-icon.desktop, add
  X-GNOME-Autostart-enabled=false instead

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
