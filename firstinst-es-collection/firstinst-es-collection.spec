
%define _fi_confdir %{_sysconfdir}/firstinst
%define _fi_inst_dir()     install -dm 0755 %{buildroot}/%{_fi_confdir}/%1.d \
%{nil}
%define _fi_inst_file()    install -pm 0644 %{_sourcedir}/%3 ${RPM_BUILD_ROOT}%{_fi_confdir}/%1.d/%2-%3 \
%{nil}

%define _this_package_contains_text This package is part of First Install Scripts collection.\
This package contains the scripts that were run during the\
installation of your system. These files are of little use\
on an already installed system.\
%{nil}

Name:           firstinst-es-collection
Version:        1.0
Release:        2%{?dist}
Summary:        collection of first install tasks

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/esoule

Source400:      NetworkManager-sysctl-fixup.sh
Source410:      avahi-daemon-off.sh
Source420:      developers-developers.sh
Source430:      etckeeper-commit-early.sh
Source440:      etckeeper-commit-late.sh
Source450:      firewall-config.sh
Source460:      firstinst-services-off.sh
Source470:      fstab-noatime.sh
Source480:      gconf-custom-finish.sh
Source490:      gconf-custom-start.sh
Source500:      gconf-font-rendering-config.sh
Source510:      gconf-gpk-update-icon-off.sh
Source520:      gconf-login-user-list-off.sh
Source530:      gconf-screensaver-lock-off.sh
Source540:      gdm-config.sh
Source550:      git-lola-config.sh
Source560:      gpk-update-icon-off.sh
Source570:      grub-config.sh
Source580:      inputrc-config.sh
Source590:      minicom-ttyS0-config.sh
Source600:      nfs-config.sh
Source610:      nginx-off.sh
Source620:      prelink-off.sh
Source630:      root-gitconfig.sh
Source640:      sshd-config.sh
Source650:      tftp-config.sh
Source660:      vsftpd-config.sh
Source670:      yum-config.sh
Source680:      yum-epel-repo-config.sh
Source690:      yum-rpmforge-repo-config.sh

Source4501:     system-config-firewall.txt
Source4502:     iptables-local-ipv4-filter-forward.txt
Source4503:     iptables-local-ipv4-filter-nfs.txt
Source4504:     iptables-local-ipv4-filter-ntp.txt
Source4505:     ip6tables-config.txt
Source4506:     ip6tables.txt
Source4507:     iptables-config.txt
Source4508:     iptables.txt


BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  tree

%description
collection of first install tasks

%prep
%setup -q  -c -T

%build

%install
rm -rf ${RPM_BUILD_ROOT}

%_fi_inst_dir     firstinst-early-02
%_fi_inst_dir     firstinst-late-96
%_fi_inst_dir     firstinst-late-99

%_fi_inst_file    firstinst-early-02        050    etckeeper-commit-early.sh
%_fi_inst_file    firstinst-early-02        200    gconf-custom-start.sh
%_fi_inst_file    firstinst-early-02        250    firewall-config.sh

%_fi_inst_file    firstinst-early-02        400    NetworkManager-sysctl-fixup.sh
%_fi_inst_file    firstinst-early-02        410    avahi-daemon-off.sh
%_fi_inst_file    firstinst-early-02        420    developers-developers.sh
%_fi_inst_file    firstinst-early-02        500    gconf-font-rendering-config.sh
%_fi_inst_file    firstinst-early-02        510    gconf-gpk-update-icon-off.sh
%_fi_inst_file    firstinst-early-02        520    gconf-login-user-list-off.sh
%_fi_inst_file    firstinst-early-02        530    gconf-screensaver-lock-off.sh
%_fi_inst_file    firstinst-early-02        540    gdm-config.sh
%_fi_inst_file    firstinst-early-02        550    git-lola-config.sh
%_fi_inst_file    firstinst-early-02        560    gpk-update-icon-off.sh
%_fi_inst_file    firstinst-early-02        570    grub-config.sh
%_fi_inst_file    firstinst-early-02        580    inputrc-config.sh
%_fi_inst_file    firstinst-early-02        590    minicom-ttyS0-config.sh
%_fi_inst_file    firstinst-early-02        600    nfs-config.sh
%_fi_inst_file    firstinst-early-02        610    nginx-off.sh
%_fi_inst_file    firstinst-early-02        620    prelink-off.sh
%_fi_inst_file    firstinst-early-02        630    root-gitconfig.sh
%_fi_inst_file    firstinst-early-02        640    sshd-config.sh
%_fi_inst_file    firstinst-early-02        650    tftp-config.sh
%_fi_inst_file    firstinst-early-02        660    vsftpd-config.sh
%_fi_inst_file    firstinst-early-02        670    yum-config.sh
%_fi_inst_file    firstinst-early-02        680    yum-epel-repo-config.sh
%_fi_inst_file    firstinst-early-02        690    yum-rpmforge-repo-config.sh

