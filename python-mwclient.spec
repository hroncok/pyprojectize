%global test_requires python3-requests python3-requests-oauthlib python3-six python3-simplejson

%global github_owner    mwclient
%global github_name     mwclient

Name:           python-mwclient
Version:        0.11.0
Release:        1%{?dist}
Summary:        Mwclient is a client to the MediaWiki API

License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/v%{version}.tar.gz
BuildArch:      noarch

%description
mwclient is a lightweight Python client library to the MediaWiki API which
provides access to most API functionality.

%package -n python3-%{github_name}
Summary:        %{summary}
Obsoletes:      python2-%{github_name} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-mock
BuildRequires:  python3-funcsigs
BuildRequires:  python3-responses >= 0.3.0
BuildRequires:  %{test_requires}

Requires:       %{test_requires}

%description -n python3-%{github_name}
%{github_name} is a lightweight Python client library to the MediaWiki API which
provides access to most API functionality. This is the Python 3 build of
%{github_name}.

%prep
%autosetup -p1 -n %{github_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l '%{github_name}*'


%check
%pyproject_check_import

%{__python3} setup.py test

%files -n python3-%{github_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
* Mon Aug 12 2024 Adam Williamson <awilliam@redhat.com> - 0.11.0-1
- Update to 0.11.0
- Simplify spec by dropping EPEL 7 support

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.10.1-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.10.1-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.10.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Adam Williamson <awilliam@redhat.com> - 0.10.1-1
- New release 0.10.1: bugfixes and enhancements

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Adam Williamson <awilliam@redhat.com> - 0.10.0-1
- New release 0.10.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Adam Williamson <awilliam@redhat.com> - 0.9.3-3
- Backport a few patches to remove use of pep8 (being retired)
- Only BuildRequire pytest-cache on EL7, it is part of pytest since

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Adam Williamson <awilliam@redhat.com> - 0.9.3-1
- New release 0.9.3
- Disable Python 2 build on F30+ / RHEL 8+

* Tue Jul 31 2018 Adam Williamson <awilliam@redhat.com> - 0.9.1-1
- New release 0.9.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Adam Williamson <awilliam@redhat.com> - 0.9.0-1
- New release 0.9.0
- Version the python2 requires (except one)
- Enable tests on EPEL 7+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Adam Williamson <awilliam@redhat.com> - 0.8.7-1
- New release 0.8.7
- Drop PR #177 patch, merged upstream

* Thu Nov 16 2017 Adam Williamson <awilliam@redhat.com> - 0.8.6-1
- New release 0.8.6
- Backport PR #177 to restore compatibility with older responses

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 17 2017 Adam Williamson <awilliam@redhat.com> - 0.8.4-1
- New release 0.8.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-2
- Rebuild for Python 3.6

* Mon Dec 05 2016 Adam Williamson <awilliam@redhat.com> - 0.8.3-1
- new release 0.8.3 (note: no EL 6 from now on, upstream dropped Python 2.6)
- drop patch merged upstream
- update requirements
- enable tests on F23 (python-funcsigs update went stable)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 29 2016 Adam Williamson <awilliam@redhat.com> - 0.8.1-2
- re-add a patch which it turns out wasn't merged upstream yet

* Mon Feb 29 2016 Adam Williamson <awilliam@redhat.com> - 0.8.1-1
- new release 0.8.1
- drop patches merged upstream

* Tue Feb 16 2016 Adam Williamson <awilliam@redhat.com> - 0.8.0-3
- enable tests on Fedora > 23 (deps now available)

* Wed Feb 03 2016 Adam Williamson <awilliam@redhat.com> - 0.8.0-2
- fix an iterator problem with Python 3 (upstream PR #108)

* Thu Jan 21 2016 Adam Williamson <awilliam@redhat.com> - 0.8.0-1
- new release 0.8.0
- split into python2 and python3 builds (0.8.0 adds py3 support)

* Fri Aug 07 2015 Adam Williamson <awilliam@redhat.com> - 0.7.2-1
- new release 0.7.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 12 2014 Adam Williamson <awilliam@redhat.com> - 0.7.1-1
- new release 0.7.1, bit of spec cleaning

* Fri Oct 31 2014 Adam Williamson <awilliam@redhat.com> - 0.7.0-2
- requires python-requests

* Wed Oct 01 2014 Adam Williamson <awilliam@redhat.com> - 0.7.0-1
- new release: 0.7.0
- update for github source, use of setuptools and modern Python packaging rules

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Robert Scheck <robert@fedoraproject.org> - 0.6.5-1
- Upgrade to 0.6.5 (#714302)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Sep 22 2009 Steven M. Parrish <smparrish@gmail.com> - 0.6.3-3
- Fix patch

* Sun Sep 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.6.3-2
- upstream wmf patch
- %%doc README.txt
- use %%global (instead of %%define)

* Tue Sep 15 2009  Steven M. Parrish <smparrish@gmail.com> - 0.6.3-1
- Initial build
