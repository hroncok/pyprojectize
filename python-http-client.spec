%global srcname http-client
%global desc Quickly and easily access any RESTful or RESTful-like API.

Name:           python-%{srcname}
Version:        3.3.7
Release:        10%{?dist}
Summary:        HTTP REST client, simplified for Python
License:        MIT
URL:            https://github.com/sendgrid/%{name}
Source0:        %{url}/archive/%{version}.tar.gz

BuildArch:      noarch


%description
%{desc}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}
This is a Python 3 version of the package.


%prep
%autosetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%check
# test_daterange.py tests the presence of the current year
# in the license file and breaks every January
%pytest --ignore=tests/test_daterange.py


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGELOG.md USAGE.md
%{python3_sitelib}/python_http_client/
%{python3_sitelib}/python_http_client-%{version}.dist-info/
%exclude %{python3_sitelib}/tests


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.7-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.3.7-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.7-2
- Rebuilt for Python 3.11

* Fri Mar 11 2022 Lumír Balhar <lbalhar@redhat.com> - 3.3.7-1
- Update to 3.3.7
Resolves: rhbz#2062946

* Fri Feb 11 2022 Lumír Balhar <lbalhar@redhat.com> - 3.3.6-1
- Update to 3.3.6
Resolves: rhbz#2052907

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Lumír Balhar <lbalhar@redhat.com> - 3.3.5-1
- Update to 3.3.5
Resolves: rhbz#2040432

* Fri Dec 17 2021 Lumír Balhar <lbalhar@redhat.com> - 3.3.4-1
- Update to 3.3.4
Resolves: rhbz#2028633

* Wed Oct 06 2021 Lumír Balhar <lbalhar@redhat.com> - 3.3.3-1
- Update to 3.3.3
Resolves: rhbz#2007053

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.2-2
- Rebuilt for Python 3.10

* Thu Feb 11 2021 Lumír Balhar <lbalhar@redhat.com> - 3.3.2-1
- Update to 3.3.2
Resolves: rhbz#1927544

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Lumír Balhar <lbalhar@redhat.com> - 3.3.1-2
- Fix FTBFS by ignoring test of the year in the license file

* Thu Aug 27 2020 Lumír Balhar <lbalhar@redhat.com> - 3.3.1-1
- Update to 3.3.1 (#1870393)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.7-2
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.7-1
- Update to 3.2.7 (#1819947)

* Thu Mar 05 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.6-1
- Update to 3.2.6 (#1805003)

* Thu Feb 20 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.5-1
- Update to 3.2.5 (#1805003)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.4-1
- New upstream version 3.2.4 (bz#1794624)

* Thu Jan 23 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.3-1
- New upstream version 3.2.3 (bz#1794323)

* Fri Sep 13 2019 Lumír Balhar <lbalhar@redhat.com> - 3.2.1-1
- New upstream version 3.2.1 (bz#1751784)

* Thu Sep 12 2019 Lumír Balhar <lbalhar@redhat.com> - 3.2.0-1
- New upstream version 3.2.0 (bz#1751451)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Lumír Balhar <lbalhar@redhat.com> - 3.1.0-6
- Skip useles failing test

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Lumír Balhar <lbalhar@redhat.com> - 3.1.0-4
- Get rid of Python 2 subpackage
- Resolves: rhbz#1639322

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Lumír Balhar <lbalhar@redhat.com> - 3.1.0-1
- New usptream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Lumír Balhar <lbalhar@redhat.com> 3.0.0-1
- New upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-2
- Rebuild for Python 3.6

* Thu Aug 11 2016 Dominika Krejci <dkrejci@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Mon Jul 18 2016 Dominika Krejci <dkrejci@redhat.com> - 2.1.1-1
- Initial release

