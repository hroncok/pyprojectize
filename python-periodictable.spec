%global pname periodictable

%global middle_release 0
%if 0%{?middle_release}
%global  commit      bc922958444c721475bd412f9c38c1589cfc1fb8
%global  date        .20220518git
%global  shortcommit %(c=%{commit}; echo ${c:0:8})
%else
%global  commit      %{nil}
%global  date        %{nil}
%global  shortcommit %{nil}
%endif

%bcond_without check

%global _description %{expand:
This package provides a periodic table of the elements
with support for mass, density and xray/neutron
scattering information.

Masses, densities and natural abundances come from
the NIST Physics Laboratory, but do not represent a
critical evaluation by NIST scientists.

Neutron scattering calculations use values collected
by the Atomic Institute of the Austrian Universities.
These values do corresponding to those from other packages,
though there are some differences depending to the tables used.
Bound coherent neutron scattering for gold in particular is
significantly different from older value: 7.63(6) as 
easured in 1974 compared to 7.90(7) as measured in 1990.

X-ray scattering calculations use a combination of empirical
and theoretical values from the LBL Center for X-ray Optics.
These values differ from those given in other sources such as
the International Tables for Crystallography, Volume C, and so
may give different results from other packages.}

Name:           python-%{pname}
Version:        1.6.1
Release:        11%{date}%{shortcommit}%{?dist}
Summary:        Extensible periodic table of the elements

# periodictable/cromermann.py: BSD 3-clause "New" or "Revised" License
# https://github.com/pkienzle/periodictable/issues/30
# Automatically converted from old format: Public Domain and BSD - review is highly recommended.
License:        LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-BSD
URL:            http://www.reflectometry.org/danse/elements.html
%if 0%{?middle_release}
Source0:        https://github.com/pkienzle/%{pname}/archive/%{commit}/%{pname}-%{commit}.tar.gz
%else
Source0:        https://github.com/pkienzle/%{pname}/archive/v%{version}/%{pname}-%{version}.tar.gz
%endif
BuildArch:      noarch
Patch0:         %{name}-remove_unrecognized_flag.patch

%description
%{_description}.

%package -n python%{python3_pkgversion}-%{pname}
Summary: Extensible periodic table of the elements

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pyparsing

%description -n python%{python3_pkgversion}-%{pname}
%{_description}.


%prep
%autosetup -n %{pname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with check}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v
%endif

%files -n python%{python3_pkgversion}-%{pname}
%{python3_sitelib}/*egg-info/
%{python3_sitelib}/%{pname}/

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.1-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.6.1-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.1-2
- Rebuilt for pyparsing-3.0.9

* Fri Jun 24 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.6.1-1
- Release 1.6.1

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.3-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.5.3-1
- Release 1.5.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.5.2-4
- Switch to pytest

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-3
- Rebuilt for Python 3.9

* Tue Mar 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.5.2-2
- Switch to pytest

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.5.2-1
- First release
