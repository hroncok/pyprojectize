%{?python_enable_dependency_generator}
%global pypi_name leather
%global dir_name leather
%global project_owner wireservice
%global github_name leather
%global desc Leather is the Python charting library for those who need charts now and don’t\
care if they’re perfect.\
\
- A readable and user-friendly API.\
- Optimized for exploratory charting.\
- Produces scale-independent SVG charts.\
- Completely type-agnostic. Chart your data, whatever it is.\
- Designed with iPython, Jupyter and atom/hydrogen in mind.\
- Pure Python. No C dependencies to compile.


Name:           python-%{pypi_name}
Version:        0.4.0
Release:        2%{?dist}
Summary:        Python charting for 80% of humans

License:        MIT
URL:            https://pypi.python.org/pypi/leather
Source0:        https://github.com/wireservice/leather/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# Backport of upstream commit to add compatibility with Python 3.10
BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-nose >= 1.1.2
BuildRequires:  python3-sphinx >= 1.2.2
BuildRequires:  python3-furo
BuildRequires:  python3-coverage >= 3.7.1
BuildRequires:  python3-sphinx_rtd_theme >= 0.1.6
BuildRequires:  python3-lxml >= 3.6.0
BuildRequires:  python3-six >= 1.6.1
BuildRequires:  python3-cssselect

%description -n python3-%{pypi_name}
%{desc}


%package -n    python-%{pypi_name}-doc
Summary:       %{summary}

%description -n python-%{pypi_name}-doc
%{desc}

Documentation package.


%prep
%setup -qn %{github_name}-%{version}
# Remove shebang on non executable scripts
sed -i '1{\@^#!/usr/bin/env python@d}' leather/*.py leather/**/*.py

# Remove hidden files in examples
rm examples/charts/.placeholder

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs
    make html
    # Remove hidden file
    rm _build/html/.buildinfo
popd


%install
%pyproject_install
%pyproject_save_files -l %{dir_name}


%check
nosetests-%{python3_version} tests -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst


%files -n python-%{pypi_name}-doc
%doc examples docs/_build/html
%license COPYING


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Julien Enselme <jujens@jujens.eu> - 0.4.0-1
- Update to 0.4.0

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.4-8.git
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.3.4-4.git
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Julien Enselme <jujens@jujens.eu> - 0.3.4-1
- Update to 0.3.4

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.3-22.gite85dd30
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-21.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-20.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.3-19.gite85dd30
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-18.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-17.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-16.gite85dd30
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-15.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.3-14.gite85dd30
- Remove dependency on unittest2 (#1789200)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-13.gite85dd30
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-12.gite85dd30
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-11.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-10.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-9.gite85dd30
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-8.gite85dd30
- Subpackage python2-leather has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-6.gite85dd30
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Julien Enselme <jujens@jujens.eu> - 0.3.3-5.gite85dd30
- Correct build dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Julien Enselme <jujens@jujens.eu> - 0.3.3-2.gite85dd30
- Remove uneeded BuildArch
- Don't use sed inside a loop, pass the expression with globs directly to sed.
- Improve description

* Tue Jan 03 2017 Julien Enselme <jujens@jujens.eu> - 0.3.3-1.gite85dd30
- Inital package