%_fi_inst_file    firstinst-early-02        800    gconf-custom-finish.sh

%_fi_inst_file    firstinst-late-96         470    fstab-noatime.sh

%_fi_inst_file    firstinst-late-99         900    firstinst-services-off.sh
%_fi_inst_file    firstinst-late-99         950    etckeeper-commit-late.sh


install -dm 0755 ${RPM_BUILD_ROOT}%{_fi_confdir}/firewall-config
install -pm 0600 %{SOURCE4501} ${RPM_BUILD_ROOT}%{_fi_confdir}/firewall-config
install -pm 0600 %{SOURCE4502} ${RPM_BUILD_ROOT}%{_fi_confdir}/firewall-config
install -pm 0600 %{SOURCE4503} ${RPM_BUILD_ROOT}%{_fi_confdir}/firewall-config
install -pm 0600 %{SOURCE4504} ${RPM_BUILD_ROOT}%{_fi_confdir}/firewall-config
install -pm 0600 %{SOURCE4505} ${RPM_BUILD_ROOT}%{_fi_confdir}/firewall-config
install -pm 0600 %{SOURCE4506} ${RPM_BUILD_ROOT}%{_fi_confdir}/firewall-config
install -pm 0600 %{SOURCE4507} ${RPM_BUILD_ROOT}%{_fi_confdir}/firewall-config
install -pm 0600 %{SOURCE4508} ${RPM_BUILD_ROOT}%{_fi_confdir}/firewall-config

(cd ${RPM_BUILD_ROOT} && find etc/firstinst -type f ) | sort
/usr/bin/tree -AanFp ${RPM_BUILD_ROOT}%{_fi_confdir}


%package -n firstinst-etckeeper-commit
Summary: scripts that record changes in /etc with etckeeper (for system install only)

%description -n firstinst-etckeeper-commit
Scripts that record changes in /etc with etckeeper during
first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-etckeeper-commit
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/050-etckeeper-commit-early.sh
%{_fi_confdir}/firstinst-late-99.d/950-etckeeper-commit-late.sh



%package -n firstinst-gconf-custom
Summary: scripts that store gconf customizations (for system install only)

%description -n firstinst-gconf-custom
Scripts that store gconf customizations during first boot
of the installed system. Other firstinst-gconf-* packages
need this one to be installed to work properly.

%{_this_package_contains_text}

%files -n firstinst-gconf-custom
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/200-gconf-custom-start.sh
%{_fi_confdir}/firstinst-early-02.d/800-gconf-custom-finish.sh



%package -n firstinst-firewall-config
Summary: scripts that apply predefined firewall configuration (for system install only)

