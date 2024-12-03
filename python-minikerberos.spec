%global pypi_name minikerberos

Name:           python-%{pypi_name}
Version:        0.2.9
Release:        13%{?dist}
Summary:        Kerberos manipulation library in Python

License:        MIT
URL:            https://github.com/skelsec/minikerberos
Source0:        %pypi_source
BuildArch:      noarch

%description
Kerberos manipulation library in pure Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Kerberos manipulation library in pure Python

%package -n %{pypi_name}
Summary:        %{summary}
Requires:       python3-%{pypi_name}

%description -n %{pypi_name}
Command line tools for Kerberos manipulations.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebangs. https://github.com/skelsec/minikerberos/issues/7
sed -i -e '/^#!\//, 1d' %{pypi_name}/{*.py,*/*.py,*/*/*.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%files -n %{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.9-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.9-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.9-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.9-2
- Rebuilt for Python 3.10

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.9-1
- Update to latest upstream release 0.2.9 (#1926520)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.8-1
- Update to latest upstream release 0.2.8 (#1914690)

* Fri Dec 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.7-1
- Update to latest upstream release 0.2.7 (#1905752)

* Wed Dec 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.6-1
- Update to latest upstream release 0.2.6 (#1905752)

* Wed Oct 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-1
- Update to latest upstream release 0.2.5 (#1891354)

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.4-1
- Update to new upstream version 0.2.4 (#1876057)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.3-1
- Update to new upstream version 0.2.3 (#1847184)

* Mon Jun 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Update to new upstream version 0.2.2 (#1846178)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Update to new upstream version 0.2.1 (#1808881)

* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Update to new upstream version 0.2.0 (#1808881)

* Sun Feb 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Update to new upstream version 0.1.0

* Sat Feb 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.12-1
- Update to new upstream version 0.0.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.11-1
- Update to new upstream version 0.0.11

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.10-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.10-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-2
- Remove binary (#1722597)

* Thu Jun 20 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-1
- Update to latest upstream release 0.0.10

* Sat Jun 15 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.7-1
- Initial package for Fedora
