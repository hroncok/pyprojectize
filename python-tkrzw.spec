%global	module	tkrzw

Name:		python-%{module}
Version:	0.1.32
Release:	3%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
Summary:	TKRZW Python bindings
URL:		https://dbmx.net/tkrzw/
Source0:	https://dbmx.net/tkrzw/pkg-python/%{module}-python-%{version}.tar.gz
# https://github.com/estraier/tkrzw-python/issues/6
Patch0:		%{name}-%{version}.patch
BuildRequires:	gcc-c++
# python3-devel
BuildRequires:	pkgconfig(python3)
# python3-sphinx
BuildRequires:	python3dist(sphinx)
# tkrzw due tkrzw_build_util
BuildRequires:	tkrzw >= 1.0.30
# tkrzw-devel
BuildRequires:	pkgconfig(tkrzw) >= 1.0.30
# xz-devel
BuildRequires:	pkgconfig(liblzma)
# lz4-devel
BuildRequires:	pkgconfig(liblz4)
# libzstd-devel
BuildRequires:	pkgconfig(libzstd)
# zlib-devel
BuildRequires:	pkgconfig(zlib)
# Temporary disabled: https://github.com/estraier/tkrzw-python/issues/4
ExcludeArch:	i686

%description
TKRZW is a library of routines for managing a key-value database.

%package -n	python3-%{module}
Summary:	%{summary}
%if 0%{?epel} && 0%{?epel} < 9
%endif

%description -n	python3-%{module}
TKRZW is a library of routines for managing a key-value database.

%package	doc
Summary:	%{summary} - API documentation
BuildArch:	noarch

%description	doc
TKRZW is a library of routines for managing a key-value database.
This package contains API documentation of it.


%prep
%autosetup -n %{module}-python-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%make_build apidoc


%install
%pyproject_install
%pyproject_save_files -l tkrzw


%check
%pyproject_check_import

export PYTHONPATH=%{buildroot}%{python3_sitearch}
%make_build check


%files -n python3-%{module} -f %{pyproject_files}
%if 0%{?epel} && 0%{?epel} < 9
%else
%endif

%files doc
%license COPYING
%doc README CONTRIBUTING.md example?.py api-doc/


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.32-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 TI_Eugene <ti.eugene@gmail.com> - 0.1.32-1
- Version bump

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.31-2
- Rebuilt for Python 3.13

* Tue May 07 2024 TI_Eugene <ti.eugene@gmail.com> - 0.1.31-1
- Version bump

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.1.30-2
- Rebuilt for Python 3.12

* Thu Apr 06 2023 TI_Eugene <ti.eugene@gmail.com> - 0.1.30-1
- Version bump

* Mon Feb 20 2023 TI_Eugene <ti.eugene@gmail.com> - 0.1.29-1
- Version bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.28-7
- Rebuilt for Python 3.11

* Fri Apr 08 2022 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-6
- Temporary excluded i686 for F36+

* Fri Apr 08 2022 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-5
- Rebuild against tkrzw-1.0.24

* Wed Mar 09 2022 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-4
- Rebuild against tkrzw-1.0.23

* Sun Jan 23 2022 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-3
- Rebuild against tkrzw-1.0.22

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 27 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.28-1
- Version bump

* Thu Nov 18 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.27-1
- Version bump

* Sat Oct 09 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.23-1
- Version bump
- Build against tkrzw-1.0.17
- ppc64le enabled back

* Sat Sep 25 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.22-1
- Version bump
- Build against tkrzw-1.0.13
- ppc64le temporary excluded

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.7-2
- Rebuilt for Python 3.10

* Fri May 14 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.7-1
- Version bump
- Build against tkrzw-0.9.16

* Tue May 04 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.6-1
- Version bump

* Sun Feb 14 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.4-2
- python_provide fix
- -doc subpackage added
- check introduced
- epel8 compatible

* Sat Feb 06 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.4-1
- Initial build
