%global upstream_name www-authenticate
%global modname www_authenticate


Name:           python-%{upstream_name}
Version:        0.9.2
Release:        28%{?dist}
Summary:        Python library for parsing WWW-Authenticate HTTP header values
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/alexsdutton/www-authenticate
Source0:        https://github.com/alexsdutton/%{upstream_name}/archive/%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
# https://github.com/alexsdutton/www-authenticate/issues/1
Source1:        https://raw.githubusercontent.com/lphuberdeau/www-authenticate/a35e5df38d909e0f73bb6df0573fa80333a4922e/LICENSE
BuildArch:      noarch

%global _description \
Parsing WWW-Authenticate headers is difficult. Let this tiny library do all \
the hard work for you.

%description %{_description}

%package -n python%{python3_pkgversion}-%{upstream_name}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose

%description -n python%{python3_pkgversion}-%{upstream_name} %{_description}

Python %{python3_pkgversion} version.

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{upstream_name}
Summary:        %{summary}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-nose

%description -n python%{python3_other_pkgversion}-%{upstream_name} %{_description}

Python %{python3_other_pkgversion} version.
%endif

%prep
%autosetup -n %{upstream_name}-%{version}
cp -p %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%pyproject_install
%pyproject_save_files -l %{modname}
%if 0%{?with_python3_other}
%py3_other_install
%endif

%check
%{__python3} setup.py test
%if 0%{?with_python3_other}
%{__python3_other} setup.py test
%endif

%files -n python%{python3_pkgversion}-%{upstream_name} -f %{pyproject_files}
%doc README.rst

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{upstream_name}
%license LICENSE
%doc README.rst
%{python3_other_sitelib}/%{modname}.py*
%{python3_other_sitelib}/__pycache__/%{modname}.*
%{python3_other_sitelib}/%{modname}-*.egg-info
%endif

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.2-28
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.2-26
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.2-22
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.2-19
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.2-16
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.2-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 08 2016 Dan Callaghan <dcallagh@redhat.com> - 0.9.2-1
- initial version
