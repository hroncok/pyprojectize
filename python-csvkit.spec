%{?python_enable_dependency_generator}
%global pypi_name csvkit
%global project_owner wireservice
%global github_name csvkit
%global desc csvkit is a suite of utilities for converting to and working with CSV, the king \
of tabular file formats.


Name:           python-%{pypi_name}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Suite of utilities for converting to and working with CSV

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/wireservice/csvkit/archive/%{version}/csvkit-%{version}.tar.gz

BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist agate} >= 1.6.1
BuildRequires:  %{py3_dist agate-excel} >= 0.2.2
BuildRequires:  %{py3_dist agate-dbf} >= 0.2
BuildRequires:  %{py3_dist agate-sql} >= 0.5.3
BuildRequires:  %{py3_dist six} >= 1.6.1
BuildRequires:  %{py3_dist furo}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%package doc
BuildRequires:  python-sphinx-doc
BuildRequires:  python3-sphinx_rtd_theme
Summary:        %{summary}

%description doc
%{desc}

Documentation package

%prep
%setup -q -n %{github_name}-%{version}
rm -rf *.egg-info
# Fix non-executable-script
find csvkit -name \*.py -type f | xargs sed -i '1{\@^#!/usr/bin/env python@d}'


%build
%py3_build

cd docs
make html
make man


%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man1
for file in docs/_build/man/*.1; do
    install -p -m0644 ${file} %{buildroot}%{_mandir}/man1/
done

# Remove unuseful files in doc
rm docs/_build/html/.buildinfo

# Correct permissions in doc
chmod -x examples/realdata/census_2000/VROUTFSJ.TXt


%check
# This tests fails because of local error.
pytest-%{python3_version} tests -v -k "not test_convert_dbf and not test_decimal_format"

%files -n python3-%{pypi_name}
%license COPYING
%doc README.rst CHANGELOG.rst AUTHORS.rst
%{_bindir}/*
%{_mandir}/man1/*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{pypi_name}/


%files doc
%license COPYING
%doc README.rst CHANGELOG.rst AUTHORS.rst docs/_build/html examples


%changelog
* Thu Aug 22 2024 Julien Enselme <jujens@jujens.eu> - 2.0.1-1
- Update to 2.0.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 22 2024 Julien Enselme <jujens@jujens.eu> - 2.0.0-1
- Update to 2.0.0

* Sat Jun 15 2024 Python Maint <python-maint@redhat.com> - 1.1.1-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.12

* Tue Apr 25 2023 Julien Enselme <jujens@jujens.eu> - 1.1.1-1
- Update to 1.1.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Julien Enselme <jujens@jujens.eu> - 1.1.0-1
- Update to 1.1.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Julien Enselme <jujens@jujens.eu> - 1.0.7-2
- Rebuilt for Python 3.11

* Sat Jun 18 2022 Julien Enselme <jujens@jujens.eu> - 1.0.7-1
- Update to 1.0.7

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.4-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-4
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Julien Enselme <jujens@jujens.eu> - 1.0.4-3
- Fix tests for mass rebuild.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Julien Enselme <jujens@jujens.eu> - 1.0.4-1
- Update to 1.0.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-5
- Enable python dependency generator

* Fri Dec 28 2018 Julien Enselme <jujens@jujens.eu> - 1.0.3-4
- Remove Python 2 subpackage.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Julien Enselme <jujens@jujens.eu> - 1.0.3-1
- Update to 1.0.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Jan 16 2018 Julien Enselme <jujens@jujens.eu> - 1.0.2-2
- Add missing dependency

* Sun  Oct 15 2017 Julien Enselme <jujens@jujens.eu> - 1.0.2-1
- Update to 1.0.2
- Use the %%{summary} macro
- Use the %%py2_dist and %%py3_dist macros
- Use the version instead of git tag to fetch the source on github

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11.gitbf18815
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10.gitbf18815
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-9.gitbf18815
- Fix XLSX reader

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-8.gitbf18815
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-7.gitbf18815
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 11 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-6.gitbf18815
- Correct typo in comment

* Sat Feb 6 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-5.gitbf18815
- Correct some rpmlint warnings

* Sun Jan 24 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-4.gitbf18815
- Correct build on rawhide.

* Sun Jan 24 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-3.gitbf18815
- Move unversionned binaries to python2 subpackage.

* Wed Nov 25 2015 Julien Enselme <jujens@jujens.eu> - 0.9.1-2.gitbf18815
- Add python-enum34 to the Requires for python 2 subpackage

* Mon Nov 9 2015 Julien Enselme <jujens@jujens.eu> - 0.9.1-1.gitbf18815
- Inital package
