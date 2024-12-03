# Disable automatic dependencies generation
# It fails for xattr as pyxattr provices pyxattr, not xattr
%{?python_disable_dependency_generator}

%global pypi_name pifpaf

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-pifpaf
Version:        2.2.2
Release:        23%{?dist}
Summary:        Pifpaf is a suite of fixtures to manage daemons 
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/jd/pifpaf
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        Pifpaf is a suite of fixtures to manage daemons

BuildRequires:    python2-setuptools
BuildRequires:    python2-devel
BuildRequires:    python2-pbr

Requires:         python2-daiquiri
Requires:         python2-psutil
Requires:         python2-pbr
Requires:         python2-six
Requires:         python2-fixtures
Requires:         python2-jinja2

%if 0%{?rhel} <= 7
Requires:         python-click
Requires:         pyxattr
%else
Requires:         python2-click
Requires:         python2-pyxattr
%endif

%description -n python2-%{pypi_name}
Pifpaf is a suite of fixtures and a command-line tool that allows to start and
stop daemons for a quick throw-away usage.

%endif


%if %{with python3}
%package -n python3-%{pypi_name}

Summary:          Pifpaf is a suite of fixtures to manage daemons

BuildRequires:    python3-devel
BuildRequires:    python3-pbr

Requires:         python3-click
Requires:         python3-daiquiri
Requires:         python3-psutil
Requires:         python3-pbr
Requires:         python3-six
Requires:         python3-fixtures
Requires:         python3-pyxattr
Requires:         python3-jinja2

%description -n python3-%{pypi_name}
Pifpaf is a suite of fixtures and a command-line tool that allows to start and
stop daemons for a quick throw-away usage. 

%endif

%description
Pifpaf is a suite of fixtures and a command-line tool that allows to start and
stop daemons for a quick throw-away usage. 

%prep
%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%pyproject_wheel
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%pyproject_install
%pyproject_save_files -l '*'
%endif


%if %{with python2}
%check
%pyproject_check_import
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/pifpaf
%{python2_sitelib}/*
%endif

%if %{with python3}
%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/pifpaf
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.2-23
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.2-21
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.2-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.2-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.2-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Javier Peña <jpena@redhat.com> - 2.2.2-3
- Fix dependencies when building on RHEL 7

* Fri Feb 01 2019 Alfredo Moralejo <amoralej@redhat.com> - 2.2.2-2
- Disable automatic dependencies generation.

* Fri Feb 01 2019 Javier Peña <jpena@redhat.com> - 2.2.2-1
- Rebase to 2.2.2
- Drop python2 subpackage in Fedora

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-7
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Pradeep Kilambi <pkilambi@redhat.com> - 1.1.0-1
- rebase to 1.1.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 08 2017 Pradeep Kilambi <pkilambi@redhat.com> - 0.24.1-1
- rebase to 0.24.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuild for Python 3.6

* Fri Jul 29 2016 Pradeep Kilambi <pkilambi@redhat.com> - 0.12.0-1
- rebase to 0.12.0

* Fri Jul 29 2016 Pradeep Kilambi <pkilambi@redhat.com> - 0.6.0-2
- dropped macros
- fixed python-xattr
- fixed python3 symlink binaries

* Thu Jun 23 2016 Pradeep Kilambi <pkilambi@redhat.com> - 0.6.0-1
- initial package release
