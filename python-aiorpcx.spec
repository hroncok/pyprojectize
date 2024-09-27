%global pypi_name aiorpcX
%global srcname aiorpcx

Name:      python-%{srcname}
Version:   0.23.1
Release:   3%{?dist}
Summary:   Generic async RPC implementation

# https://github.com/kyuupichan/aiorpcX/issues/11
# aiorpcx/curio.py is BSD, rest is MIT
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:   LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:       https://pypi.org/project/aiorpcX/
Source:    %{pypi_source %{pypi_name}}
Source2:   https://raw.githubusercontent.com/kyuupichan/aiorpcX/%{version}/LICENCE

BuildArch: noarch

%global _description %{expand:
Transport, protocol and framing-independent async RPC client
and server implementation.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
install -m 644 %SOURCE2 .
rm -vrf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%doc README.rst
%license LICENCE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{pypi_name}.dist-info/

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.23.1-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 Jonathan Wright <jonathan@almalinux.org> - 0.23.1-1
- update to 0.23.1 rhbz#2269920

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.22.1-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.22.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.22.1-2
- Rebuilt for Python 3.11

* Sun Mar 27 2022 Jonathan Schleifer <js@nil.im> - 0.22.1-1
- Updated to 0.22.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.18.7-2
- Rebuilt for Python 3.10

* Mon Apr 05 2021 Jonny Heggheim <hegjon@gmail.com> - 0.18.7-1
- Updated to 0.18.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Jonny Heggheim <hegjon@gmail.com> - 0.18.4-1
- Updated to 0.18.4

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Thu Apr 04 2019 Jonny Heggheim <hegjon@gmail.com> - 0.10.5-2
- Changed python- prefix to python3-

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.5-1
- Initial package
