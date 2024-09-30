Name:           python-firehose
Version:        0.5
Release:        30%{?dist}
Summary:        Library for working with output from static code analyzers

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/fedora-static-analysis/firehose
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# https://github.com/fedora-static-analysis/firehose/pull/42
Patch0:         0001-Remove-calls-to-deprecated-plistlib-function.patch

BuildRequires:  libxml2
# ^^^: for xmllint
# ^^^: used during selftests

BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-mock
# ^^^: used during selftests

%global _description\
"firehose" is a Python package intended for managing the results from\
code analysis tools (e.g. compiler warnings, static analysis, linters,\
etc).\
\
It currently provides parsers for the output of gcc, clang-analyzer and\
cppcheck.  These parsers convert the results into a common data model of\
Python objects, with methods for lossless roundtrips through a provided\
XML format.  There is also a JSON equivalent.\


%description %_description

%package -n python3-firehose
Summary:        Library for working with output from static code analyzers
Requires:  python3-six

%description -n python3-firehose %_description


%prep
%autosetup -p1 -n firehose-%{version}

# Change shebang according to Python version
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' firehose/parsers/cppcheck.py
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' firehose/parsers/gcc.py

sed -i 's/distutils\.core/setuptools/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files firehose
chmod +x %{buildroot}/%{python3_sitelib}/firehose/parsers/cppcheck.py
chmod +x %{buildroot}/%{python3_sitelib}/firehose/parsers/gcc.py


%check
%{__python3} -m unittest discover -v


%files -n python3-firehose -f %{pyproject_files}
%doc README.rst lgpl-2.1.txt examples firehose.rng


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5-30
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5-28
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5-25
- Fix FTBFS and FTI issues (rhbz#2226189) (rhbz#2220223) (rhbz#2154946)
- Remove deprecated patchN macro
- Replace distutils with setuptools

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5-23
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5-20
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5-14
- Remove call to deprecated plistlib functions for python 3.9 compatibility

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 20 2018 David Malcolm <dmalcolm@redhat.com> - 0.5-6
- Use explicit "python2" versions of specfile macros; fixup shebang lines
   to use explicit "python2" (rhbz #1605675)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-4
- Rebuilt for Python 3.7

* Fri Mar 23 2018 Jan Beran <jberan@redhat.com> - 0.5-3
- Fix of python3-firehose requires both Python 2 and Python 3 (rhbz #1546797)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5-1
- Update version
- Use versioned dependencies for python2
- Use github URL for sources

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2-14
- Python 2 binary package renamed to python2-firehose
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2-11
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun  6 2013 David Malcolm <dmalcolm@redhat.com> - 0.2-3
- remove redundant clean of the buildroot

* Fri May 31 2013 David Malcolm <dmalcolm@redhat.com> - 0.2-2
- add BR on python-mock and python3-mock (for selftests)

* Mon Mar 25 2013 David Malcolm <dmalcolm@redhat.com> - 0.2-1
- initial packaging
