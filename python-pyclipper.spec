%global srcname pyclipper

Name:           python-%{srcname}
Version:        1.2.0
Release:        16%{?dist}
Summary:        Cython wrapper for the C++ translation of the Angus Johnson's Clipper library

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/greginvm/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Cython: set language_level=2 explicitly as 3 is now default
# From https://github.com/fonttools/pyclipper/commit/b740d823
Patch:          0001-set-language_level-2-explicitly-as-3-is-now-default.patch

BuildRequires:  gcc-c++
BuildRequires:  polyclipping-devel

%description
Pyclipper is a Cython wrapper exposing public functions and classes of the C++
translation of the Angus Johnson's Clipper library.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-Cython
BuildRequires:  python3-setuptools_scm

%description -n python3-%{srcname}
Pyclipper is a Cython wrapper exposing public functions and classes of the C++
translation of the Angus Johnson's Clipper library.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove upstream egg-info
rm -rf pyclipper.egg-info
# Since there are no .git dir, there is no need to exclude files in MANIFEST.in
sed -i '/^exclude/d' MANIFEST.in

sed -i "s/'unittest2', //" setup.py
sed -i s/unittest2/unittest/ tests/test_pyclipper.py

%generate_buildrequires
%pyproject_buildrequires

%build
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l '*'

%check
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{__python3} setup.py test

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.0-15
- Rebuilt for Python 3.13

* Tue May 28 2024 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-14
- Fix FTBFS with Cython 3
- Drop superfluous BuildRequires python3-setuptools_scm_git_archive
- Fixes: rhzb#2248707

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 1.2.0-1
- Update version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0.post3-2
- Rebuilt for Python 3.9

* Sat Feb 29 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0.post3-1
- Update version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-9
- Remove dependency on unittest2 (#1789200)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Subpackage python2-pyclipper has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.7

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.1.0-2
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 16 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-1
- Update version
- Remove patch to use new polyclipping version (merged upstream)
- Fix patch to use system libraries due to new version modifications

* Mon Oct 23 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.6-4
- Do not Requires polyclipping
- Remove upstream egg-info before building
- Cython cpp file before each python version build

* Sun Oct 22 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.6-3
- Patch sources for compatibility with polyclipping 6.4.2

* Sun Jul 16 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.6-2
- Remove embedded libraries and use system ones instead
- Fix date format in changelog

* Wed Apr 05 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.6-1
- Initial package
