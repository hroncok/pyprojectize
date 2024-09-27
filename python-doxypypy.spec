%global srcname doxypypy
%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        0.8.8.6
Release:        9%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
Summary:        A more Pythonic version of doxypy, a Doxygen filter for Python
Url:            https://github.com/Feneric/%{srcname}
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
A more Pythonic version of doxypy, a Doxygen filter for Python.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     python3-%{srcname}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}


# Remove shebangs
find . -name \*.py -exec sed -i '/#!\/usr\/bin\/env /d' '{}' \;
find . -name \*.py -exec sed -i '/#!\/usr\/bin\/python/d' '{}' \;

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%attr(644, -, -) %{python3_sitelib}/%{srcname}/*.py
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.8.6-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.8.6-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.8.6-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.8.8.6-1
- Initial version of package
