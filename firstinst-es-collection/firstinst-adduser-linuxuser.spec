
Source101:      firstinst-es-collection.macros

%include %{SOURCE101}

Name:           firstinst-adduser-linuxuser
Version:        1.0
Release:        1%{?dist}

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source200:      adduser-linuxuser.sh

Summary:        scripts that add linuxuser user %firstinst_summary_suffix

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
Scripts that that add linuxuser user at User ID 1001
and group ID 1001.

%firstinst_this_package_contains_text

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}

%_fi_inst_dir     firstinst-early-02
%_fi_inst_file    firstinst-early-02        710    adduser-linuxuser.sh

%files
%defattr(-,root,root,-)
%_fi_file_entry   firstinst-early-02        710    adduser-linuxuser.sh

%changelog
* Sat May 16 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package
