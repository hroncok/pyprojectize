%global srcname jenkins

Name:           python-%{srcname}
Version:        1.8.2
Release:        4%{?dist}
Summary:        Python bindings for the remote Jenkins API

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://python-jenkins.readthedocs.org/en/latest
Source0:        https://opendev.org/jjb/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  %{_bindir}/sphinx-build
BuildArch:      noarch

%description
Python Jenkins is a library for the remote API of the Jenkins continuous
integration server. It is useful for creating and managing jobs as well as
build nodes.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-kerberos
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-multi_key_dict
BuildRequires:  python%{python3_pkgversion}-multiprocess
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-pbr >= 0.8.2
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-requests-mock
BuildRequires:  python%{python3_pkgversion}-six >= 1.3.0
BuildRequires:  python%{python3_pkgversion}-testscenarios
BuildRequires:  python%{python3_pkgversion}-testtools

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-multi_key_dict
Requires:       python%{python3_pkgversion}-pbr >= 0.8.2
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-six >= 1.3.0
%endif

%if 0%{?!rhel} || 0%{?rhel} >= 8
Recommends:     python%{python3_pkgversion}-kerberos
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Python Jenkins is a library for the remote API of the Jenkins continuous
integration server. It is useful for creating and managing jobs as well as
build nodes.


%prep
%autosetup -p1 -n %{name}

# Remove env from __init__.py
sed -i '1{s|^#!/usr/bin/env python||}' jenkins/__init__.py


%generate_buildrequires
%pyproject_buildrequires


%build
export PBR_VERSION=%{version}

%pyproject_wheel

PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=$PWD \
  %make_build -C doc html man
rm doc/build/html/.buildinfo


%install
export PBR_VERSION=%{version}

%pyproject_install
%pyproject_save_files -l %{srcname}

install -D -m0644 -p doc/build/man/pythonjenkins.1 %{buildroot}%{_mandir}/man1/pythonjenkins.1


%check
%pyproject_check_import
%{__python3} -m testtools.run discover tests


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst doc/build/html
%{_mandir}/man1/pythonjenkins.1.*


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.2-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 03 2024 Christoph Erhardt <fedora@sicherha.de> - 1.8.2-1
- Update to 1.8.2 (rhbz#2233791)
- Drop upstreamed patch

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Christoph Erhardt <fedora@sicherha.de> - 1.8.0-1
- Update to 1.8.0 (rhbz#1942544)

* Thu Jul 20 2023 Python Maint <python-maint@redhat.com> - 1.7.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Scott K Logan <logans@cottsay.net> - 1.7.0-1
- Update to 1.7.0 (rhbz#1552355)
- Use OpenDev upstream
- Add manpage

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-2
- Rebuilt for Python 3.9

* Sun Feb 16 2020 Scott K Logan <logans@cottsay.net> - 1.6.0-1
- Update to 1.6.0

* Sun Feb 16 2020 Scott K Logan <logans@cottsay.net> - 0.4.16-1
- Update to 0.4.16
- Add weak dependency on python-kerberos
- Align spec file between Fedora and EPEL
- Use a subpackage for python 2 on EPEL
- Enable python 3 subpackage for EPEL
- Handle automatic dependency generation (f30+)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.15-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.15-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.15-7
- Subpackage python2-jenkins has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.15-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.15-2
- Cleanups in spec

* Wed Jan 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.15-1
- Update to 0.4.15

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Scott K Logan <logans@cottsay.net> - 0.4.14-2
- Work around nose on Fedora as well (LP: #872887)

* Sat May 13 2017 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4.14-1
- Update to 0.4.14 (rhbz#1267414)
- Use HTTPS homepage URL
- New Source0 PyPI URL
- Avoid nose on el7 (LP: #872887)
- BR: python-kerberos to make the tests get a bit further

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.12-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun  7 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4.12-2
- Fix python3 subpackage provides

* Tue Jun  7 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4.12-1
- Upstream 0.4.12
- Update to python guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Aug 25 2015 Scott K Logan <logans@cottsay.net> - 0.4.8-1
- Update to 0.4.8

* Tue Jun 30 2015 Scott K Logan <logans@cottsay.net> - 0.4.7-1
- Update to 0.4.7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Scott K Logan <logans@cottsay.net> - 0.4.5-1
- Update to 0.4.5
- Update to latest python packaging guidelines

* Wed Nov 12 2014 Scott K Logan <logans@cottsay.net> - 0.4.1-1
- Update to 0.4.1 (RHBZ #1162743)
- Switch to PyPI upstream
- Add python3 package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Initial package
