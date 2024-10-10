%global pypi_name listparser

Name:           python-%{pypi_name}
Version:        0.18
Release:        23%{?dist}
Summary:        Parse OPML, FOAF, and iGoogle subscription lists

License:        LGPL-3.0-or-later
URL:            https://github.com/kurtmckee/listparser
Source0:        %pypi_source
BuildArch:      noarch
Patch0:         2to3.patch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx)

%description
listparser is a Python library that parses subscription lists (also called
reading lists) and returns all of the feeds, subscription lists, and
"opportunity" URLs that it finds. It supports OPML, RDF+FOAF, and the iGoogle
exported settings format.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
listparser is a Python library that parses subscription lists (also called
reading lists) and returns all of the feeds, subscription lists, and
"opportunity" URLs that it finds. It supports OPML, RDF+FOAF, and the iGoogle
exported settings format.

%package -n python-%{pypi_name}-doc
Summary:        listparser documentation
%description -n python-%{pypi_name}-doc
Documentation for listparser.

%prep
%autosetup -n %{pypi_name}-%{version} -p0
chmod 644 COPYING
chmod 644 COPYING.LESSER
chmod 644 README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

#%check
#%{__python3} lptest.py test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n python-%{pypi_name}-doc
%license COPYING COPYING.LESSER
%doc html

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.18-22
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.18-18
- Rebuilt for Python 3.12

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.18-17
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.18-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.18.12
- Disable tests fox 3.11. Upstream has a fix but no new release,
- and major changes in between.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.18.10
- Fix build for Sphinx 4.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.18-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18-3
- Initial package
