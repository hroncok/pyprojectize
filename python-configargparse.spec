%global srcname ConfigArgParse

Name:           python-configargparse
Version:        1.7
Release:        5%{?dist}
Summary:        Python module with support for argparse, config files, and env variables

License:        MIT
URL:            https://github.com/bw2/ConfigArgParse
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files, hard
coded defaults, and in some cases, environment variables.

Python’s command line parsing modules such as argparse have very limited
support for config files and environment variables, so this module extends
argparse to add these features.

%package -n python3-configargparse
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyyaml
%{?python_provide:%python_provide python3-configargparse}

%description -n python3-configargparse
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files, hard
coded defaults, and in some cases, environment variables.

Python’s command line parsing modules such as argparse have very limited
support for config files and environment variables, so this module extends
argparse to add these features.

%prep
%autosetup -p0 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
# the compared outputs of testBasicCase2 and testMutuallyExclusiveArgs don't
# match with the those generated by Python 3.13
# Reported: https://github.com/bw2/ConfigArgParse/issues/294
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -k "not TestMisc \
  and not testBasicCase2 and not testMutuallyExclusiveArgs"

%files -n python3-configargparse
%doc README.rst
%license LICENSE
%{python3_sitelib}/configargparse.py*
%{python3_sitelib}/%{srcname}*.egg-info
%{python3_sitelib}/__pycache__/configargparse*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.7-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Jonathan Wright <jonathan@almalinux.org> - 1.7-1
- Update to 1.7 rhbz#2225187

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Jonathan Wright <jonathan@almalinux.org> - 1.5.5-1
- Update to 1.5.5 rhbz#2218395

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5.3-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.3-2
- Rebuilt for Python 3.11

* Tue Feb 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.3-1
- Update to new upstream version 1.5.3 (closes rhbz#2010146)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.2-1
- Update to new upstream version 1.5.2 (closes rhbz#1974548)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Major Hayden <major@mhtx.net> - 1.4.1-1
- Add patch to temporarily make tests work with argparse in Python 3.10. (BZ 1914818)
- Update to version 1.4.1.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-1
- Update to new upstream version 1.4 (#1928695)

* Mon Feb 15 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-1
- Update to new upstream version 1.3 (#1928695)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.3-2
- Update check section

* Wed May 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.3-1
- update to new upstream version 1.2.3 (rhbz#1827624)
- run tests in %%check

* Thu Apr 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to new upstream version 1.2.2 (rhbz#1827055)

* Fri Apr 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Update to new upstream version 1.2.1 (rhbz#1820195)

* Thu Apr 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-1
- Update to new upstream version 1.2 (rhbz#1820195)

* Tue Mar 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1-1
- Update to new upstream version 1.1 (rhbz#1813693)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.2-1
- Update to new upstream version 0.15.2 (rhbz#1782322)

* Mon Oct 14 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.1-1
- Update to new upstream version 0.15.1 (rhbz#1759632)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Eli Young <elyscape@gmail.com> - 0.14.0-2
- Rebuilt to ensure upgrades from Fedora 29

* Sun Apr 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-1
- Update to new upstream version 0.14.0

* Wed Apr 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.0-1
- Update to new upstream version 0.13.0 (rhbz#1643700)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-6
- Subpackage python2-configargparse has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Update to new upstream version 0.12.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-2
- Rebuild for Python 3.6

* Tue Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-1
- Update to new upstream version 0.11.0 (rhbz#1382975)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0 for Let's Encrypt dep

* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 0.9.3-5
- epel7: Only build python2 package

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-3
- Remove old parts

* Fri Oct 30 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-2
- Update macros

* Thu Feb 05 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Initial package
