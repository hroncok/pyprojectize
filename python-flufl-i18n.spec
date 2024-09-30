%global srcname flufl.i18n
%global pkgname flufl-i18n
%global summary A high level API for Python internationalization
%global _description \
The ``flufl.i18n`` library provides a convenient API for managing translation \
contexts in Python applications. It provides facilities not only for          \
single-context applications like command line scripts, but also more          \
sophisticated management of multiple-context applications such as Internet    \
servers.

Name:           python-%{pkgname}
Version:        2.0.2
Release:        18%{?dist}
Summary:        %{summary}

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://gitlab.com/warsaw/flufl.i18n
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-srpm-macros
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-atpublic
%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-atpublic
%endif

%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-atpublic

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pkgname}
Summary:        %{summary}
Requires:       python%{python3_other_pkgversion}-setuptools
Requires:       python%{python3_other_pkgversion}-atpublic

%description -n python%{python3_other_pkgversion}-%{pkgname} %{_description}
%endif


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
%pyproject_install
%pyproject_save_files flufl
%if 0%{?with_python3_other}
%py3_other_install
%endif

# This will go in %%doc
rm -rf %{buildroot}%{_prefix}/lib/python*/site-packages/flufl/i18n/{*.rst,docs,conf.py}


%check
%{__python3} setup.py test
%if 0%{?with_python3_other}
%{__python3_other} setup.py test
%endif


%files -n python%{python3_pkgversion}-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc flufl/i18n/*.rst flufl/i18n/docs/*.rst
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}-nspkg.pth

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%license LICENSE
%doc flufl/i18n/*.rst flufl/i18n/docs/*.rst
%{python3_other_sitelib}/flufl/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}.egg-info/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}-nspkg.pth
%endif


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.2-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.2-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.2-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.2-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.2-1
- Version 2.0.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.1-1
- Version 2.0.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Aurelien Bompard <abompard@fedoraproject.org> - 1.1.3-5
- Fix BuildRequires name

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-2
- Rebuild for Python 3.6

* Wed Sep 14 2016 Aurelien Bompard <abompard@fedoraproject.org> - 1.1.3-1
- Initial package.
