Name:       vapoursynth
Version:    68
Release:    4%{?dist}
Summary:    Video processing framework with simplicity in mind
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2
URL:        http://www.vapoursynth.com

Source0:    https://github.com/%{name}/%{name}/archive/R%{version}/%{name}-R%{version}.tar.gz
Patch0:     %{name}-version-info.patch

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  python3
BuildRequires:  python3-Cython

%{?_with_tests:
BuildRequires:  %{name}-devel
BuildRequires:  python3dist(pytest)
}

%description
VapourSynth is an application for video manipulation. Or a plugin. Or a library.
It’s hard to tell because it has a core library written in C++ and a Python
module to allow video scripts to be created.

%package        libs
Summary:        VapourSynth's core library with a C++ API
Obsoletes:      lib%{name} < %{version}-%{release}
Provides:       lib%{name} == %{version}-%{release}
Obsoletes:      %{name}-plugins < %{version}-%{release}
Provides:       %{name}-plugins == %{version}-%{release}

%description    libs
VapourSynth's core library with a C++ API.

%package -n     python3-%{name}
Summary:        Python interface for VapourSynth

%description -n python3-%{name}
Python interface for VapourSynth/VSSCript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        tools
Summary:        Extra tools for VapourSynth

%description    tools
This package contains the vspipe tool for interfacing with VapourSynth.

%prep
%autosetup -p1 -n %{name}-R%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
autoreconf -vif
%configure \
    --disable-static \
    --enable-x86-asm \
    --enable-core \
    --enable-vsscript \
    --enable-vspipe \
    --enable-python-module

%make_build

%install
%pyproject_install
%make_install
find %{buildroot} -type f -name "*.la" -delete

# Create plugin directory
mkdir -p %{buildroot}%{_libdir}/%{name}

# Let RPM pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets libs
%ldconfig_scriptlets -n python3-%{name}

%{?_with_tests:
%check
%{python3} -m pytest -v
}

%files libs
%doc ChangeLog
%license COPYING.LESSER
%dir %{_libdir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}-script.so.*

%files -n python3-%{name}
%{python3_sitearch}/%{name}.so
%{python3_sitearch}/VapourSynth.dist-info

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-script.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-script.pc

%files tools
%{_bindir}/vspipe

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 68-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 68-2
- Rebuilt for Python 3.13

* Wed May 22 2024 Simone Caronni <negativo17@gmail.com> - 68-1
- Update to R68.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 02 2023 Simone Caronni <negativo17@gmail.com> - 65-1
- Update to version R65.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 63-2
- Rebuilt for Python 3.12

* Fri Jun 30 2023 Simone Caronni <negativo17@gmail.com> - 63-1
- Update to R63.

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 58-5
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 58-2
- Rebuilt for Python 3.11

* Wed May 25 2022 Simone Caronni <negativo17@gmail.com> - 58-1
- Update to R58.

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 57-2
- Rebuild for tesseract 5.1.0

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 57-1
- Update to R57.
- Plugins are now separate.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 51-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 19 2021 Sandro Mani <manisandro@gmail.com> - 51-6
- Rebuild (tesseract)

* Tue Dec 14 2021 Sandro Mani <manisandro@gmail.com> - 51-5
- Rebuild (tesseract)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 51-3
- Rebuilt for Python 3.10

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 51-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Mar 23 2021 Simone Caronni <negativo17@gmail.com> - 51-1
- Update to R51.
- Allow building for other archs beside x86.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 48-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Jeff Law <law@redhat.com> - 48-10
- Fix missing #include for gcc-11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 48-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 48-8
- Rebuilt for Python 3.9

* Sat Mar 07 2020 Simone Caronni <negativo17@gmail.com> - 48-7
- Fix broken dependency.

* Sat Feb 29 2020 Simone Caronni <negativo17@gmail.com> - 48-6
- Make it exclusive for i686/x86_64.
- Fix build on RHEL/CentOS 8.

* Tue Feb 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 48-5
- Add tests
- Cosmetic spec file improvements

* Thu Feb 20 2020 Simone Caronni <negativo17@gmail.com> - 48-4
- More review fixes.
- Use upstream patch for Python 3.8.

* Fri Feb 07 2020 Simone Caronni <negativo17@gmail.com> - 48-3
- Review fixes.

* Sun Jan 26 2020 Simone Caronni <negativo17@gmail.com> - 48-2
- Move script library into main library package.
- Fix build with Python 3.8.

* Thu Jan 16 2020 Simone Caronni <negativo17@gmail.com> - 48-1
- First build.
