%global module cornice
%global desc Helpers to build & document Web Services with Pyramid.

Name:             python-cornice
Version:          6.0.1
Release:          12%{?dist}
BuildArch:        noarch

License:          MPL-2.0
Summary:          Define Web Services in Pyramid
URL:              https://pypi.python.org/pypi/cornice
Source0:          https://github.com/Cornices/cornice/archive/%{version}/%{module}-%{version}.tar.gz

# Use TestCase.assertTrue() instead of TestCase.assert_()
#
# The assert_() method is deprecated and will be removed in Python 3.12.
# https://github.com/Cornices/cornice/pull/575
Patch:            https://github.com/Cornices/cornice/pull/575.patch

BuildRequires: %{py3_dist colander}
BuildRequires: %{py3_dist coverage}
BuildRequires: %{py3_dist pyramid} >= 1.7
BuildRequires: %{py3_dist simplejson}
BuildRequires: %{py3_dist sphinx}
BuildRequires: %{py3_dist venusian}
BuildRequires: %{py3_dist webtest}
BuildRequires: python3-devel
BuildRequires: python3-pytest


%description
%{desc}


%package -n python3-cornice
Summary:          %{summary}

Recommends: %{py3_dist colander}
Requires:   %{py3_dist pyramid} >= 1.7
Requires:   %{py3_dist simplejson}
Requires:   %{py3_dist six}
Requires:   %{py3_dist venusian}



%description -n python3-cornice
%{desc}


%prep
%autosetup -p1 -n %{module}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l '%{module}*'


%check
%pyproject_check_import
%pytest -v


%files -n python3-cornice -f %{pyproject_files}
%doc CHANGES.txt CONTRIBUTORS.txt README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Python Maint <python-maint@redhat.com> - 6.0.1-11
- Rebuilt for Python 3.13

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 6.0.1-10
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 6.0.1-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Mattia Verga <mattia.verga@proton.me> - 6.0.1-4
- Rebuilt for Pyramid 2.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 6.0.1-2
- Rebuilt for Python 3.11

* Sun May 29 2022 Kevin Fenzi <kevin@scrye.com> - 6.0.1-1
- Update to 6.0.1. Fixes rhbz#2008918

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 08 2021 Kevin Fenzi <kevin@scrye.com> - 5.2.0-1
- Update to 5.2.0. Fixes rhbz#1946508

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.1.0-2
- Rebuilt for Python 3.10

* Fri Mar 19 2021 Charalampos Stratakis <cstratak@redhat.com> - 5.1.0-1
- Update to 5.1.0 (rhbz#1930259)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Kevin Fenzi <kevin@scrye.com> - 5.0.3-1
- Update to 5.0.3. Fixes rhbz#1838126

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1 (#1778705).
- https://github.com/Cornices/cornice/blob/4.0.1/CHANGES.txt

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1 (#1771947).
- https://github.com/Cornices/cornice/blob/3.6.1/CHANGES.txt

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0 (#1742282).
- https://github.com/Cornices/cornice/blob/3.6.0/CHANGES.txt

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1 (#1669103).
- https://github.com/Cornices/cornice/blob/3.5.1/CHANGES.txt

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-2
- Subpackage python2-cornice has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 23 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0 (#1543660).
- https://github.com/Cornices/cornice/blob/3.4.0/CHANGES.txt

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.7

* Fri Apr 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0.
- https://github.com/Cornices/cornice/blob/3.1.0/CHANGES.txt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
