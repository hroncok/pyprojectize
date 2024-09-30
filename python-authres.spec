%global srcname authres

Name:           python-%{srcname}
Version:        1.2.0
Release:        22%{?dist}
Summary:        Authentication Results Header Module
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://launchpad.net/authentication-results-python
Source0:	https://launchpad.net/authentication-results-python/1.2/%{version}/+download/%{srcname}-%{version}.tar.gz
Source1:	https://launchpad.net/authentication-results-python/1.2/%{version}/+download/%{srcname}-%{version}.tar.gz.asc
Source2:	https://db.debian.org/fetchkey.cgi?fingerprint=E7729BFFBE85400FEEEE23B178D7DEFB9AD59AF1#/GPG-KEY-kitterman
BuildArch:      noarch
BuildRequires:	gnupg2

%global _description\
RFC 8601 Authentication-Results Headers generation and parsing for\
Python/Python3.  See README for extension RFCs implemented.

%description %_description

%package -n python3-%{srcname}
Summary: %summary
BuildRequires: python3-devel


%description -n python3-%{srcname} %_description

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%{python3} -m authres


%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING
%doc CHANGES README


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.0-20
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.0-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.0-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.9

* Tue May 26 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-6
- Add upstream signature verification

* Sat May 16 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-5
- Rename spec to python-authres.spec

* Mon May 11 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-4
- Remove python2 support from spec for rawhide.  Can add to older branches.

* Fri May  8 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-3
- Add check section, fix reviewer notes, update current RFC, py2 conditional

* Wed May  6 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-2
- Support python2 as well

* Wed May  6 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-1
- Latest upstream release

* Sun Apr 28 2013 Stuart Gathman <stuart@gathman.org> 0.601-1
- When stringifying RFC 5451 property values (pvalue), format them as quoted-
  strings if they contain spaces or special characters (and are not e-mail
  addresses). E.g., IPv6 addresses in policy.iprev properties must be
  double-quoted.
- Fix broken references to quoted_string variable in authres.core.
  AuthenticationResultsHeader._parse_pvalue method. (Closes: LP #1165978)
- Fix erroneous reference to ArgumentError exception to refer to ValueError
  instead. When does the Ruby compatiblity layer for Python come out?
- Added additional tests/examples in authres/tests

* Fri Apr 26 2013 Stuart Gathman <stuart@gathman.org> 0.600-2
- Include fixes for quoting problems

* Fri Apr 26 2013 Stuart Gathman <stuart@gathman.org> 0.600-1
- Update to 0.600, with patches for missing ArgumentError definition.

* Thu Feb 02 2010 Stuart Gathman <stuart@bmsi.com> 0.3-1
- Python-2.6 RPM

