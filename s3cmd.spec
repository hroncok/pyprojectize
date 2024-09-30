%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%define	name	s3cmd
%define	version	2.4.0
%define	release	4

Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Tool for accessing Amazon Simple Storage Service

License:        GPL-2.0-or-later
URL:            https://s3tools.org/%{name}
Source0:        https://github.com/s3tools/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python3}
BuildRequires:  python3-devel
Requires:       python3-dateutil
Requires:       python3-magic

# Disable auto dependencies as sources match Python2
%{?python_disable_dependency_generator}
%else
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       python-dateutil
Requires:       python-magic
%else
Requires:       python2-dateutil
Requires:       python2-magic
%endif
%endif

%description
S3cmd lets you copy files from/to Amazon S3
(Simple Storage Service) using a simple to use
command line client.

%prep
%setup -q
rm -rf *.egg-info
%if %{without python3}
# Not needed on Py2, RPM fails to Bytecompile it
rm -f S3/Custom_httplib3x.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
export S3CMD_PACKAGING=1
%if %{with python3}
%pyproject_wheel
%else
%py2_build
%endif

%install
export S3CMD_PACKAGING=1
%if %{with python3}
%pyproject_install
%pyproject_save_files S3
%else
%py2_install
%endif

mkdir -p %{buildroot}%{_mandir}/man1
install -D -p -m 0644 -t %{buildroot}%{_mandir}/man1 %{name}.1

%files -f %{pyproject_files}
%license LICENSE
%doc NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%if %{with python3}
%else
%{python2_sitelib}/%{name}-*.dist-info/
%{python2_sitelib}/S3/
%endif

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 15 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.4.0-1
- New upstream release.

* Thu Nov 16 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.3.0^20231020gita2b1bdf-1
- Upgraded to latest snapshot as fix for BZ2249487.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.3.0-5
- Rebuilt for Python 3.12

* Sat Feb 04 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.3.0-4
- Rebuilt to change Python shebangs to /usr/bin/python3.6 on EPEL 8

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.3.0-2
- SPDX license update

* Tue Oct 04 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.3.0-1
- New upstream release.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.2.0-2
- Fix auto dependency regression for EPEL9

* Mon Sep 27 2021 Frank Crawford <frank@crawford.emu.id.au> - 2.2.0-1
- New upstream release.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 05 2020 Frank Crawford <frank@crawford.emu.id.au> - 2.1.0-5
- Futher fixes for Python 3.9

