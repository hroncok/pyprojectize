Name:       ydiff
Version:    1.3
Release:    4%{?dist}
Summary:    View colored, incremental diff
URL:        https://github.com/ymattw/ydiff
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
Source0:    https://github.com/ymattw/ydiff/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: python3-devel
BuildArch: noarch

Requires: less
Requires: python%{python3_pkgversion}-%{name}
%description
Term based tool to view colored, incremental diff in a Git/Mercurial/Svn
workspace or from stdin, with side by side (similar to diff -y) and auto
pager support.

%package -n     python3-%{name}
Summary:        %{summary}
%description -n python3-%{name}
Python library that implements API used by ydiff tool.

%prep
%autosetup -n %{name}-%{version}
/usr/bin/sed -i '/#!\/usr\/bin\/env python/d' ydiff.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%files
%doc README.rst
%license LICENSE
%{_bindir}/ydiff

%files -n python3-%{name} -f %{pyproject_files}

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3-2
- Rebuilt for Python 3.13


* Fri Apr 05 2024 Alois Mahdal <n9042e84@vornet.cz> 1.3-1
- Updated to 1.3

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2-9
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2-3
- Rebuilt for Python 3.10

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Alois Mahdal <amahdal@redhat.com> - 1.2-1
- Updated upstream to 1.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-9
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-6
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Alois Mahdal <n9042e84@vornet.cz> 1.1-1
- Initial packaging.
