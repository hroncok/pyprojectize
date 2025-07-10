%global modname pygeoip

Name:               python-pygeoip
Version:            0.2.6
Release:            39%{?dist}
Summary:            Pure Python GeoIP API
License:            LGPL-3.0-or-later
URL:                http://pypi.python.org/pypi/pygeoip
Source0:            http://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.zip

BuildArch:          noarch

BuildRequires:      GeoIP
BuildRequires:      python3-devel
BuildRequires:      python3-nose

%global _description\
Pure Python GeoIP API based on MaxMind's C-based Python API\
but the code itself is ported from the Pure PHP GeoIP API.\
\
Create your GeoIP instance with appropriate access flag. `STANDARD` reads\
data from disk when needed, `MEMORY_CACHE` loads database into memory on\
instantiation and `MMAP_CACHE` loads database into memory using mmap.\
\
    import pygeoip\
    gi = pygeoip.GeoIP('/usr/share/geoip/GeoIP.dat', pygeoip.MEMORY_CACHE)\
\
Country lookup\
\
    >>> gi.country_code_by_name('google.com')\
    'US'\
    >>> gi.country_code_by_addr('64.233.161.99')\
    'US'\
    >>> gi.country_name_by_addr('64.233.161.99')\
    'United States'\
\
City lookup\
\
    >>> gi = pygeoip.GeoIP('/usr/share/geoip/GeoLiteCity.dat')\
    >>> gi.record_by_addr('64.233.161.99')\
    {\
        'city': 'Mountain View',\
        'region_name': 'CA',\
        'area_code': 650,\
        'longitude': -122.0574,\
        'country_code3': 'USA',\
        'latitude': 37.419199999999989,\
        'postal_code': '94043',\
        'dma_code': 807,\
        'country_code': 'US',\
        'country_name': 'United States'\
    }\
    >>> gi.time_zone_by_addr('64.233.161.99')\
    'America/Los_Angeles'\
\
For more information, check out the full API documentation at\
http://packages.python.org/pygeoip.

%description %_description

%package -n python3-pygeoip
Summary:            Pure Python GeoIP API

# While this doesn't strictly require geoip-geolite, it only makes sense
# that you would install it alongside this module.
Requires:           geoip-geolite

%description -n python3-pygeoip %_description

%prep
%setup -q -n %{modname}-%{version}


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}

## The tests require some files not in sdist
# FileNotFoundError: [Errno 2] No such file or directory:
# '/builddir/build/BUILD/pygeoip-0.2.6/tests/data/GeoIPASNum.dat'
#%%check
#PYTHONPATH=$(pwd) nosetests-3

%check
%pyproject_check_import

%files -n python3-pygeoip -f %{pyproject_files}
%doc README.md COPYING DEVELOPER INSTALL apidocs/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.6-38
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.6-37
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.6-33
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.6-30
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.6-27
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-18
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.6-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.6-13
- Python 2 binary package renamed to python2-pygeoip
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Ralph Bean <rbean@redhat.com> - 0.2.6-5
- Pull in GeoIP instead of geoip-geolite (el7).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Ralph Bean <rbean@redhat.com> - 0.2.6-1
- Latest upstream release
- Now including docs, license, readme, and tests.
- Tests are disabled until data is available
  https://bugzilla.redhat.com/show_bug.cgi?id=910233

* Mon Feb 11 2013 Ralph Bean <rbean@redhat.com> - 0.2.5-1
- Initial package for Fedora.
