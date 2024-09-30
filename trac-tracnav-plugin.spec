%global srcname TracNav

Name:           trac-tracnav-plugin
Version:        4.3
Release:        14%{?dist}
Summary:        Navigation Bar for Trac
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://svn.ipd.kit.edu/trac/javaparty/wiki/TracNav
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-toml
Requires:       trac >= 0.11

%description
The TracNav macro implements a fully customizable navigation bar for
the Trac wiki engine. The contents of the navigation bar is a wiki
page itself and can be edited like any other wiki page through the web
interface. The navigation bar supports hierarchical ordering of
topics. The design of TracNav mimics the design of the TracGuideToc
that was originally supplied with Trac.


%prep
%autosetup -n TracNav-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tracnav


%files -f %{pyproject_files}
%doc README.md
%license COPYING


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.3-12
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 4.3-9
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.3-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.3-3
- Rebuilt for Python 3.10

* Fri Feb 26 2021 Thomas Moschny <thomas.moschny@gmx.de> - 4.3-2
- Fix requirements.

* Fri Feb 26 2021 Thomas Moschny <thomas.moschny@gmx.de> - 4.3-1
- Update to 4.3 and switch to Python3.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Thomas Moschny <thomas.moschny@gmx.de> - 4.1-18
- Modernize spec file.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 04 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.1-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-14
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 4.1-11
- Replace python-setuptools-devel BR with python-setuptools

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  7 2011 Thomas Moschny <thomas.moschny@gmx.de> - 4.1-4
- Add patch from upstream for Trac 0.12 compatibility.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 31 2009 Thomas Moschny <thomas.moschny@gmx.de> - 4.1-2
- Use %%global instead of %%define.

* Mon Jul 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 4.1-1
- New package.
