
Source101:      firstinst-es-collection.macros

%include %{SOURCE101}

Name:           firstinst-adduser-tempuser1
Version:        1.0
Release:        1%{?dist}

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source200:      adduser-tempuser1.sh

Summary:        scripts that create tempuser1 user %firstinst_summary_suffix

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
Scripts that that add locked down tempuser1 user at
user ID and group ID above 10000.

%firstinst_this_package_contains_text

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}

%_fi_inst_dir     firstinst-late-96
%_fi_inst_file    firstinst-late-96         850    adduser-tempuser1.sh

%files
%defattr(-,root,root,-)
%_fi_file_entry   firstinst-late-96         850    adduser-tempuser1.sh

%changelog
* Sat May 16 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package
