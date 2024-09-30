%global srcname html5-parser

Name:           python-%{srcname}
Version:        0.4.12
Release:        4%{?dist}
Summary:        A fast, standards compliant, C based, HTML 5 parser for python

# html5-parser-0.4.4/gumbo/utf8.c is MIT
# Automatically converted from old format: ASL 2.0 and MIT - review is highly recommended.
License:        Apache-2.0 AND LicenseRef-Callaway-MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconf
# For tests
BuildRequires:  python3-lxml >= 3.8.0
BuildRequires:  gtest-devel
BuildRequires:  python3-chardet
BuildRequires:  python3-beautifulsoup4

%description
A fast, standards compliant, C based, HTML 5 parser for python

%package -n python3-%{srcname}
Summary:        %{summary}

# This package bundles sigil-gumbo a fork of gumbo
# Base project: https://github.com/google/gumbo-parser
# Forked from above: https://github.com/Sigil-Ebook/sigil-gumbo
# It also patches that bundled copy with other changes.
# sigil-gumbo bundled here was added 20170601
Provides:      bundled(sigil-gumbo) = 0.9.3-20170601git0830e1145fe08
# sigil-gumbo forked off gumbo-parser at this commit in 20160216
Provides:      bundled(gumbo-parser) = 0.9.3-20160216git69b580ab4de04

%description -n python3-%{srcname}
A fast, standards compliant, C based, HTML 5 parser for python

%prep
export debug=True
%autosetup -n %{srcname}-%{version} -p1

# remove shebangs from library files
sed -i -e '/^#!\//, 1d' src/html5_parser/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/*

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.12-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.12-2
- Rebuilt for Python 3.13

* Tue Apr 09 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 0.4.12-1
- Update to 0.4.12
- Fixes: rhbz#2186089
- Fixes: rhbz#2261568

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.4.10-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.10-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Kevin Fenzi <kevin@scrye.com> - 0.4.10-1
- Update to 0.4.10. Fixes rhbz#2006688

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.9-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.9-2
- Rebuilt for Python 3.9

* Sat Feb 15 2020 Kevin Fenzi <kevin@scrye.com> - 0.4.9-1
- Update to 0.4.9. Fixes bug 1768159

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.8-3
- Drop python2 subpackages and dependdencies. Fixes #1744402 and #1744646

* Tue Aug 20 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.8-2
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.8-1
- Update to latest version (#1742306)
- This fixes compatibility with python-beautifulsoup4 4.8.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.7-1
- Update to 0.4.7. Fixes bug #1716728

* Sat May 18 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.6-1
- Update to 0.4.6. Fixes bug #1709226

* Sun Apr 14 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.5-1
- Update to 0.4.5. Fixes bug #1697342

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.4-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 08 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.4-4
- Rebuild for upgrade path from f27

* Fri Oct 20 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.4-3
- Adjust BuildRequires names for older releases

* Fri Oct 20 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.4-2
- Clarify bundled copy of sigil-gumbo in spec comments.

* Sat Aug 12 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.4-1
- Initial version for Fedora
