%global         srcname  inema
%global         desc     This is a python module for interfacing the "Internetmarke" API provided by the\
German postal company "Deutsche Post". It implements V3 of this API.\
\
The Internetmarke API allows you to buy online franking for national and\
international postal products like post cards and letters of all weight\
classes and service classes (normal, registered, ...).

Name:           python-%{srcname}
Version:        0.8.10
Release:        4%{?dist}
Summary:        A Python interface to the Deutsche Post Internetmarke Online Franking

License:        LGPL-3.0-or-later
URL:            http://git.sysmocom.de/python-inema/
Source0:        %pypi_source

BuildArch:      noarch

# required for py3_build macro
BuildRequires:  python3-devel


# from setup.py
BuildRequires: python3-pytz
BuildRequires: python3-zeep

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
sed -i '1,1s@^#!.*$@@' inema/frank.py inema/inema.py
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/frank
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.10-3
- convert license to SPDX

* Thu Jun 27 2024 Python Maint <python-maint@redhat.com> - 0.8.10-2
- Rebuilt for Python 3.13

* Wed May 29 2024 Georg Sauthoff <mail@gms.tf> - 0.8.10-1
- Bump to upstream release (includes July, 2024 product updates, fixes fedora#2283711)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Georg Sauthoff <mail@gms.tf> - 0.8.9-1
- Update to latest release that fixes BüWa shipment prices in 2024 (fixes fedora#2256295)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.8.8-2
- Rebuilt for Python 3.12

* Sat May 27 2023 Georg Sauthoff <mail@gms.tf> - 0.8.8-1
- Update to latest upstream release because of product list and license changes
  (fixes fedora#2210419).

* Sun Jan 22 2023 Georg Sauthoff <mail@gms.tf> - 0.8.7-1
- Update to latest upstream release (because of product list changes)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Georg Sauthoff <mail@gms.tf> - 0.8.6-1
- Update to latest upstream release (removes discontinued products)

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.8.5-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Georg Sauthoff <mail@gms.tf> - 0.8.5-1
- Bump to latest upstream release (include price changes for 2022)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.4-2
- Rebuilt for Python 3.10

* Sat May  1 2021 Georg Sauthoff <mail@gms.tf> - 0.8.4-1
- Bump to latest upstream release (supports discount prices and new warenpost API)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 Georg Sauthoff <mail@gms.tf> - 0.8.3-1
- Bump to latest upstream release (COVID-19 VAT reduction ends and some other product changes happened)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Georg Sauthoff <mail@gms.tf> - 0.8.2-2
- Be more explicit regarding setuptools depenency,
  cf. https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/

* Fri Jun 26 2020 Georg Sauthoff <mail@gms.tf> - 0.8.2-1
- Bump to latest upstream release (COVID-19 VAT updates)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Georg Sauthoff <mail@gms.tf> - 0.8.1-2
- Fix changelog date

* Sun Dec 08 2019 Georg Sauthoff <mail@gms.tf> - 0.8.1-1
- Update to latest upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Georg Sauthoff <mail@gms.tf> - 0.8-1
- Update to latest upstream version
* Wed Mar 27 2019 Georg Sauthoff <mail@gms.tf> - 0.6-1
- initial packaging
