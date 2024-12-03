%global pypi_name credslayer
%bcond_with local

Name:           credslayer
Version:        0.1.2
Release:        16%{?dist}
Summary:        Extract credentials and other details from network captures

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/ShellCode33/CredSLayer
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pyshark
BuildRequires:  wireshark-cli

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
CredSLayer goal is to look for credentials and other useful stuff in network
captures. Two modes are available, pcap scanning and active processing. The
latest listens for packets on a chosen interface and dynamically extracts
everything it can.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
CredSLayer goal is to look for credentials and other useful stuff in network
captures. Two modes are available, pcap scanning and active processing. The
latest listens for packets on a chosen interface and dynamically extracts
everything it can.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{pypi_name}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-argparse

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n CredSLayer-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=%{PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%if %{with local}
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests/tests.py
%endif

%files
%{_bindir}/credslayer

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.2-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.1.2-14
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.1.2-10
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.1.2-7
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.2-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Remove shebang and Python standard module (rhbz#1856825)
- Update to latest upstream release 0.1.2

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora
