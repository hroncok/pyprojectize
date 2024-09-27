Name: python-ovirt-engine-sdk4
Summary: Python SDK for version 4 of the oVirt Engine API
Version: 4.6.2
%global major_version %(v=%{version}; echo ${v:0:3})
Release: 6%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/oVirt/python-ovirt-engine-sdk4
Source: https://github.com/oVirt/python-ovirt-engine-sdk4/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: libxml2-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%global _description\
This package contains the Python SDK for version 4 of the oVirt Engine\
API.

%description %_description

%package -n python3-ovirt-engine-sdk4
Summary: %summary
%{?python_provide:%python_provide python3-ovirt-engine-sdk4}

%description -n python3-ovirt-engine-sdk4 %_description

%prep
%autosetup
%py3_shebang_fix examples
find examples -type f -print0 | xargs -0 chmod 0644
GENERATED_FILES="
 lib/ovirtsdk4/version.py
 setup.py
 PKG-INFO
 lib/ovirt_engine_sdk_python.egg-info/PKG-INFO
 python-ovirt-engine-sdk4.spec
"

for gen_file in ${GENERATED_FILES} ; do
  sed \
    -e "s|@RPM_VERSION@|%{version}|g" \
    -e "s|@RPM_RELEASE@|%{release}|g" \
    -e "s|@PACKAGE_NAME@|%{name}|g" \
    -e "s|@PACKAGE_VERSION@|%{package_version}|g" \
    < ${gen_file}.in > ${gen_file}
done

%build
%py3_build

%install
%py3_install

%files -n python3-ovirt-engine-sdk4
%doc README.adoc
%doc examples
%license LICENSE.txt
%{python3_sitearch}/ovirtsdk4
%{python3_sitearch}/ovirt_engine_sdk_python-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 4.6.2-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.6.2-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Juan Orti Alcaine <jortialc@redhat.com> - 4.6.2-1
- Version 4.6.2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.5.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 01 2022 Klaas Demter <Klaas-@users.noreply.github.com> - 4.5.2-1
- Version 4.5.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.4.15-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Juan Orti Alcaine <jortialc@redhat.com> - 4.4.15-1
- Version 4.4.15

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.9-2
- Rebuilt for Python 3.10

* Mon Mar 08 2021 Juan Orti Alcaine <jortialc@redhat.com> - 4.4.9-1
- Version 4.4.9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.2-3
- Rebuilt for Python 3.9

* Fri May 08 2020 Juan Orti Alcaine <jortialc@redhat.com> - 4.3.2-2
- Correct provides
- Include python3_sitearch dirs explicitly
- Correct shebang and remove execution of example scripts
- BR: python3-setuptools

* Wed May 06 2020 Juan Orti Alcaine <jortialc@redhat.com> - 4.3.2-1
- Version 4.3.2
- Spec improvements

* Thu Jun 06 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 4.3.1-1
- 4.3.1
- Adhere to Fedora packaging guidelines naming schema

* Wed Jun 14 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.0-1
- 4.2.0
