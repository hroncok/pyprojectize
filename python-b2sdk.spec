Name:           python-b2sdk
Version:        1.21.0
Release:        7%{?dist}
Summary:        Backblaze B2 SDK

License:        MIT
URL:            https://github.com/Backblaze/b2-sdk-python
Source0:        %{pypi_source b2sdk}
BuildArch:      noarch

# Fedora does not ship with version 5 or lower
Patch0:         relax-setuptools_scm-version.patch

%global _description %{expand:
Python library and a few handy utilities for easy access to all of the
capabilities of B2 Cloud Storage.

B2 command-line tool is an example of how it can be used to provide command-line
access to the B2 service, but there are many possible applications (including
FUSE filesystems, storage backend drivers for backup applications etc).}

%description %_description

%package -n python3-b2sdk
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools_scm

%description -n python3-b2sdk %_description

%prep
%autosetup -p1 -n b2sdk-%{version}
rm -rf b2sdk.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
rm -rf %{buildroot}%{python3_sitelib}/test


%files -n python3-b2sdk
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%{python3_sitelib}/b2sdk-*.dist-info/
%{python3_sitelib}/b2sdk/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.21.0-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.21.0-2
- Rebuilt for Python 3.12

* Wed Apr 19 2023 Jonny Heggheim <hegjon@gmail.com> - 1.21.0-1
- Updated to version 1.21.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Jonny Heggheim <hegjon@gmail.com> - 1.18.0-1
- Updated to version 1.18.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.14.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Jonny Heggheim <hegjon@gmail.com> - 1.14.0-1
- Updated to version 1.14.0

* Thu Dec 02 2021 Jonny Heggheim <hegjon@gmail.com> - 1.13.0-1
- Updated to version 1.13.0
- Relax constraint on arrow

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.10

* Mon Apr 05 2021 Jonny Heggheim <hegjon@gmail.com> - 1.4.0-1
- Updated to version 1.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Jonny Heggheim <hegjon@gmail.com> - 0.1.2-1
- Initial package
