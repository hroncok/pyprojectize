%bcond_with enc_x264
%bcond_with enc_x265
# Theses settings requires 64bit
%if 0%{?__isa_bits} == 64
%bcond_without dec_avcodec2
%bcond_without csc_swscale
%else
%bcond_with dec_avcodec2
%bcond_with csc_swscale
%endif

# For debugging only
%bcond_with debug
%if %{with debug}
%global _with_debug --with-debug
%endif
#

%global __js_jquery_latest %{_datadir}/javascript/jquery/latest/

# These are necessary as the _with_foo is *not* defined if the
# --with flag isn't specifed, and we need to have the --without
# specified option in that case.
%if %{without enc_x264}
%global _with_enc_x264 --without-enc_x264
%endif

%if %{with enc_x265}
%global _with_enc_x265 --with-enc_x265
%endif

%if %{without dec_avcodec2}
%global _with_dec_avcodec2 --without-dec_avcodec2
%endif

%if %{without csc_swscale}
%global _with_csc_swscale --without-csc_swscale
%endif

# Remove private provides from .so files in the python3_sitearch directory
%global __provides_exclude_from ^%{python3_sitearch}/.*\\.so$

# Note: cups-config not in buildroot during srpm build, so we use the
# conditional execution to silence erros during srpm build.
%if 0%{?_cups_serverbin:1}
%global cupslibdir %_cups_serverbin
%else
%global cupslibdir %(cups-config --serverbin 2> /dev/null || echo "/usr/lib/cups")
%endif

Name:           xpra
Version:        5.0.6
Release:        %autorelease
Summary:        Remote display server for applications and desktops
# Automatically converted from old format: GPLv2+ and BSD and LGPLv3+ and MIT - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LGPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:            https://www.xpra.org/
Source0:        https://github.com/Xpra-org/xpra/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Appdata file for Fedora
Source1:        %{name}.appdata.xml
Patch1:         ignore_assert_pandoc.patch
# Add compatibility with FFMPEG 7.0
# https://github.com/Xpra-org/xpra/pull/4216
Patch2:         0001-Add-compatibility-with-FFMPEG-7.0.patch

BuildRequires:  python3-devel
BuildRequires:  gtk3-devel
BuildRequires:  libXtst-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  lz4-devel
BuildRequires:  python3-Cython
BuildRequires:  ack
BuildRequires:  desktop-file-utils
BuildRequires:  libvpx-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXres-devel
BuildRequires:  cups-devel
BuildRequires:  python3-cups
BuildRequires:  redhat-rpm-config
BuildRequires:  python3-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  pam-devel
BuildRequires:  pandoc
# needs by setup.py to detect systemd `sd_listen_ENABLED = POSIX and pkg_config_ok("--exists", "libsystemd")`
BuildRequires:  systemd-devel
%if 0%{?fedora}
BuildRequires:  procps-ng-devel
%endif
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  libdrm-devel
BuildRequires:  pkgconfig(libwebp)
%if 0%{?el8}
#BuildRequires:  xorg-x11-server-Xvfb
#BuildRequires:  cairo-devel
BuildRequires:  pygobject3-devel
%else
BuildRequires:  python3-gobject-devel
%endif
BuildRequires:  libappstream-glib
BuildRequires:  python3-cairo-devel
BuildRequires:  xorg-x11-server-Xorg
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  xorg-x11-xauth
BuildRequires:  xkbcomp
BuildRequires:  setxkbmap
%if %{with debug}
BuildRequires: libasan
%endif

%if %{with enc_x264}
BuildRequires:  x264-devel
%endif
# While ffmpeg-devel should only be needed in theses conditions, setup.py requires it anyway
#if %%{with dec_avcodec2} || %%{with csc_swscale}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
#endif

Requires: python3-pillow
Requires: python3-cups
Requires: python3-pyopengl
Requires: python3-gobject
Requires: python3-inotify
Requires: python3-lz4
Requires: python3-ldap3
Requires: python3-rencode
Requires: python3-netifaces
Requires: python3-dbus
Requires: python3-numpy
%if 0%{?fedora}
Requires: python3-zeroconf
%endif
Requires: dbus-x11
Requires: xmodmap
Requires: xrandr
Requires: xorg-x11-drv-dummy%{?_isa}
Requires: xorg-x11-xauth%{?_isa}
Requires: xorg-x11-server-Xorg%{?_isa}
Requires: gstreamer1%{?_isa}
Requires: gstreamer1-plugins-base%{?_isa}
Requires: gstreamer1-plugins-good%{?_isa}
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires: pipewire%{?_isa}
Requires: pipewire-utils%{?_isa}
Requires: pipewire-pulseaudio%{?_isa}
%else
Requires: pulseaudio%{?_isa}
Requires: pulseaudio-utils%{?_isa}
%endif
Requires: cups-filesystem
Requires: shared-mime-info%{?_isa}
Requires: js-jquery

# python3-opencv is required for webcam forwarding support, client-side only.
# Available on Fedora only.
%{?fedora:Requires: python3-opencv}

# Needed to create the xpra group
Requires(pre):  shadow-utils

# xpra-html5 is now separately provided
Obsoletes: xpra-html5 < 0:4.1-1

Requires: systemd-udev%{?_isa}
Obsoletes: xpra-udev < %{version}-%{release}
Provides: xpra-udev = %{version}-%{release}

%description
Xpra is "screen for X": it allows you to run X programs, usually on a remote
host, direct their display to your local machine, and then to disconnect from
these programs and reconnect from the same or another machine, without losing
any state. It gives you remote access to individual applications.

