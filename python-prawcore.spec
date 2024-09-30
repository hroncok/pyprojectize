%global pypi_name prawcore

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        12%{?dist}
Summary:        Low-level communication layer for PRAW 4+ library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/praw-dev/prawcore
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Low-level communication layer for PRAW 4+ library.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  mock
BuildRequires:  python3-mock
BuildRequires:  python3-betamax
BuildRequires:  python3-betamax-matchers
BuildRequires:  python3-betamax-serializers
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-testfixtures
%py_provides    python3-nng

%description -n python3-%{pypi_name}
Low-level communication layer for PRAW 4+ library.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGES.rst README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.0-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 2.3.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-1
- Update to latest upstream release 2.3.0
- Fix FTO (rhbz#1969084)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.10

* Fri Feb 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update to latest upstream release 2.0.0

* Wed Feb 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update to latest upstream release 1.5.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to latest upstream release 1.4.0

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.9

* Sat May 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-2
- Disable tests

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Initial package for Fedora
