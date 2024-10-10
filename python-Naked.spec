%global pypi_name Naked
%global _description Naked is a new Python command line application framework \
                     that makes creating command line options and sub-commands \
                     simpler.

Name:           python-%{pypi_name}
Version:        0.1.31
Release:        27%{?dist}
Summary:        A command line application framework

License:        MIT
URL:            http://naked-py.com
Source0:        https://files.pythonhosted.org/packages/source/N/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel

BuildArch:      noarch

%description
%{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
Conflicts:      python2-%{pypi_name} < 0.1.31-8

Requires:       python3-Naked
Requires:       python3-PyYAML
Requires:       python3-requests
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
%{_description}


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sed -i -e '1d' lib/Naked/templates/licenses.py
sed -i -e '1d' lib/Naked/templates/readme_md_file.py

%install
function update_scripts() {
    for f in $(find "${1}" -name '*.py*'); do
        if [ x"$(head -n1 "${f}")" == "x#!/usr/bin/env python" ]; then
            sed -i -e '1d' "${f}"
        fi
    done
    find "${1}" \( -name '*.c' -or -name '*.sh' \) -delete
}

%pyproject_install
%pyproject_save_files %{pypi_name}
update_scripts "%{buildroot}/%{python3_sitelib}/%{pypi_name}"


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license docs/LICENSE lib/Naked/templates/licenses.py
%doc docs/README.rst lib/Naked/templates/readme_md_file.py
%{_bindir}/naked

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.31-26
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.31-22
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.31-19
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.31-16
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-8
- Subpackage python2-Naked has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-5
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Gregory Hellings <greg.hellings@gmail.com> - 0.1.31-4
- Corrected spelling of Python 3 dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Gregory Hellings <greg.hellings@gmail.com> - 0.1.31-2
- Fixed description length
- Fixed executable file lint errors

* Mon Sep 25 2017 Gregory Hellings <greg.hellings@gmail.com> - 0.1.31-1
- Initial package.
