%{?python_enable_dependency_generator}

%global srcname pvc 

Name:           python-%{srcname}
Version:        0.3.0
Release:        25%{?dist}
Summary:        Python vSphere Client with a dialog interface
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/dnaeon/%{srcname}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch0:         %{url}/commit/79a6f63f5b57622f1d3871b86ce8f048803d0914.patch
Patch1:         %{url}/commit/1b8b803d467d550fd21830d407f0e900b2b10363.patch

BuildArch:      noarch


%global _description \
PVC is an interactive text-mode vSphere Client with a dialog interface\
for GNU/Linux systems built on top of the pyVmomi vSphere API bindings.\
\
Using PVC allows you to quickly navigate in your vSphere environment\
and perform common tasks against various vSphere Managed Entities.

%description
%{_description}

%package        doc
Summary:        Documentation files for PVC (Python vSphere Client)
BuildArch:      noarch

%description    doc
%{_description}\
\
This package installs the documentation files.

%package     -n python%{python3_pkgversion}-%{srcname}
Summary:        Python vSphere Client with a dialog interface
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
BuildRequires: make
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-humanize
BuildRequires:  python%{python3_pkgversion}-pyvmomi
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-vconnector
BuildRequires:  python%{python3_pkgversion}-sphinx
Requires:       python%{python3_pkgversion}-dialog
# no magic dependencies in epel
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-humanize
Requires:       python%{python3_pkgversion}-pyvmomi
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-vconnector
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{_description}


%prep
%autosetup -p1 -n%{srcname}-%{version}
# dependency checker does not like dashes in version specifier
sed -i 's/5.5.0-2014.1.1/5.5.0.2014.1.1/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}
PYTHONPATH=../src %make_build -C docs html \
 SPHINXBUILD=sphinx-build-%{python3_version} \
 SPHINXOPTS=%{_smp_mflags}
rm -rf docs/_build/html/.{doctrees,buildinfo}

%install
%{pyproject_install}


%files doc
%license LICENSE
%doc docs/_build/html/

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%{_bindir}/%{srcname}-tui


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.3.0-23
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 30 2023 Raphael Groner <raphgro@fedoraproject.org> - 0.3.0-20
- ignore dash in versioned dependency 

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.3.0-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.0-13
- Rebuilt for Python 3.10

* Sat Mar 06 2021 Raphael Groner <raphgro@fedoraproject.org> - 0.3.0-12
- add patch to support for VMRC, upstream #24

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Raphael Groner <projects.rg@smart.ms> - 0.3.0-9
- add patch to improve password input, upstream #28

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-8
- Rebuilt for Python 3.9

* Thu Feb 06 2020 Raphael Groner <projects.rg@smart.ms> - 0.3.0-7
- [epel7] fix call to sphinx with python3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 0.3.0-3
- drop brand

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 0.3.0-2
- fix URL
- fix description
- split doc subpackage
- add dialog dependencies for runtime
- ignore manpage warning of rpmlint due to interactive tui, later in scm

* Thu Jul 25 2019 Raphael Groner <projects.rg@smart.ms> - 0.3.0-1
- initial
