
Source101:      firstinst-es-collection.macros

%include %{SOURCE101}

Name:           firstinst-etckeeper-commit
Version:        1.4
Release:        5%{?dist}

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source200:      etckeeper-commit-early.sh
Source201:      etckeeper-commit-late.sh
Source202:      etckeeper-commit-wrap-up.sh

Summary:        scripts that record changes in /etc with etckeeper %firstinst_summary_suffix

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
Scripts that record changes in /etc with etckeeper during
first boot of the installed system.

%firstinst_this_package_contains_text

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}

%_fi_inst_dir     firstinst-early-02
%_fi_inst_dir     firstinst-late-96
%_fi_inst_dir     firstinst-late-99
%_fi_inst_file    firstinst-early-02        050    etckeeper-commit-early.sh
%_fi_inst_file    firstinst-late-96         940    etckeeper-commit-late.sh
%_fi_inst_file    firstinst-late-99         950    etckeeper-commit-wrap-up.sh

%files
%defattr(-,root,root,-)
%_fi_file_entry   firstinst-early-02        050    etckeeper-commit-early.sh
%_fi_file_entry   firstinst-late-96         940    etckeeper-commit-late.sh
%_fi_file_entry   firstinst-late-99         950    etckeeper-commit-wrap-up.sh

%changelog
* Sun May 10 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.4-5
- perform an additional commit before firstboot is run

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
