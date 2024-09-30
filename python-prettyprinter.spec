# what it's called on pypi
%global srcname prettyprinter
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Syntax-highlighting, declarative and composable pretty printer.  Drop in
replacement for the standard library pprint: just rename pprint to
prettyprinter in your imports.  Uses a modified Wadler-Leijen layout algorithm
for optimal formatting.  Write pretty printers for your own types with a dead
simple, declarative interface.}

%if 0%{?fedora} >= 31
# tests are incompatible with hypothesis 4
# https://github.com/tommikaikkonen/prettyprinter/issues/53
%bcond_with tests
%else
%bcond_without tests
%endif


Name:           python-%{pkgname}
Version:        0.17.0
Release:        20%{?dist}
Summary:        Syntax-highlighting, declarative and composable pretty printer
License:        MIT
URL:            https://github.com/tommikaikkonen/prettyprinter
Source0:        %pypi_source
# avoid build requirement on pytest-runner
Patch0:         remove-setup-requires.patch
# test relies on a pinned requests version user-agent
Patch1:         allow-failure-with-different-requests-versions.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1642003
Patch2:         allow-failure-with-system-wide-timezone-database.patch
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-requests
BuildRequires:  python3-attrs
BuildRequires:  python3-ipython
BuildRequires:  python3-pytz
BuildRequires:  python3-numpy
BuildRequires:  python3-colorful >= 0.4.0
BuildRequires:  python3-pygments >= 2.2.0
%endif
Requires:       python3-colorful >= 0.4.0
Requires:       python3-pygments >= 2.2.0


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -rf %{eggname}.egg-info

# tests are incompatible with django 2
# https://github.com/tommikaikkonen/prettyprinter/issues/54
rm -r tests/test_django


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose tests
%endif


%files -n python3-%{pkgname}
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}.dist-info


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.17.0-19
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.17.0-15
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.17.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.17.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 06 2019 Carl George <carl@george.computer> - 0.17.0-1
- Initial package
