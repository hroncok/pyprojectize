%global pkg_name restructuredtext-lint
%global pypi_name restructuredtext_lint
%global desc Lint reStructuredText linter files with an API or a CLI.\
It reports errors and warning including:\
- Unknown directives\
- Wrong usage of directives\
- Inconsistencies in title levels\
- Unexpected unindent


Name:           python-%{pkg_name}
Version:        1.4.0
Release:        10%{?dist}
Summary:        reStructuredText linter

License:        Unlicense
URL:            https://pypi.python.org/pypi/restructuredtext_lint
Source0:        https://files.pythonhosted.org/packages/48/9c/6d8035cafa2d2d314f34e6cd9313a299de095b26e96f1c7312878f988eec/restructuredtext_lint-1.4.0.tar.gz
Source1:        pytest.ini

BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pkg_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-PyYAML >= 3.11
BuildRequires:  python3-docutils >= 0.11
BuildRequires:  python3-docutils < 1.0
Requires:       python3-docutils >= 0.11
Requires:       python3-docutils < 1.0
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
%{desc}


%prep
%autosetup -n %{pypi_name}-%{version} -p1
cp -a %{SOURCE1} .
# Remove pyc files from source
find -name '*.pyc' -delete


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%check
PYTHONPATH="$(pwd)" pytest-%{python3_version} -v


%files -n python3-%{pkg_name}
%doc README.rst
%license UNLICENSE
%{_bindir}/rst-lint
%{_bindir}/restructuredtext-lint
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{python3_sitelib}/%{pypi_name}/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.0-5
- Rebuilt for Python 3.12

* Thu Feb 02 2023 Julien Enselme <jujens@jujens.eu> - 1.4.0-4
- Update SPEC to build on EPEL9

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Julien Enselme <jujens@jujens.eu> - 1.4.0-1
- Update to 1.4.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Julien Enselme <jujens@jujens.eu> - 1.3.1-1
- Update to 1.3.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Julien Enselme <jujens@jujens.eu> - 1.3.0-1
- Update to 1.3.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Julien Enselme <jujens@jujens.eu> - 1.1.3-4
- Remove Python 2 subpackage (#1629792)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-2
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Julien Enselme <jujens@jujens.eu> - 1.1.3-1
- Update to 1.1.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Nov 14 2017 Julien Enselme <jujens@jujens.eu> - 1.1.2-1
- Update to 1.1.2

* Sat Aug 05 2017 Julien Enselme <jujens@jujens.eu> - 1.1.0-1
- Update to 1.1.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 17 2017 Julien Enselme <jujens@jujens.eu> - 1.0.1-1
- Update to 1.0.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.17.2-4
- Rebuild for Python 3.6

* Sun Oct 30 2016 Julien Enselme <jujens@jujens.eu> - 0.17.2-3
- Correct typos in description
- Use -delete option in find to delete pyc files

* Sun Oct 30 2016 Julien Enselme <jujens@jujens.eu> - 0.17.2-2
- Expand description
- Rename package from python-restructuredtext_lint to python-restructuredtext-lint
- Use only on executable

* Tue Oct 11 2016 Julien Enselme <jujens@jujens.eu> - 0.17.2-1
- Inital package
