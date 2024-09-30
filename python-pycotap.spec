# Created by pyp2rpm-3.3.2
%global pypi_name pycotap

Name:           python-%{pypi_name}
Version:        1.3.1
Release:        2%{?dist}
Summary:        A tiny test runner that outputs TAP results to standard output

License:        MIT
URL:            https://el-tramo.be/pycotap
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
pycotap is a simple Python test runner for unit tests that outputs Test Anything
Protocol results directly to standard output.Contrary to other TAP runners
for Python, pycotap prints TAP (and *only* TAP) to standard output
instead of to a separate file, allowing you to pipe it directly to TAP pretty
printers and processors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
pycotap is a simple Python test runner for unit tests that outputs Test Anything
Protocol results directly to standard output.Contrary to other TAP runners
for Python, pycotap prints TAP (and *only* TAP) to standard output
instead of to a separate file, allowing you to pipe it directly to TAP pretty
printers and processors.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
find %{buildroot}/%{python3_sitelib} -name '*.py' | xargs sed -i '/^#!/d'
%__rm -f %{buildroot}/usr/COPYING

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Shlomi Fish <shlomif@shlomifish.org> 1.3.1-1
- New upstream release ( https://bugzilla.redhat.com/show_bug.cgi?id=2297455 )

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.0-21
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 21 2023 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.1.0-18
- Mark this as SPDX license expression converted

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.0-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-10
- Rebuilt for Python 3.10

* Sat May 01 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.1.0-9
- Enable CI

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Shlomi Fish <shlomif@shlomifish.org> - 1.1.0-1
- Initial package.
