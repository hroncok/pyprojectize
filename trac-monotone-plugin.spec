%global tardate 20210704
%global tarrev  34341a53
%global tarname TracMonotone-%{version}.dev%{tardate}

Name:           trac-monotone-plugin
Version:        0.0.15
Release:        0.11.%{tardate}mtn%{tarrev}%{?dist}
Summary:        Monotone version control plugin for Trac
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://tracmtn.1erlei.de/
# Source comes from mtn right now:
#  mtn clone -r %%{tarrev} monotone.ca net.venge.monotone.trac-plugin tracmtn
#  cd tracmtn; python3 setup.py sdist --formats bztar
Source:         %{tarname}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-setuptools
Requires:       trac >= 1.5
Requires:       monotone >= 1.1


%description
This Trac plugin provides support for the Monotone SCM.


%prep
%autosetup -n %{tarname}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tracmtn


%files -f %{pyproject_files}
%doc README
%license COPYING


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.15-0.11.20210704mtn34341a53
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-0.10.20210704mtn34341a53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.15-0.9.20210704mtn34341a53
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-0.8.20210704mtn34341a53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-0.7.20210704mtn34341a53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.15-0.6.20210704mtn34341a53
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-0.5.20210704mtn34341a53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-0.4.20210704mtn34341a53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.15-0.3.20210704mtn34341a53
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-0.2.20210704mtn34341a53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Thomas Moschny <thomas.moschny@gmx.de> - 0.0.15-0.1.20210704mtn34341a53
- Update to latest snapshot and switch to Python3.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-25.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-24.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-23.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-22.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-21.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-20.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.0.14-19.20100327mtnda420c80
- Modernize spec file.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-19.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.0.14-18.20100327mtnda420c80
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-17.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-16.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-15.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-14.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-13.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-12.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-11.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-10.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-9.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-8.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-7.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.0.14-6.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Apr 11 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.0.14-5.20100327mtnda420c80
- Update to current head, in order to support monotone >= 0.46.
- Remove old conditionals.
- Use %%global instead of %%define.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-4.20080208mtnb4dd178b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-3.20080208mtnb4dd178b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.0.14-2.20080208mtnb4dd178b
- Rebuild for Python 2.6

* Fri Feb  8 2008 Roland McGrath <roland@redhat.com> - 0.0.14-1.20080208mtnb4dd178b
- New upstream version.

* Tue Feb  5 2008 Roland McGrath <roland@redhat.com> - 0.0.14-1.20080205mtn8ef4880f
- New upstream version.

* Fri Jan 25 2008 Roland McGrath <roland@redhat.com> - 0.0.13-1.20080125mtn393b5412
- New upstream version, fixes errors in log/ urls.

* Fri Jan 18 2008 Roland McGrath <roland@redhat.com> - 0.0.12-1.20080116mtn3907adc7
- New package
