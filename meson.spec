%global libname mesonbuild

%bcond check 1

Name:           meson
Version:        1.5.1
Release:        %autorelease
Summary:        High productivity build system

License:        Apache-2.0
URL:            https://mesonbuild.com/
Source:         https://github.com/mesonbuild/meson/releases/download/%{version_no_tilde .}/meson-%{version_no_tilde %{quote:}}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python%{python3_version}dist(setuptools)
Requires:       ninja-build

%if %{with check}
BuildRequires:  ninja-build
# Some tests expect the unversioned executable
BuildRequires:  /usr/bin/python
# Various languages
BuildRequires:  gcc
BuildRequires:  libasan
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
%if %{undefined rhel}
BuildRequires:  gcc-objc
BuildRequires:  gcc-objc++
%endif
BuildRequires:  java-devel
BuildRequires:  libomp-devel
%if %{undefined rhel}
BuildRequires:  mono-core mono-devel
%endif
BuildRequires:  rust
# Since the build is noarch, we can't use %%ifarch
#%%ifarch %%{ldc_arches}
#BuildRequires:  ldc
#%%endif
# Various libs support
BuildRequires:  boost-devel
BuildRequires:  /usr/bin/clang-format
%if %{undefined rhel}
BuildRequires:  clippy
%endif
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
%if %{undefined rhel}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-linguist
%endif
BuildRequires:  vala
BuildRequires:  python3-gobject-base
%if %{undefined rhel}
BuildRequires:  wxGTK-devel
BuildRequires:  bindgen
%endif
BuildRequires:  binutils-gold
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gettext
%if %{undefined rhel}
BuildRequires:  gnustep-base-devel
BuildRequires:  /usr/bin/gnustep-config
%endif
BuildRequires:  git-core
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(glib-2.0)
%if %{undefined rhel}
BuildRequires:  pkgconfig(glib-sharp-2.0)
%endif
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  pkgconfig(zlib)
BuildRequires:  zlib-static
BuildRequires:  python3dist(cython)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  /usr/bin/pcap-config
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  llvm-devel
BuildRequires:  cups-devel
%endif

%description
Meson is a build system designed to optimize programmer
productivity. It aims to do this by providing simple, out-of-the-box
support for modern software development tools and practices, such as
unit tests, coverage reports, Valgrind, CCache and the like.

%prep
%autosetup -p1 -n meson-%{version_no_tilde %{quote:}}
# Macro should not change when we are redefining bindir
sed -i -e "/^%%__meson /s| .*$| %{_bindir}/%{name}|" data/macros.%{name}

%build
%py3_build

%install
%py3_install
install -Dpm0644 -t %{buildroot}%{rpmmacrodir} data/macros.%{name}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions/ data/shell-completions/bash/meson
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions/ data/shell-completions/zsh/_meson

%if %{with check}
%check
export MESON_PRINT_TEST_OUTPUT=1
%{python3} ./run_unittests.py -v
%{python3} ./run_meson_command_tests.py -v
%endif

%files
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/%{libname}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_mandir}/man1/%{name}.1*
%{rpmmacrodir}/macros.%{name}
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
%{_datadir}/bash-completion/completions/meson
%{_datadir}/zsh/site-functions/_meson

%changelog
%autochangelog
