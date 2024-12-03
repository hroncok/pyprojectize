%global pypi_name shodan
# The tests require a working API key and the possibility to connect to Shodan.io
%bcond_with api_key
# Add your Shodan.io API key
%global api_key ABCDEFGH

Name:           python-%{pypi_name}
Version:        1.31.0
Release:        3%{?dist}
Summary:        Python library and command-line utility for Shodan.io

License:        MIT
URL:            https://github.com/achillean/shodan-python
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  dos2unix

%description
The official Python library and CLI for Shodan Shodan is a search engine for 
Internet-connected devices. Google lets you search for websites, Shodan lets
you search for devices. This library provides developers easy access to all
of the data stored in Shodan in order to automate tasks and integrate into
existing tools.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-click
BuildRequires:  python3-click-plugins
BuildRequires:  python3-colorama
BuildRequires:  python3-requests
BuildRequires:  python3-xlsxwriter

%description -n python3-%{pypi_name}
The official Python library and CLI for Shodan Shodan is a search engine for 
Internet-connected devices. Google lets you search for websites, Shodan lets
you search for devices. This library provides developers easy access to all
of the data stored in Shodan in order to automate tasks and integrate into
existing tools.

%package -n python-%{pypi_name}-doc
Summary:        %{name} documentation

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%package -n     %{pypi_name}
Summary:        CLI tool to access Shodan.io

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{pypi_name}
Command-line tool to to access Shodan.io.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' shodan/cli/worldmap.py
dos2unix docs/{api.rst,tutorial.rst}
dos2unix docs/examples/{basic-search.rst,cert-stream.rst,query-summary.rst}
%if %{with api_key}
echo %{api_key} > SHODAN-API-KEY
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%if %{with api_key}
%check
%pyproject_check_import

%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n %{pypi_name}
%{_bindir}/%{pypi_name}

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.31.0-2
- Rebuilt for Python 3.13

* Sun Apr 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.31.0-1
- Update to latest upstream release

* Sat Feb 03 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.30.0-1
- Update to latest upstream release 1.30.0 (closes rhbz#2232219)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.29.1-2
- Rebuilt for Python 3.12

* Tue May 23 2023 Fabian Affolter <mail@fabian-affolter.ch> - 1.29.1-1
- Update to latest upstream release 1.29.1 (closes rhbz#2204485)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.28.0-1
- Update to latest upstream release 1.28.0 (closes rhbz#2105727)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.27.0-2
- Rebuilt for Python 3.11

* Thu Mar 03 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.27.0-1
- Update to latest upstream release 1.27.0 (closes rhbz#2057211)

* Sat Jan 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.6.1-1
- Update to latest upstream release 1.26.1 (closes rhbz#2037983)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.24.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.24.0-1
- Update to latest upstream release 1.24.0

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.23.1-1
- Update to latest upstream release 1.23.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.23.0-1
- Update to latest upstream release 1.23.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.22.0-2
- Rebuilt for Python 3.9

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.22.0-1
- Update to latest upstream release 1.22.0

* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.3-3
- Fix line endings

* Tue Jan 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.3-2
- Fix ownership
- Improve the check workflow (rhbz#1795077)

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.3-1
- Initial package for Fedora
