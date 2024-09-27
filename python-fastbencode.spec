%global pypi_name fastbencode

Name:           python-%{pypi_name}
Version:        0.2
Release:        5%{?dist}
Summary:        Implementation of bencode with optional fast C extensions

License:        GPL-2.0-or-later AND MIT
#fastbencode is licensed under GPLv2+
#_bencode_py.py is licensed under MIT
URL:            https://github.com/breezy-team/fastbencode
Source:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.29
BuildRequires:  python3dist(setuptools)
BuildRequires:  gcc

%global _description %{expand:
fastbencode is an implementation of the bencode serialization format 
originally used by BitTorrent.
The package includes both a pure-Python version and an optional C extension 
based on Cython.
Both provide the same functionality, but the C extension provides 
significantly better performance.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-%{pypi_name}
%license COPYING
%doc README.md
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Ondřej Pohořelský <opohorel@redhat.com> - 0.2-1
- Update to 0.2
- Convert license to SPDX format

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.9-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.9-2
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Ondřej Pohořelský <opohorel@redhat.com> - 0.0.9-1
- Initial package.
