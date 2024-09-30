%global pypi_name pypcapkit

Name:           python-%{pypi_name}
Version:        0.15.5
Release:        12%{?dist}
Summary:        Python multi-engine PCAP analyse kit

License:        MPL-2.0
URL:            https://github.com/JarryShaw/pypcapkit
Source0:        https://github.com/JarryShaw/PyPCAPKit/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The pcapkit project is an open source Python program focus on PCAP parsing
and analysis, which works as a stream PCAP file extractor. With support of
dictdumper, it shall support multiple output report formats.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
The pcapkit project is an open source Python program focus on PCAP parsing
and analysis, which works as a stream PCAP file extractor. With support of
dictdumper, it shall support multiple output report formats.

%prep
%autosetup -n PyPCAPKit-%{version}
chmod -x LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pcapkit

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/pcapkit*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.15.5-11
- Rebuilt for Python 3.13

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 0.15.5-10
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.15.5-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.15.5-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.5-1
- Update to latest upstream release 0.15.5 (closes rhbz#1969097)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.15.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.3-1
- Update to latest upstream release 0.15.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.2-1
- Update to latest upstream release 0.15.2

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.5-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.5-1
- Update to latest upstream release 0.14.5

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.2-1
- Update to latest upstream release 0.14.2
- Use upstream source instead of PyPI (rhbz#1714013)

* Sun May 26 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.3-1.post2
- Initial package for Fedora
