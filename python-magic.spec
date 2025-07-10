%global pypi_name python-magic
%global srcname magic

Name:           %{pypi_name}
Version:        0.4.27
Release:        9%{?dist}
Summary:        File type identification using libmagic

License:        MIT
URL:            https://github.com/ahupp/python-magic
Source0:        %{pypi_source %{pypi_name}}
#Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual
and MIME-type output.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

Requires:       file-devel

%description -n python3-%{srcname}
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual
and MIME-type output.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l magic

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.27-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.27-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.27-1
- Update to latest upstream release 0.4.27 (closes rhbz#2089045)

* Sat Jul 09 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.26-1
- Update to latest upstream release 0.4.26

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.25-2
- Rebuilt for Python 3.11

* Wed Feb 23 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.25-1
- Update to latest upstream release 0.4.25 (closes rhbz#2049348)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.24-1
- Update to latest upstream release 0.4.24 (closes rhbz#1929455)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.22-2
- Rebuilt for Python 3.10

* Wed Feb 17 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.22-1
- Update to latest upstream release 0.4.22 (#1929455)

* Wed Feb 10 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.20-1
- Update to latest upstream release 0.4.20 (#1901860)

* Mon Feb 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.19-1
- Update to latest upstream release 0.4.19 (#1901860)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Christian Birk <mail@birkc.de> - 0.4.18-1
- New upstream release 0.4.18

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.15-3
- Rebuilt for Python 3.9

* Thu Jan 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.15-2
- Rename package (rhbz#1790100)

* Sat Jan 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.15-1
- Initial package for Fedora
