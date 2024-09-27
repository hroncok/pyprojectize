%global pypi_name imagehash

Name:           python-%{pypi_name}
Version:        4.3.2
Release:        2%{?dist}
Summary:        A Python perceptual image hashing module

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/JohannesBuchner/imagehash
Source0:        https://github.com/JohannesBuchner/imagehash/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A image hashing library written in Python. ImageHash supports average hashing,
perception hashing, difference hashing and wavelet hashing.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pywt
BuildRequires:  python3-pillow
BuildRequires:  python3-scipy
BuildRequires:  python3-six
BuildRequires:  python3-wheel, python3-pip, python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A image hashing library written in Python. ImageHash supports average hashing,
perception hashing, difference hashing and wavelet hashing.

%package -n %{pypi_name}-demo
Summary:        %{summary}
Requires:       python3-%{pypi_name}

%description -n %{pypi_name}-demo
Demo tool for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}/usr/images

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*.dist-info
%exclude %{python3_sitelib}/%{pypi_name}/tests/

%files -n %{pypi_name}-demo
%doc README.rst
%license LICENSE
%{_bindir}/find_similar_images.py

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.2-2
- convert license to SPDX

* Sat Aug 10 2024 Dennis Gilmore <dennis@ausil.us> - 4.3.2-1
- update to 4.3.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 4.0-19
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 4.0-15
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Python Maint <python-maint@redhat.com> - 4.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 4.0-2
- Fix changelog entry (rhbz#1723103)
- Update BR
- Enable tests

* Fri Jun 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 4.0-1
- Initial package for Fedora
