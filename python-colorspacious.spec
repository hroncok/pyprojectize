%bcond_without check
%bcond_without html
%global pname colorspacious

Name: python-%{pname}
Version: 1.1.2
Release: 24%{?dist}
Summary: Perform colorspace conversions accurately and easily
License: MIT
URL: https://github.com/njsmith/colorspacious
Source0: https://files.pythonhosted.org/packages/source/c/%{pname}/%{pname}-%{version}.tar.gz
Patch0: %{name}-1.1.2-sphinx.patch
%if %{with html}
BuildRequires: graphviz
BuildRequires: make
BuildRequires: python3-ipython-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-sphinxcontrib-bibtex
BuildRequires: python3-matplotlib
%endif
%if %{with check}
BuildRequires: python3-nose
%endif
BuildArch: noarch

%global desc \
Colorspacious is a powerful, accurate, and easy-to-use library for\
performing colorspace conversions.\
\
In addition to the most common standard colorspaces (sRGB, XYZ, xyY,\
CIELab, CIELCh), we also include: color vision deficiency ("color\
blindness") simulations using the approach of Machado et al (2009);\
a complete implementation of CIECAM02; and the perceptually uniform\
CAM02-UCS / CAM02-LCD / CAM02-SCD spaces proposed by Luo et al (2006).

%description
%{desc}

%package doc
Summary: HTML documentation for python colorspacious module

%description doc
%{desc}

This package contains the HTML documentation.

%package -n python3-%{pname}
Summary: Perform colorspace conversions accurately and easily
BuildRequires: python3-devel
BuildRequires: python3-numpy
Requires: python3-numpy

%description -n python3-%{pname}
%{desc}

This package contains the python3 module.

%prep
%setup -q -n %{pname}-%{version}
%patch -P0 -p1
rm -r *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%if %{with html}
pushd doc
PYTHONPATH=`realpath ../build/lib.linux*` make html
popd
%endif
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pname}

%if %{with check}
%check
%pyproject_check_import

nosetests-3 --all-modules colorspacious
%endif

%if %{with html}
%files doc
%doc doc/_build/html/*
%endif

%files -n python3-%{pname} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.1.2-23
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 1.1.2-19
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.1.2-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.2-13
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Dominik Mierzejewski <dominik@greysector.net> 1.1.2-12
- fix build with sphinxcontrib-bibtex 2.0 (#1914144)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Petr Viktorin <releng@fedoraproject.org> - 1.1.2-4
- Remove the Python 2 subpackage (#1629833)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-2
- Rebuilt for Python 3.7

* Thu Apr 12 2018 Dominik Mierzejewski <dominik@greysector.net> 1.1.2-1
- update to 1.1.2 (#1564870)

* Fri Apr 06 2018 Dominik Mierzejewski <dominik@greysector.net> 1.1.1-1
- update to 1.1.1 (#1562763)
- upstream switched to tar.gz for source
- drop obsolete patch
- enable testsuite

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuild for Python 3.6

* Thu Sep 22 2016 Dominik Mierzejewski <dominik@greysector.net> 1.0.0-3
- use a simpler patch (by QuLogic)
- add missing build dependency for building HTML docs

* Sat Sep 10 2016 Dominik Mierzejewski <dominik@greysector.net> 1.0.0-2
- build python3 package as well

* Sun Jun 05 2016 Dominik Mierzejewski <dominik@greysector.net> 1.0.0-1
- initial build
