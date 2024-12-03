%bcond_without tests
%bcond_without docs

Name:       python-atomicwrites
Version:    1.4.1
Release:    10%{?git_tag}%{?dist}
Summary:    Python Atomic file writes on POSIX 

License:    MIT
URL:        https://github.com/untitaker/%{name}
Source0:    https://github.com/untitaker/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:  noarch

%global short_name atomicwrites

BuildRequires: make
BuildRequires:  python3-devel
%if %{with docs}
BuildRequires:  python3-sphinx
%endif
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%global _description\
This Python module provides atomic file writes on POSIX operating systems.\
It sports:\
* Race-free assertion that the target file doesn't yet exist\
* Windows support\
* Simple high-level API that wraps a very flexible class-based API

%description %_description

%package -n python3-%{short_name}
Summary:    Python Atomic file writes on POSIX 

%description -n python3-%{short_name} %{_description}

Python 3 version.

%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build

%pyproject_wheel

%if %{with docs}
export PYTHONPATH=`pwd`
cd docs
make %{?_smp_mflags} SPHINXBUILD=sphinx-build-3 man
cd ..
unset PYTHONPATH
%endif


%install

%pyproject_install
%pyproject_save_files '%{short_name}*'

%if %{with docs}
install -d "$RPM_BUILD_ROOT%{_mandir}/man1"
cp -r docs/_build/man/*.1 "$RPM_BUILD_ROOT%{_mandir}/man1"
%endif

%check
%pyproject_check_import

%if %{with tests}

%{__python3} -m pytest -v
%endif

%files -n python3-%{short_name} -f %{pyproject_files}
%doc README.rst LICENSE
%if %{with docs}
%{_mandir}/man1/atomicwrites.1.*
%endif

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.1-9
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.1-8
- Bootstrap for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.4.1-4
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.1-3
- Bootstrap for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Michele Baldessari <michele@acksyn.org> - 1.4.1-1
- New upstream

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.0-12
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.0-11
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 1.4.0-8
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 1.4.0-7
- Bootstrap for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Bootstrap for Python 3.9

* Mon May 04 2020 Nils Philippsen <nils@redhat.com> - 1.4.0-2
- Remove remnants of building for Python 2

* Fri May 01 2020 Michele Baldessari <michele@acksyn.org> - 1.4.0-1
- New upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Subpackage python2-atomicwrites has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.0-3
- Bootstrap build for Python 3.8 without optional BRs.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-12
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-10
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-9
- Bootstrap for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-8
- Remove unused tox dependency, use pytest
- Enable tests, they work without network
- Use python2 explicitly instead of python

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.5-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.5-5
- Python 2 binary package renamed to python2-atomicwrites
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-2
- Rebuild for Python 3.6

* Sun Sep 04 2016 Michele Baldessari <michele@acksyn.org> - 1.1.5-1
- New upstream release

* Wed Jul 27 2016 Michele Baldessari <michele@acksyn.org> - 1.1.0-1
- New upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Mar 26 2016 Michele Baldessari <michele@acksyn.org> - 1.0.0-1
- New upstream release

* Mon Feb 22 2016 Michele Baldessari <michele@acksyn.org> - 0.1.9-1
- New upstream release (BZ 1308379)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 13 2015 Michele Baldessari <michele@acksyn.org> - 0.1.8-1
- New upstream (BZ 1262584)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Michele Baldessari <michele@acksyn.org> - 0.1.5-1
- New upstream (BZ 1209294)

* Mon Mar 02 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-5
- Disable tests as they require network

* Sun Mar 01 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-4
- Move it to python 3

* Sat Feb 28 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-3
- Fix check section and add python-tox as BR

* Sat Feb 28 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-2
- Improve description

* Mon Feb 23 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-1
- New upstream

* Wed Feb 04 2015 Michele Baldessari <michele@redhat.com> - 0.1.1-3
- Add python-sphinx BR

* Wed Oct 01 2014 Michele Baldessari <michele@redhat.com> - 0.1.1-1
- Initial packaging
