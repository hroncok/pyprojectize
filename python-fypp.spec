%global pname fypp

Name: python-%{pname}
Version: 3.2
Release: 5%{?dist}
Summary: Fortran preprocessor
License: BSD-2-Clause
URL: https://github.com/aradi/fypp
Source0: %{url}/archive/%{version}/%{pname}-%{version}.tar.gz
BuildArch: noarch

%global desc Fypp is a Python powered preprocessor. It can be used for any programming\
languages but its primary aim is to offer a Fortran preprocessor, which helps\
to extend Fortran with condititional compiling and template metaprogramming\
capabilities. Instead of introducing its own expression syntax, it uses Python\
expressions in its preprocessor directives, offering the consistency and\
versatility of Python when formulating metaprogramming tasks. It puts strong\
emphasis on robustness and on neat integration into developing toolchains.

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-%{pname}}

%description -n python3-%{pname}
%{desc}

%prep
%autosetup -p1 -n %{pname}-%{version}
rm -rf src/%{pname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
test/runtests.sh %{__python3}

%files -n python3-%{pname}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{_bindir}/%{pname}
%{python3_sitelib}/%{pname}.py
%{python3_sitelib}/%{pname}-%{version}.dist-info
%{python3_sitelib}/__pycache__/%{pname}.cpython-%{python3_version_nodots}.opt-1.pyc
%{python3_sitelib}/__pycache__/%{pname}.cpython-%{python3_version_nodots}.pyc

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.2-1
- update to 3.2 (resolves rhbz#2233442)
- use SPDX identifier in License tag
- switch to GitHub source tarball

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.1-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1-2
- Rebuilt for Python 3.10

* Wed May 19 2021 Dominik Mierzejewski <rpm@greysector.net> 3.1-1
- update to 3.1 (#1951010)
- drop obsolete patch

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Dominik Mierzejewski <rpm@greysector.net> 3.0-1
- update to 3.0 (#1790240)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-9
- Rebuilt for Python 3.8

* Sat Aug 10 2019 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-8
- drop unnecessary "cleanup" from prep

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-2
- fix wrong-script-interpreter/non-executable-script rpmlint error

* Fri Oct 06 2017 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-1
- update to 2.1.1

* Fri Jun 30 2017 Dominik Mierzejewski <rpm@greysector.net> 2.0.1-2
- update upstream URL (bitbucket URL redirects to github)

* Tue Mar 14 2017 Dominik Mierzejewski <rpm@greysector.net> 2.0.1-1
- update to 2.0.1

* Mon Mar 13 2017 Dominik Mierzejewski <rpm@greysector.net> 2.0-1
- initial build
