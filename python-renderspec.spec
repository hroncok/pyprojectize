%global pypi_name renderspec
%global common_desc\
renderspec is a tool to convert a .spec.j2 Jinja2 template to a rpm .spec file\
which is usable for different distributions and follow their policies and\
processes.

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        8%{?dist}
Summary:        Jinja2 template renderer for generating .spec files

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://docs.openstack.org/developer/renderspec/
Source0:        %{pypi_source}
BuildArch:      noarch
 
%description
%{common_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pbr}
BuildRequires:  %{py3_dist testrepository}
BuildRequires:  %{py3_dist testresources}
BuildRequires:  %{py3_dist testtools}
BuildRequires:  %{py3_dist ddt}
BuildRequires:  %{py3_dist Sphinx}
BuildRequires:  %{py3_dist openstackdocstheme}
BuildRequires:  %{py3_dist setuptools}
# Required for tests
BuildRequires:  %{py3_dist stestr}
BuildRequires:  %{py3_dist packaging}
BuildRequires:  %{py3_dist pymod2pkg}
BuildRequires:  %{py3_dist PyYAML}

Requires:       %{py3_dist Jinja2} >= 2.8
Requires:       %{py3_dist pymod2pkg} >= 0.7
Requires:       %{py3_dist PyYAML} >= 3.10
Requires:       %{py3_dist packaging} >= 16.5
Requires:       %{py3_dist setuptools}

%description -n python3-%{pypi_name}
%{common_desc}


%package -n python-%{pypi_name}-doc
Summary:        renderspec documentation
%description -n python-%{pypi_name}-doc
Documentation for renderspec

%prep
%autosetup -n %{pypi_name}-%{version}
# Let's handle dependencies ourselves
rm -f *requirements.txt
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# remove shebangs
find -type f -a \( -name '*.py' -o -name 'py.*' \) \
   -exec sed -i '1{/^#!/d}' {} \; \

%build
%py3_build

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install
cp %{buildroot}/%{_bindir}/renderspec %{buildroot}/%{_bindir}/renderspec-%{python3_version}
ln -s %{_bindir}/renderspec-%{python3_version} %{buildroot}/%{_bindir}/renderspec-3

%check
stestr run

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/renderspec
%{_bindir}/renderspec-3
%{_bindir}/renderspec-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.0-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.2.0-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.12

* Tue May 02 2023 Joel Capitao <jcapitao@redhat.com> - 2.2.0-1
- Update to 2.2.0
- Remove py2 bits

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.12.0-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.12.0-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Javier Peña <jpena@redhat.com> - 1.12.0-1
- Update to upstream version 1.12.0 (bz#1736532)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Javier Peña <jpena@redhat.com> - 1.7.0-8
- Removed python2 subpackage from Fedora

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Javier Peña <jpena@redhat.com> - 1.7.0-6
- Fixed Rawhide build (bz#1605872)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Javier Peña <jpena@redhat.com> - 1.7.0-2
- Fixes to issues found during review
- Use py2_dist and py3_dist for requirements

* Wed Sep 20 2017 Javier Peña <jpena@redhat.com> - 1.7.0-1
- Initial package.
