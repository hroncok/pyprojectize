%global pkg_name protego
%global pypi_name Protego
%global desc %{expand:
Protego is a pure-Python `robots.txt` parser with support for modern
conventions.}

Name:		python-protego
Version:	0.3.0
Release:	6%{?dist}
Summary:	Pure-Python robots.txt parser with support for modern conventions

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/scrapy/protego
Source0:	%{pypi_source}

BuildArch:	noarch


%description
%{desc}

%package -n python3-%{pkg_name}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-pytest


%description -n python3-%{pkg_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files protego

%check
%pytest

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 12 2023 Eduardo Echeverria  <echevemaster@gmail.com> - 0.3.0-1
- Bump package version
- Removing six

* Sun Sep 17 2023 Eduardo Echeverria  <echevemaster@gmail.com> - 0.2.1-7
- Fix install dependencies
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.11

* Sun Feb 20 2022 Eduardo Echeverria <echevemaster@gmail.com> - 0.2.1-1
- Bumped to the latest upstream version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.16-2
- Rebuilt for Python 3.10

* Sat Apr 3 2021 Eduardo Echeverria <echevemaster@gmail.com> - 0.1.16-1
- Initial packaging
