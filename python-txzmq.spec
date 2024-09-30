# what it's called on pypi
%global srcname txZMQ
# what it's imported as
%global libname txzmq
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{libname}

%global common_description %{expand:
txZMQ allows to integrate easily ZeroMQ sockets into Twisted event loop
(reactor).}

%bcond_without  tests


Name:           python-%{pkgname}
Version:        1.0.0
Release:        12%{?dist}
Summary:        Twisted bindings for ZeroMQ
License:        MPL-2.0
URL:            https://github.com/smira/txZMQ
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist twisted pyzmq}
%endif


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -rf %{eggname}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{libname}


%check
%if %{with tests}
PYTHONPATH=%{buildroot}%{python3_sitelib} trial-3 txzmq
%endif


%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.0.0-11
- Rebuilt for Python 3.13

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-10
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.0.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Carl George <carl@george.computer> - 1.0.0-1
- Latest upstream
- Resolves: rhbz#2004574

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Carl George <carl@george.computer> - 0.8.2-1
- Latest upstream rhbz#1772197

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-11
- Subpackage python2-txzmq has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.0-3
- Python 2 binary package renamed to python2-txzmq
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Lumir Balhar <lbalhar@redhat.com> - 0.8.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-7.git772df64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-6.git772df64
- Rebuild for Python 3.6

* Tue Jul 26 2016 Lumir Balhar <lbalhar@redhat.com> - 0.7.4-5.git772df64
- Enabled Py3 support
- Changed source to the latest commit on GitHub

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Ralph Bean <rbean@redhat.com> - 0.7.4-1
- new version

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 0.7.3-1
- Latest upstream with support for zmq reconnect options.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Ralph Bean <rbean@redhat.com> - 0.7.2-1
- Latest upstream with python3 support -- woot, woot!

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- Latest upstream.
- Dropped support for older pyzmq.

* Tue Jan 14 2014 Ralph Bean <rbean@redhat.com> - 0.6.2-3
- Narrow dep down to the twisted-core subpackage.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Ralph Bean <rbean@redhat.com> - 0.6.2-1
- Latest upstream including our patches.
- Removed patches 2 through 5 for pyzmq compat.

* Wed Mar 27 2013 Ralph Bean <rbean@redhat.com> - 0.6.1-5
- Added three patches to support old and new pyzmq.
- More explicit file ownership in %%{python_sitelib}.
- Removed some trailing whitespace.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-3
- Patch to add support for tcp keepalives with zeromq3.
- Fixed "bad" rhel conditional.

* Mon Oct 29 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-2
- Patch (again) to support older pyzmq on f17 and el6.

* Mon Oct 29 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- Upstream integrates zeromq3 support.  Dropping patches.

* Wed Oct 10 2012 Ralph Bean <rbean@redhat.com> - 0.5.2-3
- Patch to support older pyzmq on f17 and el6.
- Fix changelog.

* Wed Oct 10 2012 Ralph Bean <rbean@redhat.com> - 0.5.2-2
- Added three patches to support zeromq3.

* Tue Oct 02 2012 Ralph Bean <rbean@redhat.com> - 0.5.2-1
- Latest upstream with new socket types.
- Remove old epgm-disabling patch.
- Add new egpm-disabling patch.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Ralph Bean <rbean@redhat.com> - 0.5.0-2
- Patch out setuptools dep on Twisted for epel.

* Mon May 21 2012 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- Removed FSF address patch.
- Packaged new upstream version.
- Replaced txZMQ with %%{modname}

* Mon Apr 09 2012 Ralph Bean <rbean@redhat.com> - 0.3.1-2
- Changed BuildRequires python-devel to python2-devel.
- Dropped the %%defattr macro .
- Patched to disable the EPGM test.  libpgm isn't packaged for fedora yet.
- Added %%check section to run nosetests.

* Thu Apr 05 2012 Ralph Bean <rbean@redhat.com> - 0.3.1-1
- initial package for Fedora
