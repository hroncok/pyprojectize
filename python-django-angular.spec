# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# Setup _pkgdocdir if not defined already.
%{!?_py3docdir:%global _py3docdir	%{_docdir}/python3-%{pypi_name}%{!?_pkgdocdir:-%{version}}}
%{!?_pkgdocdir:%global _pkgdocdir	%{_docdir}/%{name}-%{version}}

# Settings used for build from snapshots.
%{!?rel_build:%global commit		ab2dc2db9db979816a4a7c4fd269ad2f27ef2d0b}
%{!?rel_build:%global commit_date	20150104}
%{!?rel_build:%global shortcommit	%(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global gitver		git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global gitrel		.git%{commit_date}.%{shortcommit}}

# Proper naming for the tarball from github.
%global gittar %{name}-%{version}%{!?rel_build:-%{gitver}}.tar.gz

# Upstream name
%global pypi_name django-angular

Name:			python-%{pypi_name}
Version:		2.0.3
Release:		22%{?gitrel}%{?dist}
Summary:		Classes and utility functions to integrate AngularJS with Django

License:		MIT
URL:			https://github.com/jrief/%{pypi_name}
# Sources for release-builds.
%{?rel_build:Source0:	%{url}/archive/%{version}.tar.gz#/%{gittar}}
# Sources for snapshot-builds.
%{!?rel_build:Source0:	%{url}/archive/%{commit}.tar.gz#/%{gittar}}

BuildArch:		noarch

%description
Django-Angular is a collection of utilities, which aim to ease the
integration of Django with AngularJS by providing reusable components.


%package -n python3-%{pypi_name}
Summary:		Classes and utility functions to integrate AngularJS with Django

BuildRequires: make
BuildRequires:		python3-devel

Requires:		python3-six
Requires:		python3-django

Obsoletes:		python2-%{pypi_name} < 1.1.2-2
Obsoletes:		python-%{pypi_name} < 1.1.2-2



%description -n python3-%{pypi_name}
Django-Angular is a collection of utilities, which aim to ease the
integration of Django with AngularJS by providing reusable components.


%package -n python3-%{pypi_name}-doc
Summary:		Documentation-files for python3-%{pypi_name}

BuildRequires:		dos2unix
BuildRequires:		python3-sphinx

Obsoletes:		python2-%{pypi_name}-doc < 1.1.2-2
Obsoletes:		python-%{pypi_name}-doc < 1.1.2-2


%description -n python3-%{pypi_name}-doc
This package contains the documentation-files for python3-%{pypi_name}.


%prep
%if 0%{?rel_build}
%autosetup -n %{pypi_name}-%{version} -p 1
%else
%autosetup -n %{pypi_name}-%{commit} -p 1
%endif

%{__rm} -rf *.egg-info examples/.coveragerc


# Fix hashbangs.
for _file in $(%{__grep} -Rle '^#![ \t]*/usr/bin/env[ \t]*python' .)
do
  %{__sed} -e 's~^#![ \t]*/usr/bin/env[ \t]*python.*$~#!%{__python3}~'	\
	< ${_file} > ${_file}.new
  /bin/touch -r ${_file} ${_file}.new
  %{__mv} -f ${_file}.new ${_file}
done


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Documentation
pushd docs
%make_build html SPHINXBUILD=sphinx-build-3
%{__rm} -f _build/html/{.buildinfo,objects.inv}
%{_bindir}/find _build/html -type f -print0 |				\
	%{_bindir}/xargs -0 %{_bindir}/dos2unix -k -o -s
popd


%install
%pyproject_install
%pyproject_save_files -l djng

# Documentation
%{__mkdir} -p %{buildroot}%{?_py3docdir}
%{__cp} -a CONTRIBUTING.md README.md docs/_build/html client examples	\
		%{buildroot}%{?_py3docdir}
%if 0%{?rhel} && 0%{?rhel} <= 6
%{__cp} -a LICENSE.txt %{buildroot}%{?_py3docdir}
%endif


%check
%pyproject_check_import

# noop


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc %dir %{?_py3docdir}
%if 0%{fedora} || 0%{?rhel} >= 7
%else
%doc %{?_py3docdir}/LICENSE.txt
%endif

%files -n python3-%{pypi_name}-doc
%if 0%{fedora} || 0%{?rhel} >= 7
%license %{_datadir}/licenses/python3-%{pypi_name}*
%endif
%doc %{?_py3docdir}


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.3-21
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.0.3-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.3-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.3-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Matthias Runge <mrunge@redhat.com> - 2.0.3-1
- update to 2.0.3 (rhbz#1490109)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-2
- Removed Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Django20
- Add %%python_provide to the docs subpackage

* Thu Aug 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2 (rhbz#1480933)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 (rhbz#1474123)
- Update spec file to recent guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-2
- Rebuild for Python 3.6

* Wed Aug 31 2016 Matthias Runge <mrunge@redhat.com > - 0.8.3-1
- update to 0.8.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.16-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 23 2016 Matthias Runge <mrunge@redhat.com> - 0.7.16-1
- update to 0.7.16 (rhbz#1310274)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.15-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Björn Esser <bjoern.esser@gmail.com> - 0.7.15-1
- Update to 0.7.15 (#1219993)

* Tue Mar 31 2015 Björn Esser <bjoern.esser@gmail.com> - 0.7.13-1
- new upstream release v0.7.13 (#1207442)

* Fri Jan 16 2015 Björn Esser <bjoern.esser@gmail.com> - 0.7.10-3.git20150104.ab2dc2d
- updated to latest post-release-snapshot

* Fri Jan 16 2015 Björn Esser <bjoern.esser@gmail.com> - 0.7.10-2
- fix versioning in %%{_py3docdir}

* Thu Jan 15 2015 Björn Esser <bjoern.esser@gmail.com> - 0.7.10-1
- new upstream release 0.7.10
- added sphinx-documentation
- added Python3-build
- several improvements to spec-file

* Thu Jan 15 2015 Björn Esser <bjoern.esser@gmail.com> - 0.7.1-3
- initial import (#1182533)

* Mon May 26 2014 Matthias Runge <mrunge@redhat.com> - 0.7.1-2
- require python-django

* Tue May 20 2014 Matthias Runge <mrunge@redhat.com> - 0.7.1-1
- Initial package.