* Sat Oct 03 2020 Frank Crawford <frank@crawford.emu.id.au> - 2.1.0-4
- Fix for Python 3.9 (RHBZ #1884607)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.9

* Sun Apr 26 2020 Frank Crawford <frank@crawford.emu.id.au> - 2.1.0-1
- New upstream release.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 2019 Frank Crawford <frank@crawford.emu.id.au> - 2.0.2-7
- Build for EPEL8 (#1784445)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 2019 Frank Crawford <frank@crawford.emu.id.au> - 2.0.2-3
- Disable python automatic dependency generator due to issues with python3-magic

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- Update URL
- Fixes in packaging
- Update License

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 (rhbz #1533676)

* Sun Oct 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.1-2
- Switch to python3

* Sun Oct 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 (rhbz #1505145)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-2
- Revert Py3 support for Fedora, it's not production ready.

* Sun Jul 02 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-1
- Cleanup the specfile / remove EL5 bits
- Remove Amazon Linux workaround (s3cmd is now compatible w/ py 2.7)
- Use py3 for Fedora package

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Matt Domsch <mdomsch@fedoraproject.org> 1.6.1-1
- upstream 1.6.1
- conditionalize el6 test to keep same spec across all branches

* Tue Dec 15 2015 Matt Domsch <mdomsch@fedoraproject.org> 1.6.0-3
- try again to force python 2.6 executable for EPEL 6.

* Mon Dec  7 2015 Matt Domsch <mdomsch@fedoraproject.org> 1.6.0-2
- force python 2.6 executable for EPEL 6. Amazon Linux 6 default python is 2.7.

* Fri Sep 18 2015 Matt Domsch <mdomsch@fedoraproject.org> 1.6.0-1
- upstream 1.6.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb  5 2015 Matt Domsch <mdomsch@fedoraproject.org> - 1.5.1.2-5
- add Requires: python-magic

* Wed Feb  4 2015 Matt Domsch <mdomsch@fedoraproject.org> - 1.5.1.2-4
- upstream 1.5.1.2, mostly bug fixes
- remove ez_setup, add dependency on python-setuptools

* Mon Jan 12 2015 Matt Domsch <mdomsch@fedoraproject.org> - 1.5.0-1
- upstream 1.5.0 final

* Tue Jul  1 2014 Matt Domsch <mdomsch@fedoraproject.org> - 1.5.0-0.7.rc1
- put back dropped dist tag

* Tue Jul  1 2014 Matt Domsch <mdomsch@fedoraproject.org> - 1.5.0-0.6.rc1
- upstream 1.5.0-rc1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.5.gitb196faa5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Matt Domsch <mdomsch@fedoraproject.org> - 1.5.0-0.4.git
- upstream 1.5.0-beta1 plus even newer upstream fixes

* Sun Feb 02 2014 Matt Domsch <mdomsch@fedoraproject.org> - 1.5.0-0.3.git
- upstream 1.5.0-beta1 plus newer upstream fixes

* Wed May 29 2013 Matt Domsch <mdomsch@fedoraproject.org> - 1.5.0-0.2.gita122d97
- more upstream bugfixes
- drop pyxattr dep, that codepath got dropped in this release

* Mon May 20 2013 Matt Domsch <mdomsch@fedoraproject.org> - 1.5.0-0.1.gitb1ae0fbe
- upstream 1.5.0-alpha3 plus fixes
- add dep on pyxattr for the --xattr option

* Tue Jun 19 2012 Matt Domsch <mdomsch@fedoraproject.org> - 1.1.0-0.4.git11e5755e
- add local MD5 cache

* Mon Jun 18 2012 Matt Domsch <mdomsch@fedoraproject.org> - 1.1.0-0.3.git7de0789d
- parallelize local->remote syncs

* Mon Jun 18 2012 Matt Domsch <mdomsch@fedoraproject.org> - 1.1.0-0.2.gitf881b162
- add hardlink / duplicate file detection support

* Fri Mar  9 2012 Matt Domsch <mdomsch@fedoraproject.org> - 1.1.0-0.1.git2dfe4a65
- build from git for mdomsch patches to s3cmd sync

* Thu Feb 23 2012 Dennis Gilmore <dennis@ausil.us> - 1.0.1-1
- update to 1.0.1 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 05 2011 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.0.0-3
- No hashlib hackery

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.0.0-1
- New upstream release

* Mon Nov 29 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.9.9.91-3
- Patch for broken f14 httplib

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.9.91-2.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Apr 28 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.9.9.91-1.1
- Do not use sha1 from hashlib

* Sun Feb 21 2010 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.9.91-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.9-1
- New upstream release

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.8.4-2
- Rebuild for Python 2.6

* Tue Nov 11 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.4-1
- New upstream release, URI encoding patch upstreamed

* Fri Sep 26 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.3-4
- Try 3/65536

* Fri Sep 26 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.3-3
- Whoops, forgot to actually apply the patch.

* Fri Sep 26 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.3-2
- Fix listing of directories with special characters in names

* Thu Jul 31 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.3-1
- New upstream release: Avoid running out-of-memory in MD5'ing large files.

* Fri Jul 25 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.2-1.1
- Fix a typo

* Tue Jul 15 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.2-1
- New upstream

* Fri Jul 04 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.1-3
- Be satisfied with ET provided by 2.5 python

* Fri Jul 04 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.1-2
- Added missing python-devel BR, thanks to Marek Mahut
- Packaged the Python egg file

* Wed Jul 02 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.8.1-1
- Initial packaging attempt
