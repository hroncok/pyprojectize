%global pypi_name urlbuster

Name:           %{pypi_name}
Version:        0.5.1
Release:        4%{?dist}
Summary:        URL bruteforcer to locate files or directories

License:        MIT
URL:            https://github.com/cytopia/urlbuster
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Powerful web directory fuzzer to locate existing and/or hidden files or
directories.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Powerful web directory fuzzer to locate existing and/or hidden files or
directories.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files
%{_bindir}/%{pypi_name}
%{_datadir}/%{pypi_name}/

%files -n python3-%{pypi_name}
%doc README.md examples/
%license LICENSE.txt
%{_bindir}/urlbuster
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Lumír Balhar <lbalhar@redhat.com> - 0.5.1-1
- Update to 0.5.1

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.0-10
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.0-7
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-2
- Add examples (rhbz#1856864)

* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Initial package for Fedora
