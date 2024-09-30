%global pypi_name mulpyplexer

Name:           python-%{pypi_name}
Version:        0.09
Release:        16%{?dist}
Summary:        Module that multiplexes interactions with lists of Python objects

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/zardus/mulpyplexer
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel

%description
Mulpyplexer is a piece of code that can multiplex interactions with lists of
python objects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Mulpyplexer is a piece of code that can multiplex interactions with lists of
python objects.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.09-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.09-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.09-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.09-7
- Rebuilt for Python 3.11

* Mon Mar 07 2022 Karolina Surma <ksurma@redhat.com> - 0.09-4
- Fix package build with setuptools >= 60.x

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.09-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.09-1
- UPdate to latest upstream release 0.09

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.08-2
- Rebuilt for Python 3.9

* Sat Mar 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.08-2
- Add license file (#1808506) 

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.08-1
- Initial package for Fedora
