%global pypi_name pysmt

Name:           python-%{pypi_name}
Version:        0.9.5
Release:        8%{?dist}
Summary:        Solver-agnostic library for SMT Formulae manipulation and solving

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://www.pysmt.org
Source0:        https://github.com/pysmt/pysmt/archive/v%{version}/PySMT-%{version}.tar.gz
BuildArch:      noarch

%description
A library for SMT formulae manipulation and solving pySMT makes working
with Satisfiability Modulo Theory simple. Among others, you can:

* Define formulae in a solver independent way in a simple and inutitive way
* Write ad-hoc simplifiers and operators
* Dump your problems in the SMT-Lib format
* Solve them using one of the native solvers
* Wrapping any SMT-Lib complaint

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
#BuildRequires:  python3-nose
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
A library for SMT formulae manipulation and solving pySMT makes working
with Satisfiability Modulo Theory simple. Among others, you can:

* Define formulae in a solver independent way in a simple and intuitive way
* Write ad-hoc simplifiers and operators
* Dump your problems in the SMT-Lib format
* Solve them using one of the native solvers
* Wrapping any SMT-Lib complaint

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' pysmt/{cmd/shell.py,constants.py}

%build
%py3_build

%install
%py3_install

# https://github.com/pysmt/pysmt/issues/608
#%%check
#export NOSE_PROCESSES=4
#export NOSE_PROCESS_TIMEOUT=240
#export PYTHONDONTWRITEBYTECODE=True
#nosetests-%%{python3_version} -v -x

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst docs/*.rst docs/tutorials/
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/PySMT-%{version}-py*.egg-info/
%exclude %{python3_sitelib}/%{pypi_name}/test/
%{_bindir}/pysmt-install

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.5-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.5-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.5-2
- Rebuilt for Python 3.12

* Sat Feb 11 2023 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.5-1
- Update to latest upstream release 0.9.5 (closes rhbz#2157764)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to latest upstream release 0.9.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-2
- Fix typo in description (rhbz#1808467)

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Initial package for Fedora
