%global rpmname debianbts
%global pypi_name python-debianbts

Name:           %{pypi_name}
Version:        2.8.2
Release:        17%{?dist}
Summary:        Python interface to Debian's Bug Tracking System

License:        MIT
URL:            https://github.com/venthur/python-debianbts
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/venthur/python-debianbts/master/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%description
Python-debianbts is a Python library that allows for querying
Debian's Bug Tracking System.

%package -n     python3-%{rpmname}
Summary:        %{summary}

Requires:       python3dist(mock)
Requires:       python3dist(pysimplesoap)
Requires:       python3dist(setuptools)

%description -n python3-%{rpmname}
python-debianbts is a Python library that allows for querying
Debian's Bug Tracking System.

%prep
%autosetup -n %{pypi_name}-%{version}
for lib in debianbts/*.py; do
 sed -e '1{\@^#! /usr/bin/env python@d}' -e '1{\@^#!/usr/bin/env python@d}' \
     -e '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
cp -p %{SOURCE1} .

# Remove bundled egg-info
#rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l debianbts

%check
%pyproject_check_import

%files -n python3-%{rpmname} -f %{pyproject_files}
%doc README.md
%{_bindir}/debianbts

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.8.2-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 2.8.2-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.8.2-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.8.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 2.8.2-1
- Initial package.
