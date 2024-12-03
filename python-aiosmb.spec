%global pypi_name aiosmb

Name:           python-%{pypi_name}
Version:        0.2.35
Release:        13%{?dist}
Summary:        Asynchronous SMB protocol implementation

License:        MIT
URL:            https://github.com/skelsec/aiosmb
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Fully asynchronous SMB library written in pure Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Fully asynchronous SMB library written in pure Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
rm -rf external
# Remove shebang
sed -i -e '/^#!\//, 1d' aiosmb/{authentication/spnego/asn1_structs.py,\
authentication/spnego/native.py,authentication/spnego/sspi.py,\
commons/connection/target.py,crypto/pure/RC4/RC4.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
# Missing license file: https://github.com/skelsec/aiosmb/pull/4
#%license LICENSE
%{_bindir}/asmbclient
%{_bindir}/asmbshareenum
%{_bindir}/asmbprotocolenum
%{_bindir}/asmbosenum
%{_bindir}/asmbgetfile

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.35-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.35-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.35-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.35-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.35-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.35-2
- Rebuilt for Python 3.10

* Thu Mar 18 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.35-1
- Update to latest upstream release 0.2.35 (#1938605)

* Mon Mar 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.34-1
- Update to latest upstream release 0.2.34 (#1926509)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.33-1
- Update to latest upstream release 0.2.33 (#1902133)

* Fri Oct 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.32-1
- Update to latest upstream release 0.2.32 (#1891357)

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.31-1
- Update to latest upstream release 0.2.28 (#1891357)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.28-1
- Update to latest upstream release 0.2.28 (#1882047)

* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.27-1
- Update to latest upstream release 0.2.27 (#1879298)

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.26-1
- Update to latest upstream release 0.2.26

* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.20-1
- Update to latest upstream release 0.2.20

* Sun Apr 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.10-1
- Initial package for Fedora

