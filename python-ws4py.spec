%global srcname ws4py
%global _description %{expand:
WebSocket client and server library.}

Name:           python-ws4py
Version:        0.5.1
Release:        19%{?dist}
Summary:        WebSocket client and server library

# Bundled utf8validator is ASL 2.0 
# Automatically converted from old format: BSD and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND Apache-2.0
URL:            https://ws4py.readthedocs.org/en/latest/
Source0:        %pypi_source
Patch01:        0001-Python-3.7-and-3.8-compat.patch

BuildArch:      noarch

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-cherrypy
BuildRequires:  python3-tornado
BuildRequires:  python3-gevent
BuildRequires:  python3-pytest
Requires:       python3-cherrypy
Requires:       python3-tornado
Requires:       python3-gevent
Provides:       bundled(utf8validator)

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/

%check
sed -i 's/^from mock import /from unittest.mock import /' test/test_*.py
%{python3} -m pytest

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-19
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.5.1-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Python Maint <python-maint@redhat.com> - 0.5.1-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.5.1-10
- Rebuilt for Python 3.11

* Tue Feb 22 2022 Stefan Bluhm <stefan.bluhm@clacee.eu> - 0.5.1-9
- Replaced python-mock with unittest.mock

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.9

* Thu Mar 12 2020 Fabien Boucher <fboucher@redhat.com> - 0.5.1-2
- Adapt packaging for Rawhide from Software Factory packaging.

* Mon Jun 04 2018 Tristan Cacqueray <tdecacqu@redhat.com> - 0.5.1-1
- Initial packaging
