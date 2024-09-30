# Created by pyp2rpm-3.3.8
%global pypi_name icoextract
%global pypi_version 0.1.4

# NOTE: 'icoextract' itself required for tests
%bcond_with tests

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        10%{?dist}
Summary:        Windows PE EXE icon extractor

License:        MIT
URL:            https://github.com/jlu5/icoextract
# Tests not available on PyPI
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  ImageMagick
BuildRequires:  make
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  python3-icoextract
%endif

%description
icoextract is an icon extractor for Windows PE files (.exe/.dll), written in
Python. It also includes a thumbnailer script (exe-thumbnailer) for Linux
desktops.

This project is inspired by extract-icon-py, icoutils, and others.

icoextract aims to be:

  * Lightweight
  * Portable (cross-platform)
  * Fast on large files


%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(pefile)
Requires:       python3dist(pillow)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
icoextract is an icon extractor for Windows PE files (.exe/.dll), written in
Python. It also includes a thumbnailer script (exe-thumbnailer) for Linux
desktops.

This project is inspired by extract-icon-py, icoutils, and others.

icoextract aims to be:

  * Lightweight
  * Portable (cross-platform)
  * Fast on large files


%prep
%autosetup -n %{pypi_name}-%{pypi_version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

# Exec permission
pushd %{buildroot}%{python3_sitelib}/%{pypi_name}
chmod a+x __init__.py
popd

pushd %{buildroot}%{python3_sitelib}/%{pypi_name}/scripts
chmod a+x {extract,icolist,thumbnailer}.py
popd


%if %{with tests}
%check
pushd tests
make
%{python3} test_extract.py
%{python3} test_thumbnailer.py
popd
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_bindir}/%{pypi_name}
%{_bindir}/exe-thumbnailer
%{_bindir}/icolist


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.4-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.4-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.4-3
- Initial package
