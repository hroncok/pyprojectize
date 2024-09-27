%global pypi_name whois

%global pypi_description Python wrapper for the "whois" command with \
a simple interface to access parsed WHOIS data for a given domain, \
able to extract data for all the popular TLDs (com, org, net, biz, info...).

Name: python-%{pypi_name}
Summary: Python module for retrieving WHOIS information of domains
License: MIT

Version: 0.9.27
Release: 7%{?dist}

URL: https://github.com/DannyCork/python-whois/
Source0: %{URL}archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

Requires: whois

%description
%pypi_description


%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%pypi_description


%prep
%setup -q


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%check
./test.sh


%files -n python3-%{pypi_name}
%license license
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}.dist-info


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.27-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.27-2
- Rebuilt for Python 3.12

* Tue Feb 07 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.27-1
- Update to v0.9.27

* Tue Jan 31 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.26-1
- Update to v0.9.26

* Fri Jan 27 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.25-1
- Update to v0.9.25

* Wed Jan 25 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.24-1
- Update to v0.9.24

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.23-1
- Update to v0.9.23

* Mon Jan 09 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.22-1
- Update to v0.9.22

* Wed Jan 04 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.21-1
- Update to v0.9.21

* Sun Jan 01 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.20-1
- Update to v0.9.20

* Tue Dec 27 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.19-1
- Update to v0.9.19
- Switch to using GitHub tarballs (PyPi sources do not contain tests)

* Fri Nov 04 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.17-1
- Update to v0.9.17

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.16-2
- Rebuilt for Python 3.11

* Fri Jun 10 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.16-1
- Update to version 0.9.16

* Wed May 18 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.15-1
- Update to version 0.9.15

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.10-2
- Rebuilt for Python 3.10

* Wed Apr 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.10-1
- Update to version 0.9.10

* Tue Apr 13 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.9-1
- Update to version 0.9.9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.7-1
- Update to version 0.9.7

* Thu Feb 27 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.6-2
- Include the README in the package

* Thu Feb 27 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.6-1
- Initial packaging
