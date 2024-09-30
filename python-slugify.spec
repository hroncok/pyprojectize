%global pypi_name slugify

Name:           python-slugify
Version:        6.1.2
Release:        9%{?dist}
Summary:        Python module to deal with unicode slugs

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/un33k/python-slugify
Source0:        %{url}/archive/v%{version}/python-%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
A Python slugify application that handles Unicode.

%package -n python3-%{pypi_name}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  python3-text-unidecode

%description -n python3-%{pypi_name}
A Python slugify application that handles Unicode.

%prep
%autosetup -n python-%{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%{__python3} test.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/%{pypi_name}

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 6.1.2-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 6.1.2-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 6.1.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Fabian Affolter <mail@fabian-affolter.ch> - 6.1.2-1
- Update to latest upstream release 6.1.2 (closes rhbz#2119939)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0.1-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.1-1
- Update to latest upstream release 4.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.0-1
- Update to latest upstream release 4.0.0

* Fri Oct 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.6-1
- Update to latest upstream release 3.0.6

* Sat Sep 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.4-1
- Update to latest upstream release 3.0.4

* Wed Sep 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.3-1
- Update to latest upstream release 3.0.3

* Tue Sep 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.2-4
- python-text-unidecode is now available (rhbz#1725788)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.2-1
- Update to latest upstream release 3.0.2
- Use upstream source, enable tests and add documentation

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-2
- Subpackage python2-slugify has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Nov 11 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 1.2.6-1
- Update to v1.2.6
- Use %%pypi_source macro

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 William Moreno <williamjmorenor@gmail.com> - 1.2.1-1
- Update to v1.2.1
- Update source url

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.2.0
- Update to 1.2.0 (switching to sources from new upstream)
- Add Python 3 support

* Thu Sep 17 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 0.0.1-7
- Update python macros

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 William José Moreno Reyes <williamjmorenor at gmail.com> - 0.0.1-5
- Fix %%Requires

* Thu Dec 25 2014 William Moreno Reyes < williamjmorenor at gmail.com> - 0.0.1.4
- Fix %%license macro

* Sun Dec 07 2014 William Moreno Reyes < williamjmorenor at gmail.com> - 0.0.1-3
- Add %%license macro

* Mon Oct 27 2014 William José Moreno Reyes <williamjmorenor at gmail.com> - 0.0.1-2
- Patching Licence

* Mon Oct 20 2014 William José Moreno Reyes <williamjmorenor at gmail.com> - 0.0.1-1
- Initial package.
