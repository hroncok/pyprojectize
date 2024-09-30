%global pypi_name yaql


# Disable docs building as it doesn't support recent sphinx
%global with_docs 0

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        15%{?dist}
Summary:        Yet Another Query Language

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0001:      0001-Replace-assertItemsEqual-with-assertCountEqual.patch

BuildArch:      noarch

%description
YAQL library has a out of the box large set of commonly used functions.

%package -n     python3-%{pypi_name}
Summary:        YAQL library has a out of the box large set of commonly used functions.

BuildRequires:  python3-devel
BuildRequires:  python3-tools
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx
BuildRequires:  python3-testtools
BuildRequires:  python3-ply
BuildRequires:  python3-dateutil

Requires:       python3-six
Requires:       python3-pbr
Requires:       python3-babel
Requires:       python3-ply
Requires:       python3-dateutil

%description -n python3-%{pypi_name}
YAQL library has a out of the box large set of commonly used functions.

%if 0%{?with_docs}
# Documentation package
%package -n python-%{pypi_name}-doc
Summary:        Documentation for YAQL library

%description -n python-%{pypi_name}-doc
Documentation for YAQL library
%endif


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if 0%{?with_docs}
# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
mv %{buildroot}/%{_bindir}/%{pypi_name} %{buildroot}/%{_bindir}/python3-%{pypi_name}

pushd %{buildroot}%{_bindir}
for i in %{pypi_name}-{3,%{?python3_version}}; do
    ln -sf  python3-%{pypi_name} $i
    ln -sf  python3-%{pypi_name} %{pypi_name}
done
popd

%check
%{python3} -W ignore::ResourceWarning setup.py test
# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/yaql/tests


%files -n python3-%{pypi_name}
%license LICENSE
%doc doc/source/readme.rst README.rst
%{_bindir}/python3-%{pypi_name}
%{_bindir}/%{pypi_name}-3*
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%if 0%{?with_docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Joel Capitao <jcapitao@redhat.com> - 2.0.0-10
- Remove oslo-sphinx BR

* Mon Oct 23 2023 Alfredo Moralejo <amoralej@redhat.com> - 2.0.0-9
- Remove 2to3 usage while building the package

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.0.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Joel Capitao <jcapitao@redhat.com> - 2.0.0-2
- Replace remaining asserItemsEqual with asserCountEqual

* Mon Jul 26 2021 Joel Capitao <jcapitao@redhat.com> - 2.0.0-1
- Update to latest release (#1981310)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Joel Capitao <jcapitao@redhat.com> - 1.1.3-18
- Switch to collections.abc
- Replace asserItemsEqual with asserCountEqual
- Enable tests

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.3-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Alfredo Moralejo <amoralej@redhat.com> - 1.1.3-15
- Remove references to python2 subpackage.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-9
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.1.3-8
- Remove python2 subpackage from fedora and rhel < 8
- Remove docs subpackage as it doesn't support recent versions of sphinx

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.3-5
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Yatin Karel <ykarel@redhat.com> - 1.1.3-2
- Fix python-ply Requires for rhel

* Fri Feb 09 2018 Alfredo Moralejo <amoralej@redhat.com> - 1.1.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuild for Python 3.6

* Mon Aug 22 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.0-3
- Fix Requires in python2-yaql

* Fri Apr  8 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.0-2
- Fix RHBZ#1282081

* Fri Apr  8 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.0-1
- Upstream 1.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Marcos Fermin Lobo <marcos.fermin.lobo@cern.ch> 1.0.2-1.el7
- Update to 1.0.2

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 26 2015 Marcos Fermin Lobo <marcos.fermin.lobo@cern.ch> 0.2.7-1
- First RPM for FC23
