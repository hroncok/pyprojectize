%global pypi_name wavio

%global pypi_description wavio is simple a Python module that allows to \
read and write WAV files as numpy arrays.

Name: python-%{pypi_name}
Summary: Read and write WAV files as numpy arrays
License: BSD-2-Clause

Version: 0.0.7
Release: 7%{?dist}

URL: https://github.com/WarrenWeckesser/wavio
Source0: %{URL}/archive/v%{version}/%{pypi_name}-v%{version}.tar.gz

BuildRequires: python3-devel

# For running the tests
BuildRequires: python3-numpy
BuildRequires: python3-pytest

BuildArch: noarch

%description
%{pypi_description}


%package -n python3-%{pypi_name}
Summary: %{summary}
BuildArch: noarch

%description -n python3-%{pypi_name}
%{pypi_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Extract license text from comment at top of source
awk 'BEGIN { start_print=0 }
/^-----$/ { start_print=1; next }
/^"""$/ { if ( start_print==1 ) exit }
/.*/ { if (start_print == 1) print $0 }' < wavio.py > LICENSE


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%check
%pytest


%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}.dist-info/
%{python3_sitelib}/__pycache__/%{pypi_name}.*


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.0.7-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.7-2
- Rebuilt for Python 3.12

* Mon Apr 24 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.0.7-1
- Update to v0.0.7
- Switch to downloading sources from GitHub (pypi tarballs ship without tests)
- Run test suite during %%check
- Migrate License tag to SPDX

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.4-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.4-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.0.4-2
- Fix installation directory (noarch package - goes in python sitelib, not sitearch)

* Sat Jul 11 2020 Artur Iwicki <fedora@svgames.pl> - 0.0.4-1
- Initial packaging
