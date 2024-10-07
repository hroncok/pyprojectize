%define modname pywt
%define pkgname PyWavelets

Name:           python-%{modname}
Version:        1.3.0
Release:        9%{?dist}
Summary:        PyWavelets, wavelet transform module
License:        MIT
URL:            https://pywavelets.readthedocs.io/en/latest
Source0:        https://github.com/PyWavelets/pywt/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Slight precision diff on aarch64 - https://github.com/PyWavelets/pywt/pull/641
Patch0:         python-pywt-almost.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  xorg-x11-server-Xvfb

%description
PyWavelets is a Python wavelet transforms module that can do:

* 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
* 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
* 1D and 2D Wavelet Packet decomposition and reconstruction
* Computing Approximations of wavelet and scaling functions
* Over seventy built-in wavelet filters and support for custom wavelets
* Single and double precision calculations
* Results compatibility with Matlab Wavelet Toolbox

%package doc
Summary:        Documentation for %{name}
BuildRequires:  python3-sphinx
BuildRequires:  python3-numpydoc
BuildRequires:  python3-matplotlib

%description doc
Documentation for %{name}.

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3dist(numpy) >= 1.9.1
BuildRequires:  python3-pytest

%description -n python3-%{modname}
PyWavelets is a Python wavelet transforms module that can do:

* 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
* 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
* 1D and 2D Wavelet Packet decomposition and reconstruction
* Computing Approximations of wavelet and scaling functions
* Over seventy built-in wavelet filters and support for custom wavelets
* Single and double precision calculations
* Results compatibility with Matlab Wavelet Toolbox

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

sed -i '1{\@^#!/usr/bin/env python@d}' %{modname}/tests/*.py 

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel -C--global-option=--force

pushd doc
  export PYTHONPATH=`readlink -f ../build/lib.*-*`
  make html SPHINXBUILD=sphinx-build-3
  find -name '.buildinfo' -delete
popd

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
mkdir -p matplotlib
touch matplotlib/matplotlibrc
export XDG_CONFIG_HOME=`pwd`
pushd %{buildroot}/%{python3_sitearch}
  xvfb-run -a pytest-%{python3_version} pywt/tests --verbose -p no:cacheprovider \
%ifarch ppc64le
  -k 'not test_cwt_complex and not test_cwt_method_fft and not test_accuracy_precomputed_cwt'
  # see https://github.com/PyWavelets/pywt/issues/508
%endif

popd

%files doc
%doc doc/build/html

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.3.0-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Orion Poplawski <orion@nwra.com> - 1.3.0-1
- Update to 1.3.0
- Add patch to fix test_cwt_batch on aarch64
- Also exclude test_accuracy_precomputed_cwt on ppc64le

* Wed Jun 22 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-8
- Fix FTBFS with setuptools >= 62.1
Resolves: rhbz#2097087

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.1.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Orion Poplawski <orion@nwra.com> - 1.1.1-1
- Update to 1.1.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep  5 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-1
- Update to latest version (#1683032)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Remove python2 subpackage

* Tue Sep 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-8
- Rebuilt for Python 3.7
- Invoke xvfb-run with -a to avoid random failures with the latter one

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.2-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Sergio Pascual  <sergiopr@fedoraproject.org> - 0.5.2-3
- Tolerance error in tests fixed upstream github.com/PyWavelets/pywt/issues/316

* Wed May 31 2017 Sergio Pascual  <sergiopr@fedoraproject.org> - 0.5.2-2
- Skip tolerance error en tests (for ppc64le aarch64 ppc64 s390x)

* Wed May 31 2017 Sergio Pascual  <sergiopr@fedoraproject.org> - 0.5.2-1
- New upstream source (0.5.2)
- Run tests with matplotlib under xvfb-run

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-2
- One doc subpkg
- Drop shebangs from tests

* Fri Nov 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Initial package
