%global srcname mailmerge
%{?python_enable_dependency_generator}

Name:          python-%{srcname}
Version:       2.2.1
Release:       11%{?dist}
Summary:       Simple command line mail merge tool

License:       MIT
URL:           https://github.com/awdeorio/mailmerge
Source0:       %{pypi_source}
BuildArch:     noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:       %{summary}
Provides:      %{srcname} = %{version}-%{release}
BuildRequires: python3-devel

%description -n python3-%{srcname}
%{summary}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l mailmerge

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/mailmerge

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.1-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.1-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild


* Fri Oct 8 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.2.1-1
- 2.2.1 and patch removed.

* Thu Oct 7 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.2.0-1
- 2.2.0 and 0001-Update-setup.py.patch added.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Brian Exelbierd <bexelbie@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Brian Exelbierd <bexelbie@redhat.com> - 2.1-1
- Remove configparser dependency

* Thu Apr 23 2020 Brian Exelbierd <bexelbie@redhat.com> - 2.1-1
- Update to 2.1.0
- remove merged patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 Brian Exelbierd <bexelbie@redhat.com> - 1.9-2
- Adding Patch for F30 backports-csv drop

* Thu May 16 2019 Brian Exelbierd <bexelbie@redhat.com> - 1.9-1
- Initial package
