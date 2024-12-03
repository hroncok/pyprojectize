%global srcname pysmi

%{?python_disable_dependency_generator}

Name:           python-smi
Version:        0.3.4
Release:        23%{?dist}
Summary:        A Python implementation of SNMP/SMI MIB parsing and conversion library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/etingof/pysmi
Source0:        %{pypi_source}
BuildArch:      noarch

%description
PySMI is a pure-Python implementation of SNMP SMI MIB parser. This tool is
designed to turn ASN.1 MIBs into various formats. As of this moment, JSON 
and pysnmp modules can be generated from ASN.1 MIBs.

- Understands SMIv1, SMIv2 and de-facto SMI dialects
- Turns MIBs into pysnmp classes and JSON documents
- Maintains an index of MIB objects over many MIB modules
- Automatically pulls ASN.1 MIBs from local directories, ZIP archives, HTTP
  and FTP servers

%package -n python3-smi
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-ply

%description -n python3-smi
PySMI is a pure-Python implementation of SNMP SMI MIB parser. This tool is
designed to turn ASN.1 MIBs into various formats. As of this moment, JSON 
and pysnmp modules can be generated from ASN.1 MIBs.

- Understands SMIv1, SMIv2 and de-facto SMI dialects
- Turns MIBs into pysnmp classes and JSON documents
- Maintains an index of MIB objects over many MIB modules
- Automatically pulls ASN.1 MIBs from local directories, ZIP archives, HTTP
  and FTP servers

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}
mv %{buildroot}%{_bindir}/mibcopy.py %{buildroot}%{_bindir}/mibcopy
mv %{buildroot}%{_bindir}/mibdump.py %{buildroot}%{_bindir}/mibdump

# Tests depend on python3-pysnmp and python3-pysnmp depends on python3-smi.
# This leads to a circular dependency that may cause side-effects.
#%check
#%{__python3} setup.py test

%check
%pyproject_check_import

%files -n python3-smi -f %{pyproject_files}
%doc CHANGES.rst README.md THANKS.txt TODO.txt examples/*.py
%{_bindir}/mibcopy
%{_bindir}/mibdump

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.4-23
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.4-21
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.4-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.4-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.4-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-3
- Disable tests

* Fri May 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-2
- Enable tests

* Sun May 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Initial package for Fedora
