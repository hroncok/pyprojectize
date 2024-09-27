%global srcname rebulk

Name: python-%{srcname}
Version: 3.3.0
Release: 6%{?dist}
Summary: ReBulk is a python library that performs advanced searches in strings
# Everything licensed as MIT, except:
# rebulk/toposort.py: Apache (v2.0)
# rebulk/test/test_toposort.py: Apache (v2.0)
# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License: LicenseRef-Callaway-MIT AND Apache-2.0
URL: https://github.com/Toilal/rebulk
Source: https://github.com/Toilal/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-pytest-runner
BuildRequires: python3-six
BuildRequires: pylint

%global _description\
ReBulk is a python library that performs advanced searches in strings that\
would be hard to implement using re module or String methods only.\
\
It includes some features like Patterns, Match, Rule that allows developers\
to build a custom and complex string matcher using a readable and\
extendable API.

%description %_description

%package -n python3-%{srcname}
Summary: %summary
%py_provides python3-%{srcname}
Requires: python3-six

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# Remove shebang from Python3 libraries
for lib in `find %{buildroot}%{python3_sitelib} -name "*.py"`; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%check
%pytest

%files -n python3-%{srcname}
%doc README.md CHANGELOG.md
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}.dist-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 3.3.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Juan Orti Alcaine <jortialc@redhat.com> - 3.3.0-1
- Version 3.3.0 (rhbz#2254798)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 3.2.0-2
- Rebuilt for Python 3.12

* Sat Feb 25 2023 Juan Orti Alcaine <jortialc@redhat.com> - 3.2.0-1
- Version 3.2.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Juan Orti Alcaine <jortialc@redhat.com> - 3.1.0-1
- Version 3.1.0 (#2020752)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.1-4
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Juan Orti Alcaine <jortialc@redhat.com> - 3.0.1-3
- Use pytest and py_provides macros

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Juan Orti Alcaine <jortialc@redhat.com> - 3.0.1-1
- Version 3.0.1

* Thu Oct 08 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.0.1-4
- BR: python3-setuptools

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.0.1-1
- Version 2.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.0.0-1
- Version 2.0.0

* Mon Aug 26 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.0.1-1
- Version 1.0.1
- Tests now pass on Python 3.8, enable them again

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.0.0-2
- Disable tests RHBZ#1716519

* Tue Jun 11 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.0-1
- Version 1.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-7
- Subpackage python2-rebulk has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.0-3
- Simplify Source URL
- Remove shebang from libraries
- Some files licensed as ASL 2.0

* Tue Aug 29 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.0-2
- Require python-six

* Mon Aug 28 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.0-1
- Initial RPM release
