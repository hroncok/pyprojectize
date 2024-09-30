%global pypi_name gphoto2

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        22%{?dist}
Summary:        A Python interface to libgphoto2

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/jim-easterbrook/python-gphoto2
Source0:        %{pypi_source}
Patch0:         python-gphoto2-c99.patch

BuildRequires:  gcc
BuildRequires:  libgphoto2-devel
BuildRequires:  pkgconfig

%description
python-gphoto2 is a comprehensive Python interface (or binding) to libgphoto2.
It is built using SWIG to automatically generate the interface code. This 
ives direct access to nearly all the libgphoto2 functions, but sometimes in
a rather un-Pythonic manner.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
python-gphoto2 is a comprehensive Python interface (or binding) to libgphoto2.
It is built using SWIG to automatically generate the interface code. This
gives direct access to nearly all the libgphoto2 functions, but sometimes in
a rather un-Pythonic manner.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove shebang
sed -e '1d' -i examples/*.py
# Examples don't need to be executable
chmod -x examples/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
# Data files are goining to the wrong location
rm -rf %{buildroot}%{_datadir}/%{name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.txt README.rst examples

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-20
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.0-16
- Rebuilt for Python 3.12

* Thu Jan 26 2023 Florian Weimer <fweimer@redhat.com> - 2.0.0-15
- Avoid implicit function declarations in SWIG-generated code

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Initial package for Fedora
