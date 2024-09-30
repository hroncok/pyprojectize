%{?python_enable_dependency_generator}
%global pypi_name ModulemdTranslationHelpers

Name:           python-%{pypi_name}
Version:        0.6
Release:        22%{?dist}
Summary:        Tools for working with translations of modulemd

License:        MIT
URL:            https://github.com/fedora-modularity/ModulemdTranslationHelpers
Source0:        %{pypi_source}

BuildArch:      noarch

%description
Provides a library and tools for dealing with translatable strings in modulemd
documents.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       libmodulemd
Requires:       python%{python3_version}dist(pygobject)

Obsoletes:      python3-mmdzanata < 0.7-3
Obsoletes:      python2-mmdzanata < 0.7-3

%description -n python3-%{pypi_name}
Provides a library and tools for dealing with translatable strings in modulemd
documents.


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


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/ModulemdTranslationHelpers


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6-21
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.6-2
- Drop manpage

* Tue Oct 16 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.6-1
- Update to 0.6
- Drop dependency on python3-koji
- Switch to proper python logging
- Support reading .po files from directories other than CWD
- Drop manpage

* Wed Oct 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5-4
- Random fixes in packaging

* Mon Oct 01 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.5-3
- Drop Python 2 subpackage

* Wed Sep 26 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.5-2
- Fixes to the specfile

* Tue Sep 25 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.5-1
- Fixes from code review

* Tue Sep 25 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.3-1
- Initial package
