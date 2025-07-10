%global pypi_name pwncat

Name:           %{pypi_name}
Version:        0.1.0
Release:        16%{?dist}
Summary:        TCP/UDP communication suite

License:        MIT
URL:            https://github.com/cytopia/pwncat
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
TCP/UDP communication suite for firewall and IDS/IPS evasion, bind and
reverse shell, self-injecting shell and port forwarding magic. pwncat is
fully scriptable with Python (PSE).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
TCP/UDP communication suite for firewall and IDS/IPS evasion, bind and
reverse shell, self-injecting shell and port forwarding magic. pwncat is
fully scriptable with Python (PSE).

%prep
%autosetup -n %{pypi_name}-%{version}

# Fix build with setuptools 62.1
# https://github.com/cytopia/pwncat/issues/113
sed -i "10i packages=[]," setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
install -Dp -m 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc docs/
%{_mandir}/man1/%{name}.*
%{_bindir}/pwncat

%files -n python3-%{pypi_name}
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}-*.dist-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.0-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.0-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Charalampos Stratakis <cstratak@redhat.com> - 0.1.0-8
- Fix FTBFS with setuptools >= 62.1
Resolves: rhbz#2097117

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-2
- Fix review issues (rhbz#1856904)

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Initial package for Fedora
