%global srcname colorlog
%global desc "colorlog.ColoredFormatter is a formatter for use with Python's logging module that outputs records using terminal colors."

Name:           python-%{srcname}
Version:        6.8.2
Release:        3%{?dist}
Summary:        Colored formatter for the Python logging module

License:        MIT
URL:            https://github.com/borntyping/python-colorlog
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%else
BuildRequires:  python3-devel
%endif

%description
%{desc}

%if 0%{?rhel} && 0%{?rhel} < 8
%package -n python2-%{srcname}
Summary:        %{summary}

%description -n python2-%{srcname}
%{desc}
%else
%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{desc}
%endif

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?rhel} && 0%{?rhel} < 8
%py2_build
%else
%pyproject_wheel
%endif

%install
%if 0%{?rhel} && 0%{?rhel} < 8
%py2_install
%else
%pyproject_install
%endif

%if 0%{?rhel} && 0%{?rhel} < 8
%files -n python2-%{srcname}
%doc README.md
%license LICENSE
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}*.dist-info/
%else
%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.dist-info/
%endif

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 6.8.2-2
- Rebuilt for Python 3.13

* Mon Feb 05 2024 Fabian Affolter <mail@fabian-affolter.ch> - 6.8.2-1
- Update to latest upstream release (closes rhbz#2252570)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 6.7.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 14 2022 Fabian Affolter <mail@fabian-affolter.ch> - 6.7.0-1
- Update to latest upstream release 6.7.0 (closes rhbz#2122243)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.6.0-2
- Rebuilt for Python 3.11

* Tue Feb 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 6.6.0-1
- Update to latest upstream release 6.6.0 (closes rhbz#2021282)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 13 2021 Fabian Affolter <mail@fabian-affolter.ch> - 6.5.0-1
- Update to latest upstream release 6.5.0 (closes rhbz#2011781)

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 6.4.1-1
- Update to latest upstream release 6.4.1 (rhbz#1941570)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.7.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 4.7.2-1
- Update to latest upstream release 4.7.2 (#1916286)

* Sun Dec 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.6.2-1
- Update to latest upstream release 4.6.2 (#1895866)

* Sun Nov 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.5.0-1
- Update to latest upstream release 4.5.0 (#1895334)

* Thu Oct 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.4.0-1
- Update to latest upstream release 4.4.0 (#1886516)

* Tue Jul 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.2.1-1
- Update to latest upstream release 4.2.1 (#1860075)

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-1
- Update to latest upstream release 4.1.0 (#1753875)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 10 2019 Marek Goldmann <mgoldman@redhat.com> - 4.0.1-3
- Add support for EPEL 7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.1-1
- Update to latest upstream release 4.0.1

* Wed Oct 10 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-2
- Rebuilt for Python 3.7

* Sat May 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.4-1
- Update to latest upstream release 3.1.4 (#1568639)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.2-1
- Update to latest upstream release 3.1.2 (#1539019)

* Sat Jul 29 2017 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Update to latest upstream release 3.1.0 (#1476423)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-2
- Rebuild for Python 3.6

* Tue Nov 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.0-1
- Add license file
- Update to latest upstream release 2.9.0

* Tue Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.0-2
- Fix ownership

* Mon Nov 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.0-1
- Initial version
