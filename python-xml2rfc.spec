%global srcname %(echo %{name} | sed 's/^python-//')

Name:           python-xml2rfc
Version:        3.9.1
Release:        12%{?dist}
Summary:        Convert IETF RFC-7749 XML into txt format

# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
URL:            https://pypi.python.org/pypi/xml2rfc/
Source0:        https://files.pythonhosted.org/packages/source/x/xml2rfc/xml2rfc-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Xml2rfc generates RFCs and IETF drafts from document source in XML
according to the dtd in RFC-7749.  It takes as input an xml file which
contains the text and meta-information about author names etc., and
transforms it into suitably formatted output. The input xml file should
follow the DTD given in RFC-7749 (or successor). }

%description %_description

%package -n python3-%{srcname}
Summary: Convert IETF RFC-2629 XML into txt format
BuildRequires:  python3-devel
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
Requires: python3-google-i18n-address
Requires: python3-appdirs
Requires: python3-configargparse
Requires: python3-pyflakes
Requires: python3-html5lib
Requires: python3-intervaltree
Requires: python3-pycountry
Requires: python3-jinja2

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
# temp workaround, filed bug upstream: https://trac.ietf.org/trac/xml2rfc/ticket/661#ticket
sed -i "s/jinja2>=2.11,<3.0/jinja2>=2.11/" requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
# fails on AssertionError: 'Noto Sans Cherokee' not found
#%{python3} setup.py test

%install
%pyproject_install

%files -n python3-%{srcname}
%license PKG-INFO
%doc changelog README
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.dist-info/
%{_bindir}/xml2rfc

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.9.1-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.9.1-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.9.1-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.9.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 28 2021 Paul Wouters <paul.wouters@aiven.io> - 3.9.1-1
- Update to 3.9.1
- Resolves: rhbz#1983367 F35FailsToInstall: python3-xml2rfc

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.7.0-2
- Rebuilt for Python 3.10

* Mon May 17 2021 Paul Wouters <paul.wouters@aiven.io> - 3.7.0-1
- Resolves: rhbz#1830688 FTI: python-xml2rfc: python3-xml2rfc
- Resolves: rhbz#1770860 python3-xml2rfc fails to install in Fedora rawhide

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 11:52:49 EDT 2020 Paul Wouters <pwouters@redhat.com> - 3.2.1-1
- Updated to 3.2.1
- Fixup changelog anomaly

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Paul Wouters <pwouters@redhat.com> - 2.44.0-1
- updated to 2.44.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.22.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.22.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.22.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Paul Wouters <pwouters@redhat.com> - 2.22.3-1
- Updated to 2.22.3

* Tue Feb 12 2019 Paul Wouters <pwouters@redhat.com> - 2.18.0-1
- Updated to 2.18.0 (hopefully get https links on rfc generation now)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5.2-8
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.5.2-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Paul Wouters <pwouters@redhat.com> - 2.5.2-2
- Resolves: rhbz#1444858 xml2rfc: no xml2rfc executable is present

* Tue Apr 04 2017 Paul Wouters <pwouters@redhat.com> - 2.5.2-1
- Updated to 2.5.2
- Resolves rhbz#1438375 xml2rfc: incorrect dependencies
- Resolves rhbz#1323171 Provide a Python3 subpackage
- Enable tests
- Updated source url

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 31 2016 Paul Wouters <pwouters@redhat.com> - 2.5.1-1
- Updated to 2.5.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Paul Wouters <pwouters@redhat.com> - 2.4.2-4
- Fix typo, convert LICENSE to utf-8, check fix and python-setuptools fix

* Sun Sep 01 2013 Paul Wouters <pwouters@redhat.com> - 2.4.2-3
- Patch for paginated_txt.py by Miek, fixes my draft crasher

* Sat Aug 31 2013 Paul Wouters <pwouters@redhat.com> - 2.4.2-2
- Fixup summary, remove cleaning buildroot, remove upstream egg-info
- Added BuildRequire for python-virtualenv to run tests
- Added commented check target - but it has issues to pass
- Fix license to BSD with advertising

* Fri Aug 30 2013 Paul Wouters <pwouters@redhat.com> - 2.4.2-1
- Initial Package
