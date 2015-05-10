
Source101:      firstinst-es-collection.macros

%include %{SOURCE101}

Name:           firstinst-gconf-clock-panel-applet-location-Montreal
Version:        1.0
Release:        1%{?dist}

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Requires:       firstinst-gconf-custom

Source200:      gconf-clock-panel-applet-location-Montreal.sh

Summary:        scripts that set default clock panel applet preferences %firstinst_summary_suffix

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
Scripts that set default clock panel applet preferences
(sets location to Montreal), during first boot of the
installed system.

%firstinst_this_package_contains_text

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}

%_fi_inst_dir     firstinst-early-02
%_fi_inst_file    firstinst-early-02        530    gconf-clock-panel-applet-location-Montreal.sh

%files
%defattr(-,root,root,-)
%_fi_file_entry   firstinst-early-02        530    gconf-clock-panel-applet-location-Montreal.sh

%changelog
* Sun May 10 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package
