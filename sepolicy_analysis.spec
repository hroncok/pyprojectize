Name:           sepolicy_analysis
Version:        0.1
Release:        27%{?dist}
Summary:        SELinux policy analysis tool

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/vmojzis/sepolicy_analysis
#./setup.py egg_info --egg-base /tmp sdist
Source0:        https://github.com/vmojzis/sepolicy_analysis/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Update-to-work-with-setools-4.3.patch

BuildArch:      noarch

BuildRequires:  python3-devel

Requires: python3-setools >= 4.0
Requires: python3-networkx >= 1.11
Requires: python3-matplotlib

%description
Tool designed to help increase the quality of SELinux policy by identifying
possibly dangerous permission pathways, simplifying regression testing and
providing policy visualization.

%prep
%autosetup -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
#mkdir -p % {buildroot}% {_mandir}/man1
%pyproject_install
%pyproject_save_files '*'

%check
%if %{?_with_check:1}%{!?_with_check:0}
%{__python3} setup.py test
%endif

%files -f %{pyproject_files}
%license COPYING
%{_bindir}/seextract_cil
%{_bindir}/sebuild_graph
%{_bindir}/seexport_graph
%{_bindir}/segraph_query
%{_bindir}/sevisual_query
%dir %{_sysconfdir}/sepolicyanalysis
%config(noreplace) %{_sysconfdir}/sepolicyanalysis/domain_groups_cil.conf
%config(noreplace) %{_sysconfdir}/sepolicyanalysis/security_related.conf
%doc %{_mandir}/man1/se*

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-27
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1-25
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1-22
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1-19
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1-16
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Vit Mojzis <vmojzis@redhat.com> - 0.1-13
- Update to work with setools-4.3
- Add missing dependency on python3-matplotlib

* Thu Jun 04 2020 Vit Mojzis <vmojzis@redhat.com> - 0.1-12
- Add dependency on python3-networkx
- Fix setools dependency (setools-python3 got renamed to python3-setools)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Vit Mojzis <vmojzis@redhat.com> - 0.1-1
- Initial release

