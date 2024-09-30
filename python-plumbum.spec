%global pypi_name plumbum
%global with_python2 0

Name:           python-%{pypi_name}
Version:        1.7.2
Release:        10%{?dist}
Summary:        Shell combinators library

License:        MIT
URL:            https://github.com/tomerfiliba/plumbum
Source0:        %{pypi_source}

BuildArch:      noarch
%if 0%{?with_python2}
BuildRequires:  python2-devel
%endif # if with_python2

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-setuptools_scm+toml

%global _description\
Ever wished the wrist-handiness of shell scripts be put into a real programming\
language? Say hello to Plumbum Shell Combinators. Plumbum (Latin for lead,\
which was used to create pipes back in the day) is a small yet feature-rich\
library for shell script-like programs in Python. The motto of the library is\
"Never write shell scripts again", and thus it attempts to mimic the shell\
syntax ("shell combinators") where it makes sense, while keeping it all\
pythonic and cross-platform.

%description %_description

%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary: %summary
Requires:       python2-six

%description -n python2-%{pypi_name} %_description
%endif # with_python2

%package -n python3-%{pypi_name}
Summary:        Shell combinators library
Requires:       python3-six

%description -n python3-%{pypi_name}
Ever wished the wrist-handiness of shell scripts be put into a real programming
language? Say hello to Plumbum Shell Combinators. Plumbum (Latin for lead,
which was used to create pipes back in the day) is a small yet feature-rich
library for shell script-like programs in Python. The motto of the library is
"Never write shell scripts again", and thus it attempts to mimic the shell
syntax ("shell combinators") where it makes sense, while keeping it all
pythonic and cross-platform.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?with_python2}
%{py2_build}
%endif # with_python2

%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files %{pypi_name}

%if 0%{?with_python2}
%{py2_install}
%endif # with_python2

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%doc LICENSE README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}.dist-info
%endif # with_python2

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc LICENSE README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.7.2-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.7.2-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.11

* Fri Mar 18 2022 Greg Hellings <greg.hellings@gmail.com> - 1.7.2-1
- Update to 1.7.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.10

* Sun Feb 14 2021 Greg Hellings <greg.hellings@gmail.com> - 1.7.0-1
- New version 1.7.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.9-2
- Rebuilt for Python 3.9

* Sat Apr 25 2020 Greg Hellings <greg.hellings@gmail.com> - 1.6.9-1
- New version 1.6.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 24 2019 Greg Hellings <greg.hellings@gmail.com> - 1.6.8-1
- New version 1.6.8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Greg Hellings <greg.hellings@gmail.com> - 1.6.7-1
- Upstream version 1.6.7
- Drop python2 package in Fedora Rawhide

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Greg Hellings <greg.hellings@gmail.com> - 1.6.6-1
- Upstream version 1.6.6
- Fix FTBFS BZ#1605834
- Switch to standard Python macros for source URL and building

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.0-7
- Python 2 binary package renamed to python2-plumbum
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.0-2
- Patch the Python 3.3 module subclass error.

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.0-1
- Update to 1.1.0.

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.1-2
- Introduce python3 subpackage.

* Mon Nov 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.1-1
- Update to 1.0.1.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.0-1
- Initial package.
