%global pypi_name pelican
Name:           python-%{pypi_name}
Version:        4.8.0
Release:        9%{?dist}
Summary:        A tool to generate a static blog from reStructuredText or Markdown input files

# Automatically converted from old format: AGPLv3
License:        AGPL-3.0-only
URL:            http://getpelican.com
Source0:        https://github.com/getpelican/pelican/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

# https://github.com/getpelican/pelican/commit/33aca76d78601f0f0da635c8a14c89bbbc9ff8d6.patch
# this patch was rebased on pelican-4.8.0:
Patch0001: adjust-extlinks-sphinx5.patch

%description
Pelican is a static site generator, written in Python_.

* Write your weblog entries directly with your editor of choice (vim!)
  in reStructuredText_ or Markdown_
* Includes a simple CLI tool to ...

%package -n python3-%{pypi_name}
Summary:        A tool to generate a static blog from reStructuredText or Markdown input files

Obsoletes:      python-%{pypi_name} < 3.7.1-4
Obsoletes:      python2-%{pypi_name} < 3.7.1-4
Conflicts:      python2-%{pypi_name} < 3.7.1-4
Provides:       %{pypi_name} == %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-blinker
BuildRequires:  python3-sphinx
BuildRequires:  python3-unidecode
BuildRequires:  python3-rich

BuildRequires:  python3-markdown
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-lxml
BuildRequires:  python3-six
BuildRequires:  python3-pytz
BuildRequires:  python3-jinja2
BuildRequires:  python3-feedgenerator
BuildRequires:  python3-dateutil

BuildRequires:  python3-pygments
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-xdist
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/diff

Requires:  python3-blinker
Requires:  python3-six
Requires:  python3-unidecode
Requires:  python3-jinja2
Requires:  python3-pytz
Requires:  python3-pygments
Requires:  python3-docutils
Requires:  python3-markdown
Requires:  python3-feedparser
Requires:  python3-dateutil
Requires:  python3-feedgenerator


%description -n python3-%{pypi_name}
Pelican is a static site generator, written in Python_.

* Write your weblog entries directly with your editor of choice (vim!)
  in reStructuredText_ or Markdown_
* Includes a simple CLI tool to ...


%prep
%autosetup -p1 -S git -n %{pypi_name}-%{version}
# make file not zero length to silence rpmlint
echo " " > pelican/themes/simple/templates/tag.html

# remove bangpath #!/usr/bin/env from files
sed -i '1d' pelican/tools/pelican_import.py
sed -i '1d' pelican/tools/pelican_quickstart.py
sed -i '1d' pelican/tools/pelican_themes.py
sed -i '1d' pelican/tools/templates/pelicanconf.py.jinja2
sed -i '1d' pelican/tools/templates/publishconf.py.jinja2

# release pytz constraints
sed -i "s|'pytz >= 0a'|'pytz'|" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# build docs
PYTHONPATH=.:$PYTHONPATH sphinx-build-3 docs html

# remove leftovers from sphinxbuild
rm html/_downloads/*/theme-basic.zip html/_static/theme-basic.zip
rm -rf html/.doctrees html/.buildinfo


%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# backwards compatibility helpers
ln -s ./pelican %{buildroot}/%{_bindir}/pelican-3
ln -s ./pelican-import %{buildroot}/%{_bindir}/pelican-import-3
ln -s ./pelican-quickstart %{buildroot}/%{_bindir}/pelican-quickstart-3
ln -s ./pelican-themes %{buildroot}/%{_bindir}/pelican-themes-3



%check
# re-checked tests, upstream is on python3.8, we are using 3.9.
# pytest -s --cov=pelican pelican

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc html README.rst
%license LICENSE

%{_bindir}/pelican
%{_bindir}/pelican-import
%{_bindir}/pelican-plugins
%{_bindir}/pelican-quickstart
%{_bindir}/pelican-themes

%{_bindir}/pelican-3
%{_bindir}/pelican-import-3
%{_bindir}/pelican-quickstart-3
%{_bindir}/pelican-themes-3



%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 4.8.0-8
- convert license to SPDX

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 4.8.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Maxwell G <maxwell@gtmx.me> - 4.8.0-4
- Remove unused python3-mock test dependency

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 4.8.0-2
- Rebuilt for Python 3.12

* Wed Apr 12 2023 Matthias Runge <mrunge@redhat.com> - 4.8.0-1
- update to 4.8.0, resolves rhbz#2180476, rhbz#1941973

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.7.2-1
- Updated to version 4.7.2.

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.5.4-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.5.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Matthias Runge <mrunge@redhat.com> - 4.5.4-1
- update to 4.5.4 (rhbz#1912541)

* Mon Jan 04 2021 Matthias Runge <mrunge@redhat.com> - 4.5.3-1
- rebase to 4.5.3 (rhbz#1870731)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.2.0-1
- 4.2.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 4.0.1-1
- 4.0.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7.1-7
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Matthias Runge <mrunge@redhat.com> - 3.7.1-6
- fix python2/python3 bangpath issue (rhbz#1546755)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Miro Hrončok <mhroncok@redhat.com> - 3.7.1-4
- Remove the python2 subpackage (rhbz#1487848)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Matěj Cepl <mcepl@redhat.com> - 3.7.1-2
- Make build working even on EPEL7

* Thu Feb 23 2017 Matthias Runge <mrunge@redhat.com> - 3.7.1-1
- update to 3.7.1 (rhbz#1426053)

* Wed Feb 08 2017 Matthias Runge <mrunge@redhat.com> - 3.7.0-2
- remove python requirements to feedgenerator (rhbz#1379149)

* Tue Jan 03 2017 Matthias Runge <mrunge@redhat.com> - 3.7.0-1
- update to 3.7.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.6.3-7
- Rebuild for Python 3.6

* Wed Aug 03 2016 Matthias Runge <mrunge@redhat.com> - 3.6.3-6
- rename python3 executables (rhbz#1362516)
- modernize spec file

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.3-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Matthias Runge <mrunge@redhat.com> - 3.6.3-3
- properly provide python2-pelican (rhbz#1282229)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5


* Wed Nov 04 2015 Matthias Runge <mrunge@redhat.com> - 3.6.3-1
- update to 3.6.3

* Mon Jun 22 2015 Matthias Runge <mrunge@redhat.com> - 3.6.0-1
- update to 3.6.0
- add python3 support (rhbz#1227982)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Matthias Runge <mrunge@redhat.com> - 3.5.0-3
- change requirements for pytz

* Mon Mar 23 2015 Matthias Runge <mrunge@redhat.com> - 3.5.0-2
- add runtime requirement python-dateutil(rhbz#1204791)

* Tue Mar 10 2015 Matthias Runge <mrunge@redhat.com> - 3.5.0-1
- update to 3.5.0 (rhbz#1200030)

* Mon Sep 01 2014 Matthias Runge <mrunge@redhat.com> - 3.4.0-1
- update to 3.4.0
- add requires: python-feedparser (rhbz#1135665)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.3.0-4
- add Requires: python-markdown

* Wed Feb 05 2014 Matthias Rugne <mrunge@redhat.com> - 3.3.0-3
- use __python2 instead of __python
- use a tarball from github, as it significantly differs from pypi
- add tests
- build docs


* Sat Jan 25 2014 Matthias Runge <mrunge@redhat.com> - 3.3-1
- Initial package.
