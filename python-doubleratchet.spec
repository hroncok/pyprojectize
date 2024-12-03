Name:           python-doubleratchet
Version:        1.0.4
Release:        1%{?dist}
Summary:        Python implementation of the Double Ratchet algorithm

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-cryptography
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pydantic

%description
This python library offers an implementation of the Double Ratchet
algorithm.

A double ratchet allows message encryption providing perfect forward
secrecy. A double ratchet instance synchronizes with a second instance
using Diffie-Hellman calculations, that are provided by the DHRatchet
class.



%package     -n python3-doubleratchet
Summary:        Python implementation of the Double Ratchet algorithm

%description -n python3-doubleratchet
This python library offers an implementation of the Double Ratchet
algorithm.

A double ratchet allows message encryption providing perfect forward
secrecy. A double ratchet instance synchronizes with a second instance
using Diffie-Hellman calculations, that are provided by the DHRatchet
class.



%prep
%autosetup -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l doubleratchet


%check
%pyproject_check_import

%pytest



%files -n python3-doubleratchet -f %{pyproject_files}
%doc README.md
# For noarch packages: sitelib



%changelog
* Wed Jul 24 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.13

* Wed May 8 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.3-2
- Remove useless variable in specfile (%%version_main)

* Wed May 1 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- Use %%pytest in %%check section instead of setup.py

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.7.0~beta-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.7.0~beta-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.0~beta-4
- Rebuilt for Python 3.10

* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0~beta-3
- Package Review RHBZ#1917089:
  - Fix the Version tag to match upstream version
  - Use %%{python3_version} in %%files section

* Mon Feb 08 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0-2
- Remove upstream name variable used once: %%{srcname}
- Add more explicit description

* Sat Jan 16 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0-1
- Initial package
