Name:           python-resultsdb_api
# NOTE: if you update version, *make sure* to also update `setup.py`
Version:        2.1.5
Release:        14%{?dist}
Summary:        Interface api to ResultsDB

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pagure.io/taskotron/resultsdb_api
Source0:        https://qa.fedoraproject.org/releases/resultsdb_api/resultsdb_api-%{version}.tar.gz

# https://pagure.io/taskotron/resultsdb_api/pull-request/14
# Fixes a bug that broke things completely on F<=34
Patch0:         0001-Fix-Retry-allowed-methods-for-urllib-1.25.patch

BuildArch:      noarch

%description
Interface api to ResultsDB

%package -n python3-resultsdb_api
Summary: %summary
Requires:       python3-simplejson
Requires:       python3-requests

BuildRequires:  python3-devel
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-simplejson
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-virtualenv

%description -n python3-resultsdb_api
Python3 interface to resultsdb.

%prep
%autosetup -p1 -n resultsdb_api-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l resultsdb_api

%check
%pyproject_check_import

%pytest

%files -n python3-resultsdb_api -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.5-14
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.5-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.1.5-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.5-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 19 2021 Adam Williamson <awilliam@redhat.com> - 2.1.5-3
- Update the patch from -2 to *really* fix the problem

* Fri Nov 19 2021 Adam Williamson <awilliam@redhat.com> - 2.1.5-2
- Fix Retry allowed methods for urllib 1.25 (F34 and earlier)

* Sun Nov 14 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.5-1
- Drop use of deprecated Retry parameter
- Drop unnecessary `_KEEP` and just `None` instead
- Make tox work (just runs pytest for now)
- Port tests to unittest.mock and ResultsDB API v2 (#1)
- Simplify update_testcase
- update_testcase: fix variable name
- ResultsDBAuth: it's `@staticmethod`, not `@static_method`
- Drop Python 2 string type blob
- Enable tests during the rpm build

* Sun Nov 14 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.4-3
- Revert backported patch for auth code

* Thu Nov 11 2021 Adam Williamson <awilliam@redhat.com> - 2.1.4-2
- Backport patch to fix critical error in auth code

* Mon Nov 08 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.4-1
- add auth class with basic http auth support

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.3-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.3-8
- Drop BR: git

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.3-1
- Fix 'RetryError' object has no attribute 'message'

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.2-4
- Drop Python 2 subpackage
- Clean spec
- Update Source0 url

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.2-1
- Python 3 subpacakage for Fedora
- Drop dependency on python-six

* Fri Apr 06 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.1-1
- Fix the python.six interaction with non-string inputs

* Wed Mar 28 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.0-1
- Add support for auth token
- Retry on HTTP 500 errors by default
- py3: Updates to work with Python 3

* Mon Feb 19 2018 Steve Milner <smilner@redhat.com> - 2.0.1-1
- Added six to support py2/py3 changes in the source.

* Thu Feb 08 2018 Kamil Páral <kparal@redhat.com> - 2.0.0-9
- fix yet another dependency issue for EPEL

* Mon Feb 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-8
- Fix condition for EPEL

* Mon Feb 05 2018 Kamil Páral <kparal@redhat.com> - 2.0.0-7
- Fix deps for EPEL

* Fri Feb 02 2018 Kamil Páral <kparal@redhat.com> - 2.0.0-6
- Accomodate deps for F27 and older

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.0-4
- Python 2 binary package renamed to python2-resultsdb_api
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Kamil Páral <kparal@redhat.com> - 2.0.0-1
- fix like: filter
- synchronize major version number with resultsdb major number
- disable the test suite until it is fixed

* Thu Nov 3 2016 Tim Flink <tflink@fedoraproject.org> - 1.3.0-1
- add support for resultsdb 2.0

* Wed May 25 2016 Martin Krizek <mkrizek@redhat.com> - 1.2.2-3
- remove not needed custom python_sitelib macro

* Tue May 24 2016 Martin Krizek <mkrizek@redhat.com> - 1.2.2-2
- rename to python-resultsdb_api (obsolete resultsdb_api)
- add python_provide
- add LICENSE file
- add check

* Wed Jul 8 2015 Martin Krizek <mkrizek@redhat.com> - 1.2.2-1
- Remove trailing slashes from url before it's used
- Add missing python-simplejson dependency

* Thu Apr 9 2015 Tim Flink <tflink@fedoraproject.org> - 1.2.1-1
- added option for retrieving job data after update_job (T456)

* Wed Apr 1 2015 Tim Flink <tflink@fedoraproject.org> - 1.2.0-1
- added logging capability, logging response errors
- added UUID support for execdb integration

* Fri May 16 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.0-1
- Releasing resultsdb_api 1.1.0

* Fri Apr 25 2014 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- bugfixes from upstream

* Fri Apr 11 2014 Tim Flink <tflink@fedoraproject.org> - 1.0.1-1
- initial packaging