Xpra is "rootless" or "seamless": programs you run under it show up on your
desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt to changing
network bandwidth constraints.

%prep
%autosetup -p1 -n %{name}-%{version}

# cc1: error: unrecognized compiler option ‘-mfpmath=387’
%ifarch %{arm}
sed -i 's|-mfpmath=387|-mfloat-abi=hard|' setup.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%set_build_flags
%py3_build -- \
    --without-nvidia --without-pandoc_lua \
    --with-verbose \
    --with-vpx \
    %{?_with_enc_x264} \
    %{?_with_enc_x265} \
    %{?_with_dec_avcodec2} \
    %{?_with_csc_swscale} \
    %{?_with_debug} \
    --with-Xdummy \
    --with-Xdummy_wrapper \
    --without-strict \
    --with-enc_ffmpeg

%install
%pyproject_install
%pyproject_save_files -l xpra

mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}/lib/systemd/system/xpra.*  %{buildroot}%{_unitdir}/

#move icon to proper directory
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps

mv %{buildroot}%{_datadir}/icons/xpra.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/

rm -f %{buildroot}%{_datadir}/icons/xpra-mdns.png
install -pm 644 fs/share/icons/xpra-mdns.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

rm -f %{buildroot}%{_datadir}/icons/xpra-shadow.png
install -pm 644 fs/share/icons/xpra-shadow.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

#replace old file with horrible WindowsXP old image
rm -rf %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/

#Install nvenc.keys file
mkdir -p %{buildroot}%{_sysconfdir}/xpra
install -pm 644 fs/etc/xpra/nvenc.keys %{buildroot}%{_sysconfdir}/xpra

#remove doc stuff from /usr/share
rm %{buildroot}%{_datadir}/xpra/COPYING

#fix shebangs from python3_sitearch
for i in `ack -rl '^#!/.*python' %{buildroot}%{python3_sitearch}/xpra`; do
    %py3_shebang_fix $i
    chmod 0755 $i
done

#fix permissions on shared objects
find %{buildroot}%{python3_sitearch}/xpra -name '*.so' \
    -exec chmod 0755 {} \;

# delete any bundled SWFs - binary content forbidden by packaging
# guidelines
find %{buildroot}%{_datadir}/xpra -name '*.swf' -exec rm {} \;

# Create this directory for sharing sockets
mkdir -p %{buildroot}%{_rundir}/xpra

# Remove use of /usr/bin/enx on scripts
%py3_shebang_fix %{buildroot}%{cupslibdir}/backend/xpraforwarder
%py3_shebang_fix %{buildroot}%{_libexecdir}/xpra/auth_dialog
%py3_shebang_fix %{buildroot}%{_libexecdir}/xpra/xdg-open

for i in `find %{buildroot}%{_bindir} -perm /644 -type f \( -name "*" \)`; do
    chmod 0755 $i
done

# Remove Build documentation
rm -rf %{buildroot}%{_docdir}/xpra/Build

install -pm 644 README.md %{buildroot}%{_docdir}/xpra/

%check
%{?fedora:appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/xpra.appdata.xml}
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%pre
getent group xpra >/dev/null || groupadd -r xpra

%files -f %{pyproject_files}
%dir %{_sysconfdir}/xpra
%dir %{_sysconfdir}/xpra/conf.d
%config(noreplace) %{_sysconfdir}/xpra/*.conf
%config(noreplace) %{_sysconfdir}/xpra/nvenc.keys
%config(noreplace) %{_sysconfdir}/xpra/conf.d/*.conf
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/90-xpra-virtual.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/xpra.conf
%config(noreplace) %{_sysconfdir}/sysconfig/xpra
%config(noreplace) %{_sysconfdir}/pam.d/xpra
%config(noreplace) %{_sysconfdir}/xpra/content-categories/10_default.conf
%config(noreplace) %{_sysconfdir}/xpra/content-parent/10_default.conf
%config(noreplace) %{_sysconfdir}/xpra/content-type/10_role.conf
%config(noreplace) %{_sysconfdir}/xpra/content-type/30_title.conf
%config(noreplace) %{_sysconfdir}/xpra/content-type/50_class.conf
%config(noreplace) %{_sysconfdir}/xpra/content-type/70_commands.conf
%config(noreplace) %{_sysconfdir}/xpra/http-headers/00_nocache.txt
%config(noreplace) %{_sysconfdir}/xpra/http-headers/10_content_security_policy.txt
%{_libexecdir}/xpra/
%{_bindir}/xpra
%{_bindir}/xpra_launcher
%{_bindir}/run_scaled
%{_sysusersdir}/*.conf
%{_datadir}/applications/xpra*.desktop
%{_datadir}/icons/hicolor/48x48/apps/xpra-mdns.png
%{_datadir}/icons/hicolor/48x48/apps/xpra-shadow.png
%{_datadir}/icons/hicolor/64x64/apps/xpra.png
%{_mandir}/man1/xpra.1.*
%{_mandir}/man1/xpra_*.1.*
%{_mandir}/man1/run_scaled.1.*
%{_metainfodir}/xpra.appdata.xml
%{_datadir}/mime/packages/application-x-xpraconfig.xml
%{_datadir}/xpra/
%{cupslibdir}/backend/xpraforwarder
%{_tmpfilesdir}/xpra.conf
%dir %{_rundir}/xpra
%{_docdir}/xpra
%{_unitdir}/xpra.service
%{_unitdir}/xpra.socket
%{_udevrulesdir}/71-xpra-virtual-pointer.rules

%changelog
%autochangelog
