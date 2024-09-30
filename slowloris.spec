Name:           slowloris
Version:        0.2.1
Release:        15%{?dist}
Summary:        Low bandwidth DoS tool

License:        MIT
URL:            https://github.com/gkbrk/slowloris
Source0:        %{pypi_source Slowloris}
BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       python3-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Slowloris is basically an HTTP Denial of Service attack that affects threaded
servers.

%package -n     python3-%{name}
Summary:        %{summary}

%description -n python3-%{name}
Slowloris is basically an HTTP Denial of Service attack that affects threaded
servers.

%prep
%autosetup -n Slowloris-%{version}
# Use setuptools
sed -i -e "s/distutils.core/setuptools/g" setup.py
# Remove shebang
sed -i -e '/^#!\//, 1d' %{name}.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

%files
%{_bindir}/%{name}

%files -n python3-%{name} -f %{pyproject_files}
%doc README.md

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.1-14
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.1-11
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.1-8
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.1-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Add README and LICENSE file
- Update to latest upstream release 0.2.1

* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora

