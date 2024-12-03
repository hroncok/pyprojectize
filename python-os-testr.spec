%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x01527a34f0d0080f8a5db8d6eb6c5df21b4b6363

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-testr

%global with_doc 1

%global common_desc \
ostestr is a testr wrapper that uses subunit-trace for output and builds \
some helpful extra functionality around testr.

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        9%{?dist}
Summary:        A testr wrapper to provide functionality for OpenStack projects

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://git.openstack.org/cgit/openstack/%{pypi_name}
Source0:        https://tarballs.openstack.org/os-testr/os-testr-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/os-testr/os-testr-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  git-core

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary: %summary
Obsoletes: python2-%{pypi_name} < %{version}-%{release}

Requires:       python3-pbr
Requires:       python3-stestr
Requires:       python3-subunit
Requires:       python3-testtools

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary: Documentation for ostestr module
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  python3-openstackdocstheme

%description -n python-%{pypi_name}-doc
Documentation for ostestr module
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Let RPM handle the dependencies
rm -rf *requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -W -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyproject_install}
%pyproject_save_files -l os_testr
for file in %{buildroot}%{python3_sitelib}/os_testr/{subunit_trace,subunit2html}.py; do
    chmod a+x $file
done

# Fix ambiguous shebangs for RHEL > 7 and Fedora > 29
%py3_shebang_fix %{buildroot}%{python3_sitelib}/os_testr/

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/generate-subunit
%{_bindir}/subunit-trace
%{_bindir}/subunit2html

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.0-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 3.0.0-1
- Update to upstream version 3.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.11

* Thu May 19 2022 Joel Capitao <jcapitao@redhat.com> 2.0.1-1
- Update to upstream version 2.0.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 2.0.0-1
- Update to upstream version 2.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.1.0-2
- Update to upstream version 1.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 10 2018 RDO <dev@lists.rdoproject.org> 1.0.0-1
- Update to 1.0.0

