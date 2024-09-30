%global pypi_name conu

Name:           %{pypi_name}
Version:        0.7.1
Release:        24%{?dist}
Summary:        library which makes it easy to write tests for your containers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/fedora-modularity/conu
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
# exclude ppc64 because there is no moby-engine package
# https://bugzilla.redhat.com/show_bug.cgi?id=1547049
ExcludeArch:    ppc64

# for docs

%description
`conu` is a library which makes it easy to write tests for your containers
and is handy when playing with containers inside your code.
It defines an API to access and manipulate containers,
images and provides more, very helpful functions.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-kubernetes
BuildRequires:  python3-docker
BuildRequires:  python3-requests
BuildRequires:  python3-pyxattr
BuildRequires:  python3-six
Requires:       python3-kubernetes
Requires:       python3-docker
Requires:       python3-requests
Requires:       python3-pyxattr
Requires:       python3-six
# these are optional but still recommended
Recommends:     moby-engine
Recommends:     source-to-image
Recommends:     acl
Recommends:     libselinux-utils

%description -n python3-%{pypi_name}
`conu` is a library which makes it easy to write tests for your containers
and is handy when playing with containers inside your code.
It defines an API to access and manipulate containers,
images and provides more, very helpful functions.

%package -n     python3-%{pypi_name}-pytest
Summary:        fixtures which can be utilized via pytest
Requires:       python3-pytest
Requires:       python3-%{pypi_name}

%description -n python3-%{pypi_name}-pytest
fixtures which can be utilized via pytest

%package -n %{pypi_name}-doc
Summary:        conu documentation
BuildRequires:  python3-sphinx

%description -n %{pypi_name}-doc
Documentation for conu.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="${PWD}:${PWD}/docs/" sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.dist-info/
%exclude %{python3_sitelib}/tests
%exclude %{python3_sitelib}/fixtures

%files -n python3-%{pypi_name}-pytest
%license LICENSE
%{python3_sitelib}/%{pypi_name}/fixtures/

%files -n %{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.1-24
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.7.1-22
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.7.1-18
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.7.1-15
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.1-12
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Lukas Slebodnik <lslebodn@fedoraproject.org> - 0.7.1-4
- Change weak dependency in rawhide (docker -> moby-engine)

* Wed May 01 2019 Lukas Slebodnik <lslebodn@fedoraproject.org> - 0.7.1-3
- rhbz#1677664 - Remove hard dependency on docker

* Thu Feb 28 2019 Jiri Popelka <jpopelka@redhat.com> - 0.7.1-2
- remove Python 2 support

* Wed Feb 27 2019 Radoslav Pitoňák <rado.pitonak@gmail.com> 0.7.1-1
- 0.7.1 release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Tomas Tomecek <ttomecek@redhat.com> 0.7.0-1
- 0.7.0 release

* Mon Jan 21 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.6.2-2
- packaging fixes

* Thu Nov 15 2018 Tomas Tomecek <ttomecek@redhat.com> 0.6.2-1
- 0.6.2 release

* Wed Nov 14 2018 lachmanfrantisek <lachmanfrantisek@gmail.com> 0.6.1-1
- 0.6.1 release

* Wed Oct 24 2018 Radoslav Pitoňák <rado.pitonak@gmail.com> 0.6.0-1
- 0.6.0 release

* Thu Sep 13 2018 Radoslav Pitonak <rado.pitonak@gmail.com> - 0.5.0-2
- add dependency kubernetes 

* Thu Sep 13 2018 Radoslav Pitonak <rado.pitonak@gmail.com> - 0.5.0-1
- New upstream release 0.5.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.7

* Fri May 25 2018 Tomas Tomecek <ttomecek@redhat.com> - 0.4.0-1
- New upstream release 0.4.0

* Wed May 02 2018 Tomas Tomecek <ttomecek@redhat.com> - 0.3.1-1
- New upstream release 0.3.1

* Thu Feb 01 2018 Tomas Tomecek <ttomecek@redhat.com> 0.2.0-1
- 0.2.0 release

* Wed Dec 06 2017 Tomas Tomecek <ttomecek@redhat.com> - 0.1.0-1
- Initial package.
