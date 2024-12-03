%global srcname edgegrid-python

Summary: {OPEN} client authentication protocol for python-requests
Name: python-edgegrid
Version: 1.2.1
Release: 12%{?dist}
Source0: %{pypi_source}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
BuildArch: noarch
URL: https://github.com/akamai-open/AkamaiOPEN-edgegrid-python

%description
This library implements an Authentication handler for requests
that provides the Akamai {OPEN} Edgegrid Authentication scheme.

%package -n python3-edgegrid
Summary:	%{summary}
BuildRequires:	python3-devel

# Dependencies for tests
BuildRequires:	python3dist(requests)


%description -n python3-edgegrid
This library implements an Authentication handler for requests
that provides the Akamai {OPEN} Edgegrid Authentication scheme.

%prep
%autosetup -n %{srcname}-%{version}

# Sources currently have some useless shebangs, and rpmlint
# doesn't like that.
# https://github.com/akamai/AkamaiOPEN-edgegrid-python/pull/35
# Let's patch them out for now.
find akamai -name '*.py' -exec sed -r -e 's|^#!/usr/bin/env.*|#|' -i '{}' ';'


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%check
%pyproject_check_import

# upstream uses custom test runner in this module
%{__python3} -m akamai.edgegrid.test.test_edgegrid

%install
%pyproject_install
%pyproject_save_files -l akamai

%files -n python3-edgegrid -f %{pyproject_files}
%doc README.rst

%{python3_sitelib}/edgegrid_python*.pth


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.1-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.1-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Joel Capitao <jcapitao@redhat.com> - 1.2.1-1
- Update to new upstream release 1.2.1 (rhbz#2012768)

* Tue Aug 17 2021 Rohan McGovern <rmcgover@redhat.com> - 1.2.0-1
- New upstream release
- Enable tests in %check

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.1-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Rohan McGovern <rmcgover@redhat.com> - 1.1.1-8
- Explicitly BuildRequires python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Rohan McGovern <rmcgover@redhat.com> - 1.1.1-2
- Ensure all directories owned
- Remove Group tag per guidelines
- Add python_provide per guidelines

* Wed Dec 19 2018 Rohan McGovern <rmcgover@redhat.com> - 1.1.1-1
- Initial RPM release
