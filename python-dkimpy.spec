# Created by pyp2rpm-3.3.4
%global pypi_name dkimpy

# Tests are missing from pypi tarball
%bcond_with check

Name:           python-%{pypi_name}
Version:        1.0.5
Release:        14%{?dist}
Summary:        DKIM, ARC, and TLSRPT email signing and verification

License:        zlib
URL:            https://launchpad.net/dkimpy
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiodns)
BuildRequires:  python3dist(authres)
BuildRequires:  python3dist(dnspython) >= 1.16
BuildRequires:  python3dist(pynacl)

%description
dkimpy is a library that implements DKIM (DomainKeys Identified Mail)
email signing and verification.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
dkimpy is a library that implements DKIM (DomainKeys Identified Mail)
email signing and verification.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Drop shebang for these files, as we don't need them
sed -e "s|#!/usr/bin/env python||" -i dkim/{arcsign.py,arcverify.py,dkimsign.py,dkimverify.py,dknewkey.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dkim

%if %{with check}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/arcsign
%{_bindir}/arcverify
%{_bindir}/dkimsign
%{_bindir}/dkimverify
%{_bindir}/dknewkey
%{_mandir}/man1/arcsign.1*
%{_mandir}/man1/arcverify.1*
%{_mandir}/man1/dkimsign.1*
%{_mandir}/man1/dkimverify.1*
%{_mandir}/man1/dknewkey.1*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.0.5-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.0.5-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.5-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.5-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.5-1
- Initial package.
