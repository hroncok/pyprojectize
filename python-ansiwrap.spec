%global pypi_name ansiwrap

Name:           python-%{pypi_name}
Version:        0.8.4
Release:        18%{?dist}
Summary:        Text wrapper with ANSI colors and styles support

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/jonathaneunice/ansiwrap
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

# Fix Python 3.12 compatibility
# https://github.com/jonathaneunice/ansiwrap/pull/20
#
# Builds on and includes:
#
# Fix tests on Python 3.11
# https://github.com/jonathaneunice/ansiwrap/pull/19
Patch:          %{url}/pull/20.patch

%description
ansiwrap wraps text, like the standard textwrap module. But it also correctly
wraps text that contains ANSI control sequences that colorize or style text.
Where textwrap is fooled by the raw string length of those control codes,
ansiwrap is not; it understands that however much those codes affect color
and display style, they have no logical length.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-ansicolors
BuildRequires:  python3-coverage
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-textwrap3
BuildRequires:  python3-tox

%description -n python3-%{pypi_name}
ansiwrap wraps text, like the standard textwrap module. But it also correctly
wraps text that contains ANSI control sequences that colorize or style text.
Where textwrap is fooled by the raw string length of those control codes,
ansiwrap is not; it understands that however much those codes affect color
and display style, they have no logical length.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.4-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.4-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.4-13
- Patch for Python 3.12

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.8.4-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.4-8
- Fix tests on Python 3.11 (fix RHBZ#2050083)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.4-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.4-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.4-1
- Initial package for Fedora
