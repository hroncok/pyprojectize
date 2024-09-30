%global pypi_name Scrapy
%global pkg_name scrapy
Name:		python-scrapy
Version:	2.11.2
Release:	2%{?dist}
Summary:	A high-level Python Screen Scraping framework
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://scrapy.org
# TODO fix Source0 to correct github source URL
Source0:	https://files.pythonhosted.org/packages/f2/1f/5524416a64c030fbe18caeba079e7176836b281bf9eb50b79efdf8015063/scrapy-2.11.2.tar.gz
BuildArch:	noarch


%description
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.


%package -n python3-%{pkg_name}
Summary:	%{summary}

BuildRequires: make
BuildRequires:	python3-devel
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	python3-cssselect
BuildRequires:	python3-lxml
BuildRequires:	python3-twisted
BuildRequires:	python3-w3lib
BuildRequires:	python3-queuelib
BuildRequires:	python3-sphinx-hoverxref
BuildRequires:	python3-sphinx-notfound-page
BuildRequires:	python-tldextract
BuildRequires:	python3-service-identity
BuildRequires:	python3-parsel
BuildRequires:	python3-itemadapter
BuildRequires:	python3-itemloaders
BuildRequires:	python3-pydispatcher
BuildRequires:	python3-pyOpenSSL
BuildRequires:	python3-cryptography 
Requires:	python3-pyOpenSSL
Requires:	python3-twisted
Requires:	python3-lxml
Requires:	python3-w3lib
Requires:	python3-queuelib
Requires:	python3-zope-interface
Requires:	python3-cssselect
Requires:	python3-pydispatcher
Requires:	python3-parsel
Requires:	python3-itemadapter
Requires:	python3-protego
Requires:	python3-itemloaders
Requires:	python3-pydispatcher
Requires:	python-tldextract
Requires:	python3-service-identity
Requires:	python3-cryptography 



%description -n python3-%{pkg_name}
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.



%package doc
Summary:	Documentation for %{name}

%description doc
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.
This package contains the documentation for %{name}

%prep
%autosetup -n %{pkg_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Removing docs temporarily because is not compatible with sphinx 7.2.x
#PYTHONPATH=$(pwd) make -C docs html
#%make_build PYTHONPATH=$(pwd) -C docs html
#rm -f docs/build/html/.buildinfo

%install
%pyproject_install


%files -n python3-%{pkg_name}
%license LICENSE
%doc AUTHORS PKG-INFO
%{python3_sitelib}/scrapy
%{python3_sitelib}/Scrapy-*.dist-info
%{_bindir}/scrapy

#%files doc
#%doc docs/build/html

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.11.2-2
- convert license to SPDX

* Wed Jul 17 2024 Filipe Rosset <rosset.filipe@gmail.com> - 2.11.2-1
- Update to 2.11.2

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.11.0-2
- Rebuilt for Python 3.13

* Sun Feb 4 2024 Eduardo Echeverria <echevemaster@gmail.com> - 2.11.0-1
- Update to 2.11.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 09 2023 Filipe Rosset <rosset.filipe@gmail.com> - 2.10.1-1
- Update to 2.10.1 fixes rhbz#2110522 rhbz#2220494 and rhbz#2159992

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 2.8.0-2
- Rebuilt for Python 3.12

* Tue Feb 21 2023 Eduardo Echeverria <echevemaster@gmail.com> - 2.8.0-1
- Update to 2.8.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.6.1-2
- Rebuilt for Python 3.11

* Mon Mar 7 2022 Eduardo Echeverria <echevemaster@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.1-4
- Rebuilt for Python 3.10

* Wed Apr 7 2021 Eduardo Echeverria <echevemaster@gmail.com> - 2.4.1-3
- Added missing requires

* Sun Mar 14 2021 Eduardo Echeverria <echevemaster@gmail.com> - 2.4.1-2
- Fixes 

* Sun Feb 28 2021 Eduardo Echeverria <echevemaster@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Eduardo Echeverria  <echevemaster@gmail.com> - 1.5.1-2
- Remove python2-scrapy as part of this process https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 13 2018 Eduardo Echeverria  <echevemaster@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Update to 1.5.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.5.0-1
- Rebuilt for new upstream release 1.5.0, fixes rhbz #1431310
- Fixes rhbz #1478686 and rhbz #1507308

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jan Beran <jberan@redhat.com> - 1.3.2-1
- Update to the latest upstream version
- Provides python 3 subpackage

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 1 2015 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.3-1
- Update to the latest upstream version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 5 2014 Eduardo Echeverria  <echevemaster@gmail.com> - 0.24.4-1
- Update to the latest upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 19 2014 Eduardo Echeverria  <echevemaster@gmail.com> - 0.22.0-1
- Update to the latest upstream version

* Sun Jan 19 2014 Eduardo Echeverria  <echevemaster@gmail.com> - 0.20.2-1
- Initial packaging
