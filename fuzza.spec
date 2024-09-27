%global pypi_name fuzza
%{?python_disable_dependency_generator}

Name:           %{pypi_name}
Version:        0.6.0
Release:        12%{?dist}
Summary:        TCP fuzzing tool to test for remote buffer overflows

License:        MIT
URL:            https://github.com/cytopia/fuzza
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
fuzza is able to send and receive any initial commands prior sending the
payload as well as sending any post commands after the payload has been
sent. In order to replicate and triage the buffer overflow, fuzza can be
used to generate custom Python scripts for attack, bad chars and finding
the eip based on your command line arguments.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
fuzza is able to send and receive any initial commands prior sending the
payload as well as sending any post commands after the payload has been
sent. In order to replicate and triage the buffer overflow, fuzza can be
used to generate custom Python scripts for attack, bad chars and finding
the eip based on your command line arguments.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# Tests are designed to run manually
#%%check
#PYTHONPATH=%%{buildroot}%%{python3_sitelib} pytest-%%{python3_version} -v tests/expected/*.py

%files
%{_bindir}/fuzza

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-3
- Disable dependency generator

* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-2
- Adjust requirement for dependency generator (rhbz#1856880)

* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Initial package for Fedora
