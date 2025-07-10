%global srcname pypillowfight

Name:           python-%{srcname}
Version:        0.3.0
Release:        20%{?dist}
Summary:        Various image processing algorithms

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight
# PyPI tarball does not include tests.
#Source0:        https://files.pythonhosted.org/packages/source/p/%%{srcname}/%%{srcname}-%%{version}.tar.gz
Source0:        https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight/-/archive/%{version}/libpillowfight-%{version}.tar.gz
# https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight/issues/15
Source1:        images.tar.xz
# Because Fedora 32-bit does not necessarily support SSE2.
Patch0001:      0001-Do-not-override-compile-args.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global _description \
Library containing various image processing algorithms: Automatic Color \
Equalization, Unpaper's algorithms, Stroke Width Transformation, etc.

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-nose >= 1.0
BuildRequires:  python3-pillow

Requires:       python3-pillow%{?_isa}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n libpillowfight-%{version} -p1
%setup -D -T -n libpillowfight-%{version} -q -a 1


echo "#define INTERNAL_PILLOWFIGHT_VERSION \"%{version}\"" > src/pillowfight/_version.h


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pillowfight


%check
%pyproject_check_import

# https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight/issues/11
PYTHONPATH=%{buildroot}%{python3_sitearch} \
    nosetests-3 -v -P tests -I 'tests_swt.py' -I 'tests_canny.py'


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.3.0-19
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.3.0-15
- Rebuilt for Python 3.12

* Sat Apr 08 2023 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-14
- Switch to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-12
- Drop support for i686

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.0-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.0-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-1
- New upstream release.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-2
- Fix license and requires.

* Wed Dec 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Initial package.
