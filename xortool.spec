%global pypi_name xortool

Name:           %{pypi_name}
Version:        0.99
Release:        16%{?dist}
Summary:        Tool for XOR cipher analysis

License:        MIT
URL:            https://github.com/hellman/xortool
Source0:        https://github.com/hellman/xortool/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel

%description
A tool to do some XOR analysis to guess the key length (based on count of
equal chars) and to guess the key (base on knowledge of most frequent char).

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' xortool/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-xor

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.99-15
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.99-12
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.99-9
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.99-6
- Rebuilt for Python 3.10

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.99-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.99-2
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.99-1
- Update to latest upstream release 0.99

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.98-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.98-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.98-1
- Initial package for Fedora
