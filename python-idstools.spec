# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%global		upstream_name	py-idstools
%global		pname		idstools

Name:		python-%{pname}
Version:	0.6.5
Release:	6%{?dist}
Summary:	Snort and Suricata Rule and Event Utilities
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/jasonish/py-idstools
Source0:	https://github.com/jasonish/py-idstools/archive/%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
BuildArch:	noarch

%global desc_base \
	py-idstools is a collection of Python libraries for working with IDS systems\
	(typically Snort and Suricata).


%description
%{desc_base}


%package -n python%{python3_pkgversion}-%{pname}
Summary:	%{summary} for Python3
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pname}}
Conflicts:	python2-%{pname} < 0.6.3-7

BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-setuptools
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:	python%{python3_pkgversion}-pytest
%else
BuildRequires:	python%{python3_pkgversion}-nose
%endif
Requires:	python%{python3_pkgversion}-dateutil

%description -n python%{python3_pkgversion}-%{pname}
%{desc_base} For Python3.


%prep
%setup -q -n %{upstream_name}-%{version}
pushd tests
popd
# remove bundled libraries
%{__rm} -rf idstools/compat
%{__sed} -i '/compat/d' setup.py


%build
%{py3_build}


%install
%{py3_install}

%check
%if 0%{?fedora} || 0%{?rhel} > 7
%pytest
%else
%{__python3} setup.py nosetests
%endif


%files -n python%{python3_pkgversion}-%{pname}
%{_bindir}/%{pname}-dumpdynamicrules
%{_bindir}/%{pname}-eve2pcap
%{_bindir}/%{pname}-gensidmsgmap
%{_bindir}/%{pname}-rulecat
%{_bindir}/%{pname}-rulemod
%{_bindir}/%{pname}-u2eve
%{_bindir}/%{pname}-u2fast
%{_bindir}/%{pname}-u2json
%{_bindir}/%{pname}-u2spewfoo
%{python3_sitelib}/%{pname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pname}
%doc README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.5-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.5-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 02 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 0.6.5-1
- New upstream release

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.4-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.4-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 0.6.4-5
- Patch for failed test with python 3.11

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 0.6.4-1
- New upstream release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 0.6.3-13
- Add explicit python3-setuptools br

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-7
- Subpackage python2-idstools has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-4
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Marcin Dulak <marcindulak@fedoraproject.org> - 0.6.3-1
- upstream update
- added dumpdynamicrules and u2spewfoo under bindir

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Marcin Dulak <marcindulak@fedoraproject.org> - 0.6.1-2
- default to python2 scripts

* Thu May 25 2017 Marcin Dulak <marcindulak@fedoraproject.org> - 0.6.1-1
- upstream update

* Sat Apr 01 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0 (#1430163)

* Wed Mar 08 2017 Marcin Dulak <marcindulak@fedoraproject.org> - 0.5.6-5
- upstream update
- install python2 and python3 scripts, see bug #1430020

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-3
- Rebuild for Python 3.6

* Fri Dec 09 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 0.5.4-2
- use %%{python3_pkgversion}, see bug #1336097

* Thu Nov 24 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 0.5.4-1
- initial package
