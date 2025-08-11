%global srcname     klusta
%global sum     Spike detection and automatic clustering for spike sorting

Name:       python-%{srcname}
Version:    3.0.16
Release:    30%{?dist}
Summary:    %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        https://github.com/kwikteam/klusta
Source0:    https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
klusta is an open source package for automatic spike sorting of multielectrode
neurophysiological recordings made with probes containing up to a few dozens of
sites.

klusta implements the following features:

- Kwik: An HDF5-based file format that stores the results of a spike sorting
  session.
- Spike detection (also known as SpikeDetekt): an algorithm designed for probes
  containing tens of channels, based on a flood-fill algorithm in the adjacency
graph formed by the recording sites in the probe.
- Automatic clustering (also known as Masked KlustaKwik): an automatic
  clustering algorithm designed for high-dimensional structured datasets.

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist numpy six pytest h5py scipy tqdm responses click}
Requires:       %{py3_dist numpy scipy six h5py tqdm click}

%description -n python3-%{srcname}
klusta is an open source package for automatic spike sorting of multielectrode
neurophysiological recordings made with probes containing up to a few dozens of
sites.

klusta implements the following features:

- Kwik: An HDF5-based file format that stores the results of a spike sorting
  session.
- Spike detection (also known as SpikeDetekt): an algorithm designed for probes
  containing tens of channels, based on a flood-fill algorithm in the adjacency
graph formed by the recording sites in the probe.
- Automatic clustering (also known as Masked KlustaKwik): an automatic
  clustering algorithm designed for high-dimensional structured datasets.


%prep
%autosetup -n %{srcname}-%{version}
rm -fr *egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
%{__python3} setup.py test

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{srcname}

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.16-30
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.0.16-28
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Maxwell G <maxwell@gtmx.me> - 3.0.16-27
- Remove unused python3-mock test dependency

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 3.0.16-23
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0.16-20
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.16-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.16-14
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-7
- Subpackage python2-klusta has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.16-5
- Fix build

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.16-2
- Update based on review comments 1532082
- use py_dist macros

* Sun Jan 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.16-1
- Initial build
