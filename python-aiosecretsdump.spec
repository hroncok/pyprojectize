%global pypi_name aiosecretsdump

Name:           python-%{pypi_name}
Version:        0.0.2
Release:        14%{?dist}
Summary:        Secrets dumper

License:        MIT
URL:            https://github.com/skelsec/aiosecretsdump
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Dump secrets feature for aiosmb.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Dump secrets feature for aiosmb.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove shebang
sed -i -e '/^#!\//, 1d' aiosecretsdump/__init__.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/aiosecretsdump
%{python3_sitelib}/%{pypi_name}
# https://github.com/skelsec/aiosecretsdump/issues/2
%{python3_sitelib}/bins
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.2-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.2-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.2-1
- Update to latest upstream release 0.0.2

* Mon Nov 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.1-2
- Add missing BRs (#1825592)

* Sun Apr 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.1-1
- Initial packagefor Fedora