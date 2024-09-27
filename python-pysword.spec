%global srcname pysword
%global sum Open source python API wrapper for Sword Bible files
%global desc %{expand: A native Python reader of the SWORD Project Bible Modules.
Reads SWORD bible files (not commentaries etc.)
Detection of locally installed Swrod bible modules.
Supports all known SWORD module formats (ztext, ztext4, rawtext, rawtext4)
Read from zipped modules, like those available from
http://www.crosswire.org/sword/modules/ModDisp.jsp?modType=Bibles
Cleans the extracted text of OSIS, GBF or ThML tags. 
Supports both python 2 and 3 (tested with 2.7 and 3.5) }

Summary: %{sum}
Name: python-%{srcname}
Version: 0.2.8
Release: 10%{?dist}
Source0: https://gitlab.com/tgc-dk/%{srcname}/repository/archive.tar.gz?ref=%{version}#/%{srcname}-%{version}.tar.gz
Source1: testdata-0.2.8.tar.gz
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
BuildArch: noarch

URL: https://gitlab.com/tgc-dk/pysword

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
# Remove this in Fedora 38:
Obsoletes:      python-%{srcname} < 0.2.7-7

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}
%autosetup -N -T -D -a 1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pysword/
%{python3_sitelib}/pysword-%{version}.dist-info/

%changelog
* Thu Aug 22 2024 Tim.Bentley <tim.bentley@openlp.org> - 0.2.8-10
- Remove unneeded macro

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.8-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.8-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.8-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 07 2022 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.8-1
- Resolve build issues and versions.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.7-9
- Rebuilt for Python 3.11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.7-9
- Rebuilt for Python 3.11

* Sun May 29 2022 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.7-0
- Updated to match upstream release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-7
- Don't own /usr/lib/python3.X/site-packages
- Rename the built package from python-pysword to python3-pysword

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.7-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Tim Bentley <Tim.Bentley@openlp.org>  - 0.2.7-0
- Upstream release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-7
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Tim Bentley <Tim.Bentley@openlp.org>  - 0.2.6-0
- Upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-3
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.5-2
- 0.2.5 Release repackage

* Fri Mar 23 2018 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.5-1
- 0.2.5 Release repackage

* Sat Mar 17 2018 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.4-1
- 0.2.4 Release repackage

* Sun Feb 11 2018 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.3-1
- 0.2.3 Release repackage

* Sat Nov 26 2016 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.3-0
- 0.2.3 Release   
