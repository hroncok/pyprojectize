%global pypi_name dictdumper

Name:           python-%{pypi_name}
Version:        0.8.4
Release:        12%{?dist}
Summary:        Python dict formatted dumper

License:        MPL-2.0
URL:            https://github.com/JarryShaw/DictDumper
Source0:        %{url}/archive/v%{version}/DictDumper-%{version}.tar.gz
BuildArch:      noarch

%description
The dictdumper project is an open source Python program works as a stream
formatted output dumper for dict.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
The dictdumper project is an open source Python program works as a stream
formatted output dumper for dict.

%prep
%autosetup -n DictDumper-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.4-11
- Rebuilt for Python 3.13

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.4-10
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.4-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.4-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.4-1
- Update to latest upstream release 0.8.4 (closes rhbz#1844692)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.3-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.3-1
- Update to latest upstream release 0.8.3 (rhbz#1842236)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.9

* Fri Mar 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-1
- Update to latest upstream release 0.8.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Update to latest upstream release 0.7.1

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1.post2
- Change version schema (rhbz#1714009)
- Use upstream source
- Add license file and fix license

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0.post2-1
- Initial package for Fedora
