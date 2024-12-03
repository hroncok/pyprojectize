Name:           python-xdot
Version:        1.1
Release:        18%{?dist}
Summary:        Interactive viewer for Graphviz dot files

# The file declares itself to be LGPLv3 or later at the top, but
# near the bottom is a large dict "brewer_colors" which is under
# "Apache-Style Software License for ColorBrewer software and ColorBrewer Color
# Schemes, Version 1.1"

# Automatically converted from old format: LGPLv3+ and ASL 1.1 - review is highly recommended.
License:        LGPL-3.0-or-later AND Apache-1.1
URL:            https://pypi.python.org/pypi/xdot
Source0:        https://github.com/jrfonseca/xdot.py/archive/%{version}.tar.gz#/xdot-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  graphviz

Requires:       python3-gobject
Requires:       graphviz


%description
xdot.py is an interactive viewer for graphs written in Graphviz's dot
language.

Internally it uses the graphviz's xdot output format as an intermediate
format, and PyGTK and Cairo for rendering.

xdot.py can be used either as a standalone application from command line
(as "xdot"), or as a library embedded in a python application.


%{?python_provide:%python_provide python3-xdot}


%prep
%setup -q -n xdot.py-%{version}

# Strip the shebang from xdot/__main__.py to avoid an rpmlint warning:
sed '1{\@^#!/usr/bin/env python@d}' xdot/__main__.py > xdot/__main__.py.new &&
 touch -r xdot/__main__.py xdot/__main__.py.new &&
 mv xdot/__main__.py.new xdot/__main__.py

# Remove pre-built egg present in upstream tarball:
rm -rf xdot.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l xdot


%check
%pyproject_check_import


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/xdot


%changelog
* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 David Malcolm <dmalcolm@redhat.com> - 1.1-1
- update to 1.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7-2
- Rebuild for Python 3.6

* Wed Sep 21 2016 Dominika Krejci <dkrejci@redhat.com> - 0.7-1
- Update to 0.7
- Switch from Python 2 to Python 3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar  3 2014 David Malcolm <dmalcolm@redhat.com> - 0.6-1
- 0.6

* Tue Sep 24 2013 David Malcolm <dmalcolm@redhat.com> - 0.5-4
- generalize egg-info glob to work with older pythons

* Mon Sep 23 2013 David Malcolm <dmalcolm@redhat.com> - 0.5-3
- add BR on python-setuptools

* Mon Sep 23 2013 David Malcolm <dmalcolm@redhat.com> - 0.5-2
- drop redundant definition of python_sitelib macro
- convert BR from python-devel to python2-devel
- remove pre-built egg before building
- remove redundant clean of buildroot from install section

* Mon Aug 26 2013 David Malcolm <dmalcolm@redhat.com> - 0.5-1
- initial packaging
