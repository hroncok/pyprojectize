%global pypi_name npyscreen

Name:           python-%{pypi_name}
Version:        4.10.5
Release:        18%{?dist}
Summary:        Writing user interfaces without all that ugly mucking about in hyperspace

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.npcole.com/npyscreen/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
This library provides a framework for developing console applications using
Python and curses. This framework should be powerful enough to create everything
from quick, simple programs to complex, multi-screen applications.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This library provides a framework for developing console applications using
Python and curses. This framework should be powerful enough to create everything
from quick, simple programs to complex, multi-screen applications.


%prep
%autosetup -n %{pypi_name}-%{version}
for i in $(find . -name '*.py')
do
        sed -i -e"s|#\!/usr/bin/python||" $i
        sed -i -e"s|#\!/usr/bin/env python||" $i
        sed -i -e"s|#\!/usr/bin/env pyton||" $i
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENCE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.10.5-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.10.5-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.10.5-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.10.5-9
- Rebuilt for Python 3.11

* Fri Feb 11 2022 Neal Gompa <ngompa@fedoraproject.org> - 4.10.5-8
- Minor spec cleanups

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.10.5-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.10.5-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Neil Horman <nhorman@redhat.com> - 4.10.5-2
- Updated to use %pypi_source
- Updated to include license file
- Fixed spelling typo in License file
- Shortened descriptions
- Fixed egg-info glob

* Thu Dec 12 2019 Neil Horman <nhorman@redhat.com> - 4.10.5-1
- Initial package

