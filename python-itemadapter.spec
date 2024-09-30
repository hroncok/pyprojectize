%global pkg_name itemadapter
%global desc %{expand:
The ItemAdapter class is a wrapper for data container objects,
providing a common interface to handle objects of different
types in an uniform manner, regardless of their underlying implementation.}
Name:		python-itemadapter
Version:	0.9.0
Release:	11%{?dist}
Summary:	The ItemAdapter class is a wrapper for data container object

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/scrapy/itemadapter
Source0:	%{pypi_source %pkg_name}

BuildArch:	noarch


%description
%{desc}

%package -n python3-%{pkg_name}
Summary:	%{summary}

BuildRequires:	python3-devel
Requires:	python3-attrs

%py_provides  python3-%{pkg_name}


%description -n python3-%{pkg_name}
%{desc}

%prep
%autosetup -n %{pkg_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l itemadapter

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.0-11
- convert license to SPDX

* Fri Aug 16 2024 Eduardo Echeverria <echevemaster@gmail.com> - 0.9.0-1
- Bumped to the latest upstream version

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.11

* Sun Feb 20 2022 Eduardo Echeverria <echevemaster@gmail.com> - 0.4.0-1
- Bumped to the latest upstream version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.10

* Sat Apr 3 2021 Eduardo Echeverria <echevemaster@gmail.com> - 0.2.0-1
- Initial packaging

