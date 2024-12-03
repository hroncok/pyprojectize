%global pypi_name pyhcl

Name:           python-%{pypi_name}
Version:        0.4.5
Release:        5%{?dist}
Summary:        HCL configuration parser for Python

License:        MPL-2.0
URL:            https://github.com/virtuald/pyhcl
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Implements a parser for HCL (HashiCorp Configuration Language) in Python.

This implementation aims to be compatible with the original Go version
of the parser.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
# Test requires:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ply)

%description -n python3-%{pypi_name}
Implements a parser for HCL (HashiCorp Configuration Language) in Python.

This implementation aims to be compatible with the original Go version
of the parser.

%prep
%autosetup -n %{pypi_name}-%{version}
# Unbundle ply
rm -vr src/hcl/ply
echo 'ply' >> requirements.txt
sed -i -e "s/,'hcl.ply'//" setup.py
grep -rl '\.ply' | xargs -t sed -i -e 's/\.ply/ply/'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l hcl

%check
%pyproject_check_import

PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 -m pytest tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/hcltool

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.5-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 08 2023 Andrew Heath <aheath1992@gmail.com> - 0.4.5-1
- Update to 0.4.5

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.4-2
- Rebuilt for Python 3.12

* Sat Mar 11 2023 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.13-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.13-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.13-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 18:52:27 EDT 2019 Neal Gompa <ngompa13@gmail.com> - 0.3.13-2
- Fix parameter for subpackage name in description section

* Thu Oct 24 18:22:07 EDT 2019 Neal Gompa <ngompa@datto.com> - 0.3.13-1
- Initial packaging for Fedora (RH#1765347)