%description -n firstinst-firewall-config
Scripts that apply predefined firewall configuration (allow
NFS server, IPv4 forwarding, synergy, iperf server) during
first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-firewall-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/250-firewall-config.sh
%defattr(0600,root,root,-)
%{_fi_confdir}/firewall-config/*.txt



%package -n firstinst-fstab-noatime
Summary: scripts that enable noatime option in fstab (for system install only)

%description -n firstinst-fstab-noatime
Scripts that enable noatime option in fstab for ext2, ext3
and ext4 file systems.

Changes are set during first boot of the installed system
and take effect at the second boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-fstab-noatime
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-late-96.d/470-fstab-noatime.sh



%package -n firstinst-firstinst-services-off
Summary: scripts that disable firstinst services (for system install only)

%description -n firstinst-firstinst-services-off
Scripts that disable firstinst services at the end of first
boot of the installed system, so that they do not run again.

%{_this_package_contains_text}

%files -n firstinst-firstinst-services-off
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-late-99.d/900-firstinst-services-off.sh



%package -n firstinst-NetworkManager-sysctl-fixup
Summary: scripts that fix NetworkManager's sysctl processing (for system install only)

%description -n firstinst-NetworkManager-sysctl-fixup
Scripts that fix NetworkManager's sysctl processing
(workaround for rhbz #1213118), during first boot of the
installed system.

%{_this_package_contains_text}

%files -n firstinst-NetworkManager-sysctl-fixup
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/400-NetworkManager-sysctl-fixup.sh



%package -n firstinst-avahi-daemon-off
Summary: scripts that disable avahi-daemon (for system install only)

%description -n firstinst-avahi-daemon-off
Scripts that disable avahi-daemon, during first boot of the
installed system.

%{_this_package_contains_text}

%files -n firstinst-avahi-daemon-off
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/410-avahi-daemon-off.sh



%package -n firstinst-developers-developers
Summary: scripts that create developers group (for system install only)

%description -n firstinst-developers-developers
Scripts that create developers group. On LiveCD, these
scripts also add the centoslive user to developers, uucp,
dialout and wireshark group.

See also: package os-tweaks-sudo-developers grants the
developers group to run certain things (iotop, networking)
as root.

%{_this_package_contains_text}

%files -n firstinst-developers-developers
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/420-developers-developers.sh



%package -n firstinst-gconf-font-rendering-config
Summary: scripts that enable font hinting, subpixel rendering (for system install only)
Requires: firstinst-gconf-custom

%description -n firstinst-gconf-font-rendering-config
Scripts that enable font hinting, subpixel rendering, for
all GNOME users, during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-gconf-font-rendering-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/500-gconf-font-rendering-config.sh



%package -n firstinst-gconf-gpk-update-icon-off
Summary: scripts that remove software update icon in GNOME (for system install only)
Requires: firstinst-gconf-custom

%description -n firstinst-gconf-gpk-update-icon-off
Scripts that remove software update icon in GNOME, for
all GNOME users, during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-gconf-gpk-update-icon-off
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/510-gconf-gpk-update-icon-off.sh



%package -n firstinst-gconf-login-user-list-off
Summary: scripts that remove the user list from GNOME login screen (for system install only)
Requires: firstinst-gconf-custom

%description -n firstinst-gconf-login-user-list-off
Scripts that remove the user list from GNOME login screen,
during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-gconf-login-user-list-off
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/520-gconf-login-user-list-off.sh



%package -n firstinst-gconf-screensaver-lock-off
Summary: scripts that disable screensaver password in GNOME (for system install only)
Requires: firstinst-gconf-custom

%description -n firstinst-gconf-screensaver-lock-off
Scripts that disable screensaver password in GNOME,
during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-gconf-screensaver-lock-off
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/530-gconf-screensaver-lock-off.sh



%package -n firstinst-gdm-config
Summary: scripts that disallow root login in GNOME (for system install only)

%description -n firstinst-gdm-config
Scripts that disallow root login in GNOME,
during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-gdm-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/540-gdm-config.sh



%package -n firstinst-git-lola-config
Summary: scripts that enable colours and aliases in git (for system install only)

%description -n firstinst-git-lola-config
Scripts that enable colours and aliases in git,
system-wide, during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-git-lola-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/550-git-lola-config.sh



%package -n firstinst-gpk-update-icon-off
Summary: scripts that remove software update icon in GNOME (for system install only)

%description -n firstinst-gpk-update-icon-off
Scripts that remove software update icon in GNOME, for
all GNOME users, during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-gpk-update-icon-off
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/560-gpk-update-icon-off.sh



%package -n firstinst-grub-config
Summary: scripts that change bootloader config (for system install only)

%description -n firstinst-grub-config
Scripts that change bootloader configuration (show menu,
increase timeout, disable graphical boot, set vga=791).
Changes are set during first boot of the installed system
and take effect at the second boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-grub-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/570-grub-config.sh



%package -n firstinst-inputrc-config
Summary: scripts that disable beep on CLI (for system install only)

%description -n firstinst-inputrc-config
Scripts that disable beep on CLI, add some PuTTY input key
mappings, during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-inputrc-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/580-inputrc-config.sh



%package -n firstinst-minicom-ttyS0-config
Summary: scripts that provide default minicom config (for system install only)

%description -n firstinst-minicom-ttyS0-config
Scripts that provide default minicom config, during first
boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-minicom-ttyS0-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/590-minicom-ttyS0-config.sh



%package -n firstinst-nfs-config
Summary: scripts that make NFS friendly to firewalls (for system install only)

%description -n firstinst-nfs-config
Scripts that edit NFS server configs to make them friendly
to firewalls, during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-nfs-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/600-nfs-config.sh



%package -n firstinst-nginx-off
Summary: scripts that disable nginx service (for system install only)

%description -n firstinst-nginx-off
Scripts that disable nginx service, during first boot of
the installed system.

%{_this_package_contains_text}

%files -n firstinst-nginx-off
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/610-nginx-off.sh



%package -n firstinst-prelink-off
Summary: scripts that provide config that disables prelink (for system install only)

%description -n firstinst-prelink-off
Scripts that provide config that disables prelink, during
first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-prelink-off
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/620-prelink-off.sh



%package -n firstinst-root-gitconfig
Summary: scripts that provide .gitconfig for root user (for system install only)

%description -n firstinst-root-gitconfig
Scripts that provide .gitconfig for root user, during
first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-root-gitconfig
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/630-root-gitconfig.sh



%package -n firstinst-sshd-config
Summary: scripts that change SSH server options (for system install only)

%description -n firstinst-sshd-config
Scripts that change SSH server options (disable root login,
disable reverse DNS lookups), during first boot of the
installed system.

%{_this_package_contains_text}

%files -n firstinst-sshd-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/640-sshd-config.sh



%package -n firstinst-tftp-config
Summary: scripts that change TFTP server options (for system install only)

%description -n firstinst-tftp-config
Scripts that change TFTP server options (set root TFTP
directory to /srv/tftpboot), during first boot of the
installed system.

%{_this_package_contains_text}

%files -n firstinst-tftp-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/650-tftp-config.sh



%package -n firstinst-vsftpd-config
Summary: scripts that change vsFTPd server options (for system install only)

%description -n firstinst-vsftpd-config
Scripts that change vsFTPd server options (disable reverse
DNS lookups, use local time in file listings), during first
boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-vsftpd-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/660-vsftpd-config.sh



%package -n firstinst-yum-config
Summary: scripts that change yum configuration (for system install only)

%description -n firstinst-yum-config
Scripts that change yum configuration (exclude Facebook and
University of Ottawa from mirror lists for performance
reasons), during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-yum-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/670-yum-config.sh



%package -n firstinst-yum-epel-repo-config
Summary: scripts that change EPEL repository config (for system install only)

%description -n firstinst-yum-epel-repo-config
Scripts that change EPEL repository config (exclude wine
packages), during first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-yum-epel-repo-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/680-yum-epel-repo-config.sh



%package -n firstinst-yum-rpmforge-repo-config
Summary: scripts that change rpmforge repository config (for system install only)

%description -n firstinst-yum-rpmforge-repo-config
Scripts that change rpmforge repository config (disable
the repository by default, exclude sqlite packages), during
first boot of the installed system.

%{_this_package_contains_text}

%files -n firstinst-yum-rpmforge-repo-config
%defattr(-,root,root,-)
%{_fi_confdir}/firstinst-early-02.d/690-yum-rpmforge-repo-config.sh



%changelog
* Thu May  7 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.1-2
- do not initialize etckeeper in /etc if initialized during
  live image generation
- make second etckeeper commit only if git repository was
  initialized

* Thu May  7 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-2
- Provide better package descriptions

* Tue May  5 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package

