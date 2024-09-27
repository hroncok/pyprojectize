Summary:       A set of scripts to work locally on subversion checkouts using mercurial
Name:          hgsvn
Version:       0.6.0
Release:       16%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://pypi.python.org/pypi/hgsvn/
Source0:       https://files.pythonhosted.org/packages/source/h/hgsvn/hgsvn-%{version}.tar.gz
BuildArch:     noarch
Requires:      mercurial >= 1.4.3
Requires:      subversion
Requires:      python3-hglib
Requires:      python3-setuptools
# Needed in %%check
BuildRequires: mercurial >= 1.4.3
BuildRequires: python3-devel
BuildRequires: python3-hglib
BuildRequires: python3-nose
BuildRequires: subversion

%description
This set of scripts allows to work locally on subversion managed
projects using the mercurial distributed version control system.

Why use mercurial? You can do local (disconnected) work, pull the
latest changes from the subversion server, manage private branches,
submit patches to project maintainers, etc. And of course you have
fast local operations like hg log and hg annotate.

%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}

%check
%{__python3} setup.py test || :

%files
%license COPYING.txt
%doc AUTHORS.txt README.txt TODO.txt
%{_bindir}/hgimportsvn
%{_bindir}/hgpullsvn
%{_bindir}/hgpushsvn
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.dist-info

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.0-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.0-14
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.6.0-10
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.6.0-7
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.6.0-1
- 0.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.5.2-1
- 0.5.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuild for Python 3.6

* Sat Oct 29 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.5.1-1
- 0.5.1

* Sun Oct 09 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.5.0-1
- 0.5.0

* Fri Oct 07 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.4.1-1
- 0.4.1
- Use Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.15-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Mar 13 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.3.15-1
- 0.3.15

* Sat Mar 05 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.3.14-1
- 0.3.14

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.3.13-1
- 0.3.13

* Thu Nov 26 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.3.12-1
- 0.3.12

* Tue Oct 13 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.3.11-2
- Add hotfix patch from upstream
- Add patch to fall back to simple lock

* Sat Oct 10 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.3.11-1
- 0.3.11

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.3-3
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 20 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.2.3-1
- 0.2.3

* Tue Nov 19 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.2.1-0.1.dev-1
- 0.2.1.dev

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.1.9-5
- Add patch to fix remove issue (bz #963320)

* Sun Feb 24 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.1.9-4
- Add patch to fix subversion 1.7 issue

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.1.9-1
- Update to 0.1.9
- With mercurial >= 1.4.3 license issue is resolved

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Mar 04 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.1.8-1
- Update to 0.1.8

* Sun Nov 01 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.1.7-1
- Update to 0.1.7
- Fix license issue (bz #531456)
 
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.6-2
- Rebuild for Python 2.6

* Fri Aug 22 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.1.6-1
- 0.1.6
- tests are broken, disable %%check

* Sat Feb 16 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.1.5-3
- Add setuptools to req, (Ian Burrell, bz #433050)

* Sun Jan 27 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.1.5-2
- Add %%check section and build req as needed
- Add req on mercurial and subversion

* Fri Jan 25 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.1.5-1
- Initial build
