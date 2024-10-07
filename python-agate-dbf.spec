%global pypi_name agate-dbf
%global file_name agatedbf
%global project_owner wireservice
%global github_name agate-dbf
%global desc Adds read support for DBF files to agate.


Name:           python-%{pypi_name}
Version:        0.2.3
Release:        2%{?dist}
Summary:        Adds read support for DBF files to agate

License:        MIT
URL:            https://pypi.python.org/pypi/agate-dbf
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{version}/%{github_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-nose >= 1.1.2
BuildRequires:  python3dist(agate) >= 1.5
BuildRequires:  python3dist(dbfread) >= 2.0.5
BuildRequires:  python3dist(furo)

%description -n python3-%{pypi_name}
%{desc}


%package -n     python-%{pypi_name}-doc
Summary:        %{summary}
BuildRequires:  python3dist(sphinx) >= 1.2.2
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.1.6
BuildArch:      noarch

%description -n python-%{pypi_name}-doc
%{desc}

Documentation package.


%prep
%setup -qn %{github_name}-%{version}
# Remove shebang on non executable scripts
sed -i '1{\@^#!/usr/bin/env python@d}' agatedbf/*.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Build documentation
pushd docs
    make html SPHINXBUILD=sphinx-build-%{python3_version}
    rm -f _build/html/.buildinfo
popd


%install
%pyproject_install
%pyproject_save_files -l %{file_name}


%check
nosetests-%{python3_version} tests -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst AUTHORS.rst CHANGELOG.rst


%files -n python-%{pypi_name}-doc
%license COPYING
%doc README.rst AUTHORS.rst CHANGELOG.rst docs/_build/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 22 2024 Julien Enselme <jujens@jujens.eu> - 0.2.3-1
- Update to 0.2.3

* Sat Jun 15 2024 Python Maint <python-maint@redhat.com> - 0.2.2-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.2.2-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Julien Enselme <jujens@jujens.eu> - 0.2.2-1
- Update to 0.2.2

* Wed Jun 29 2022 Python Maint <python-maint@redhat.com> - 0.2.1-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.1-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 0.2.1-1
- Update to 0.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-7
- Enable python dependency generator

* Mon Dec 31 2018 Julien Enselme <jujens@jujens.eu> - 0.2.0-6
- Remove Python 2 subpackage (#1662648)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Julien Enselme <jujens@jujens.eu> - 0.2.0-2
- Fetch sources on github with tag instead of commit

* Sun Mar 12 2017 Julien Enselme <jujens@jujens.eu> - 0.2.0-1
- Inital package
