Name:               python-llfuse
Version:            1.5.0
Release:            6%{?dist}
Summary:            Python Bindings for the low-level FUSE API
Source0:            https://files.pythonhosted.org/packages/source/l/llfuse/llfuse-%{version}.tar.gz
URL:                https://pypi.python.org/pypi/llfuse
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:            LicenseRef-Callaway-LGPLv2+

BuildRequires:      gcc
BuildRequires:      libattr-devel
BuildRequires:      fuse >= 2.9.0
BuildRequires:      fuse-devel >= 2.9.0
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-Cython
BuildRequires:      python%{python3_pkgversion}-pytest

%description
LLFUSE is a set of Python bindings for the low level FUSE API.
It requires at least FUSE 2.9.0.
LLFUSE was originally part of S3QL, but has been factored out so that it can be
used by other projects as well.

%package -n python%{python3_pkgversion}-llfuse
Summary:            Python Bindings for the low-level FUSE API Python %{python3_version} packages

%description -n python%{python3_pkgversion}-llfuse
LLFUSE is a set of Python %{python3_version} bindings for the low level FUSE API.
It requires at least FUSE 2.9.0.
LLFUSE was originally part of S3QL, but has been factored out so that it can be
used by other projects as well.

%prep
%autosetup -n llfuse-%{version}
rm -rf src/llfuse.egg-info

# Remove the cythonized files in order to regenerate them during build.
rm $(grep -rl '/\* Generated by Cython')

%generate_buildrequires
%pyproject_buildrequires

%build
%{__python3} setup.py build_cython
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l 'llfuse*'

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-3 -v test

%files -n python%{python3_pkgversion}-llfuse -f %{pyproject_files}
%doc README.rst Changes.rst


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 08 2023 Denis Fateyev <denis@fateyev.com> - 1.5.0-1
- Update to 1.5.0 release

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.4-2
- Rebuilt for Python 3.12

* Mon May 22 2023 Denis Fateyev <denis@fateyev.com> - 1.4.4-1
- Update to 1.4.4 release

* Fri May 12 2023 Denis Fateyev <denis@fateyev.com> - 1.4.3-1
- Update to 1.4.3 release

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.11

* Tue Jun 07 2022 Denis Fateyev <denis@fateyev.com> - 1.4.2-1
- Update to 1.4.2 release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.10

* Mon Feb 01 2021 Denis Fateyev <denis@fateyev.com> - 1.4.1-1
- Update to 1.4.1 release

* Thu Jan 28 2021 Denis Fateyev <denis@fateyev.com> - 1.4.0-1
- Update to 1.4.0 release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Denis Fateyev <denis@fateyev.com> - 1.3.8-2
- Fix upstream archive link

* Sat Oct 10 2020 Denis Fateyev <denis@fateyev.com> - 1.3.8-1
- Update to 1.3.8 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 05 2019 Denis Fateyev <denis@fateyev.com> - 1.3.6-1
- Update to 1.3.6 release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Charalampos Stratakis <cstratak@redhat.com> - 1.3.5-3
- Recythonize the sources

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.5-2
- Subpackage python2-llfuse has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 30 2018 Denis Fateyev <denis@fateyev.com> - 1.3.5-1
- Update to 1.3.5 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.7

* Sat Apr 07 2018 Denis Fateyev <denis@fateyev.com> - 1.3.3-1
- Update to 1.3.3 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Nov 18 2017 Denis Fateyev <denis@fateyev.com> - 1.3.2-1
- Update to 1.3.2 release

* Fri Sep 29 2017 Denis Fateyev <denis@fateyev.com> - 1.3-1
- Update to 1.3 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.2-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Denis Fateyev <denis@fateyev.com> - 1.2-1
- Remove deprecated pytest-3 compat patch
- Update to 1.2 release

* Wed Dec 28 2016 Adam Williamson <awilliam@redhat.com> - 1.1.1-2
- Backport a commit from upstream to fix tests with pytest-3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Sep 20 2016 Denis Fateyev <denis@fateyev.com> - 1.1.1-1
- Update to 1.1.1 release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 23 2016 Denis Fateyev <denis@fateyev.com> - 1.0-1
- Update to 1.0 release

* Fri Mar 04 2016 Denis Fateyev <denis@fateyev.com> - 0.43-1
- Modernize the package spec, test suite support
- Update to 0.43 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 21 2014 maci <maci@satgnu.net> - 0.40-1
- update to 0.40

* Tue Sep 24 2013 maci <maci@satgnu.net> - 0.39-1
- update to 0.39

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Marcel Wysocki <maci@satgnu.net> 0.38-1
- update to 0.38

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-11
- initial python3 build

* Thu Nov 01 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-10
- drop python-distribute requirement, it's provided by python-setuptools

* Wed Oct 31 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-9
- drop fuse requirement
- add license to docs

* Wed Oct 31 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-8
- filter out private libraries

* Tue Oct 30 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-7
- use python2-devel BR instead of python-devel

* Tue Oct 30 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-6
- add python-devel to the build requirements
- use optflags macro

* Mon Oct 29 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-5
- add python-setuptools to the build requirements
- delete llfuse.egg-info prior to build
- remove python from requirements, rpm picks it up itself

* Tue Oct 23 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-4
- don't use rm and install macros
- add missing dependencies

* Fri Oct 05 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-3
- add missing builddep

* Thu Oct 04 2012 Marcel Wysocki <maci@satgnu.net> 0.37.1-2
- fedora port

* Sun Jan 22 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.37.1-1
+ Revision: 764912
- new version 0.37.1

* Tue Dec 06 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.37-1
+ Revision: 738418
- Update to 0.37

* Tue Nov 29 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.36-1
+ Revision: 735378
- imported package python-llfuse
