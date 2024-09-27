%{?python_enable_dependency_generator}
%global modname moss

# Don't fail here because upstream says
# Note that some of the statistical tests depend on randomly generated data
# and fail from time to time because of this.
# ignatenkobrain: I got it failing from time to time in COPR
# Disable tests forever due to: https://github.com/mwaskom/moss/issues/17
%bcond_with check

Name:           python-%{modname}
Version:        0.5.0
Release:        25%{?dist}
Summary:        Assorted utilities for neuroimaging and cognitive science

# moss/external/mvpasurf.py is MIT
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/mwaskom/moss
Source0:        https://github.com/mwaskom/moss/archive/v%{version}/%{modname}-%{version}.tar.gz
Patch0001:      0001-put-real-dependencies-into-metadata.patch
Patch0002:      0002-remove-use-of-deprecated-removed-scipy.stats.ss.patch
Patch0003:      0003-bunch-munch.patch

BuildArch:      noarch

%description
Moss is a library of functions, classes, and scripts to that may be useful for
analyzing scientific data. Because this package is developed for neuroimaging
and cognitive science, there is probably some bias towards applications that
are useful in that domain. However, the functions are intended to be written
in as general and lightweight a fashion as possible.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
Provides:       bundled(PyMVPA)
BuildRequires:  python3-devel
%if %{with check}
# install_requires
BuildRequires:  python3dist
BuildRequires:  matplotlib
BuildRequires:  python3dist
BuildRequires:  munch
BuildRequires:  python3dist
BuildRequires:  numpy
BuildRequires:  python3dist
BuildRequires:  nibabel
BuildRequires:  python3dist
BuildRequires:  pandas
BuildRequires:  python3dist
BuildRequires:  scikit-learn
BuildRequires:  python3dist
BuildRequires:  scipy
BuildRequires:  python3dist
BuildRequires:  seaborn
BuildRequires:  python3dist
BuildRequires:  six
# tests_require
BuildRequires:  python3dist
BuildRequires:  nose
BuildRequires:  python3dist
BuildRequires:  pytest
%endif

%description -n python3-%{modname}
Moss is a library of functions, classes, and scripts to that may be useful for
analyzing scientific data. Because this package is developed for neuroimaging
and cognitive science, there is probably some bias towards applications that
are useful in that domain. However, the functions are intended to be written
in as general and lightweight a fashion as possible.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1
rm -vf licenses/BUNCH_LICENSE moss/external/bunch.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Depends on 'freeview' utility
rm -vf %{buildroot}%{_bindir}/recon_qc

%if %{with check}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v
%endif

%files -n python3-%{modname}
%license LICENSE licenses/*
%doc README.md
%{_bindir}/check_mni_reg
%{_bindir}/recon_status
%{_bindir}/recon_movie
%{_bindir}/recon_process_stats
%{_bindir}/ts_movie
%{_bindir}/warp_qc
%{python3_sitelib}/%{modname}*

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.0-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.0-23
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.0-19
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.0-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-4
- Subpackage python2-moss has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.4-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-8
- Rebuild for Python 3.6

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.3.4-7
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 16 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.4-5
- Python3 binaries should require only python3 (RHBZ #1342502)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.4-3
- Fix according review

* Wed Nov 25 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.4-2
- Provide only one version of binaries (py3)

* Thu Nov 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.4-1
- Initial package
