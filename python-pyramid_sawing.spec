%global srcname pyramid_sawing
%global desc A Pyramid framework plugin for configuring logging via YAML. This uses\
the Python standard-library's logging (initialized using\
logging.config.dictConfig).


Name: python-%{srcname}
Version: 1.1.3
Release: 22%{?dist}
BuildArch: noarch

Summary: Pyramid plugin for YAML logging configuration
# Automatically converted from old format: AGPLv3
License: AGPL-3.0-only
URL:     https://github.com/openstax/pyramid_sawing
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/openstax/pyramid_sawing/pull/3
Patch0:  0000-Use-yaml.safe_load-instead-of-load.patch

BuildRequires: python3-devel
BuildRequires: python3-pyramid
BuildRequires: python3-pyyaml


%description
%{desc}


%package -n python3-%{srcname}
Summary: %{summary}



%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%{__python3} setup.py test


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGES.rst
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.3-21
- convert license to SPDX

* Tue Jun 18 2024 Python Maint <python-maint@redhat.com> - 1.1.3-20
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.1.3-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Mattia Verga <mattia.verga@proton.me> - 1.1.3-14
- Rebuilt for Pyramid 2.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.1.3-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.3-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.3-1
- Initial release.
