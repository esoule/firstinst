
Source101:      firstinst-es-collection.macros

%include %{SOURCE101}

%define         debug_package           %{nil}

Name:           firstinst-anaconda-liveinst-utc-timezone
Version:        1.0
Release:        1%{?dist}
Summary:        use Etc/UTC as default time zone in live install %firstinst_summary_suffix

Group:          System Environment/Base
License:        GPLv2
URL:            https://github.com/esoule
Source200:      anaconda-liveinst-utc-timezone.sh
Source210:      anaconda-liveinst-utc-timezone.patch

Requires:       bash
Requires:       patch

BuildArch:      noarch

%description
Scripts that make Etc/UTC as default time zone in CentOS LiveDVD Install
to Hard Drive installer.

%firstinst_this_package_contains_text

%prep
%setup -q -c -T


%build
true


%install
rm -rf %{buildroot}
%_fi_inst_dir     firstinst-late-96
%_fi_inst_file    firstinst-late-96         310    anaconda-liveinst-utc-timezone.sh
install -dm 0755 ${RPM_BUILD_ROOT}%{firstinsthome}/anaconda-liveinst-utc-timezone
install -pm 0644 %{SOURCE210} ${RPM_BUILD_ROOT}%{firstinsthome}/anaconda-liveinst-utc-timezone/anaconda-liveinst-utc-timezone.patch


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%_fi_file_entry   firstinst-late-96         310    anaconda-liveinst-utc-timezone.sh
%dir %{firstinsthome}/anaconda-liveinst-utc-timezone
%{firstinsthome}/anaconda-liveinst-utc-timezone/anaconda-liveinst-utc-timezone.patch


%changelog
* Sat Dec 24 2016 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package
