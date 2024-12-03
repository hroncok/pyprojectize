%global         hguser         techtonik
%global         srcname        hexdump
# 2016-08-18
%global         commit         66325cb5fed890df4a345e25ea8f107fd31b60d8
%global         commitdate     20160818
%global         shortcommit    %(c=%{commit}; echo ${c:0:12})


Name:           python-hexdump
Version:        3.4
Release:        0.26.%{commitdate}hg%{shortcommit}%{?dist}
Summary:        Dump binary data to hex format and restore from there

License:        Public Domain
#               https://pypi.python.org/pypi/hexdump
#               https://bitbucket.org/techtonik/hexdump
URL:            https://bitbucket.com/%{hguser}/%{srcname}
Source0:        https://bitbucket.org/%{hguser}/%{srcname}/get/%{shortcommit}.zip#/%{name}-%{version}-%{shortcommit}.zip
Source1:        hexdumpy.1

# Create the /usr/bin/hexdumpy
# https://bitbucket.org/techtonik/hexdump/pull-requests/5/modify-the-setuppy-in-order-to-generate/diff
Patch0:         %{name}-setup.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%description
Python library to dump binary data to hex format and restore from there



%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Dump binary data to hex format and restore from there

%description -n python%{python3_pkgversion}-%{srcname}
Python library to dump binary data to hex format and restore from there



%prep
%setup -q -n %{hguser}-%{srcname}-%{shortcommit}
%patch -P0 -p 1 -b .setup
sed -i -e 's|#!/usr/bin/env python|#|' hexdump.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*'

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/hexdumpy.1

%check
%pyproject_check_import

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license UNLICENSE
%doc README.txt
%{_bindir}/hexdumpy
%{_mandir}/man1/hexdumpy.1*



%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.26.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.4-0.25.20160818hg66325cb5fed8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.24.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.23.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.22.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.4-0.21.20160818hg66325cb5fed8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.20.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.19.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.4-0.18.20160818hg66325cb5fed8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.17.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.16.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.4-0.15.20160818hg66325cb5fed8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.14.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.13.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4-0.12.20160818hg66325cb5fed8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.11.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4-0.10.20160818hg66325cb5fed8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4-0.9.20160818hg66325cb5fed8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.8.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.7.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.4-0.6.20160818hg66325cb5fed8
- Subpackage python2-hexdump has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.5.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4-0.4.20160818hg66325cb5fed8
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.4-0.3.20160818hg66325cb5fed8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 4 2018 Michal Ambroz <rebus _AT seznam.cz> - 3.4-0.2.20160818hg66325cb5fed8
- fix python package directory based on package review

* Wed Dec 13 2017 Michal Ambroz <rebus _AT seznam.cz> - 3.4-0.1.20160818hg66325cb5fed8
- fixes during the package review, fix versioning, add manpage

* Wed Oct 04 2017 Michal Ambroz <rebus _AT seznam.cz> - 3.3-1
- Initial package for Fedora
