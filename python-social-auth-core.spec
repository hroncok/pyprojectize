%global pypi_name social-auth-core
%global egginfo_name social_auth_core
# The Python module name is different from the package name published to PyPI.
%global module_name social_core

%global desc %{expand:
Python Social Auth aims to be an easy-to-setup social authentication and
authorization mechanism for Python projects supporting protocols like OAuth (1
and 2), OpenID and others.

The initial codebase is derived from django-social-auth with the idea of
generalizing the process to suit the different frameworks around, providing
the needed tools to bring support to new frameworks.

django-social-auth itself was a product of modified code from
django-twitter-oauth and django-openid-auth projects.

The project is now split into smaller modules to isolate and reduce
responsibilities and improve reusability.

Documentation: https://python-social-auth.readthedocs.io/en/latest/
Release notes: https://github.com/python-social-auth/%{module_name}/releases/tag/4.2.0
}

%global summary Python Social Auth is an easy to setup social authentication\/registration mechanism with support for several frameworks and auth providers.

Name:           python-%{pypi_name}
Version:        4.5.4
Release:        2%{?dist}
Summary:        %{summary}
License:        BSD-3-Clause
URL:            https://github.com/python-social-auth/social-core/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

# Requirements for running social-core
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(oauthlib)
BuildRequires:  python3dist(requests-oauthlib)
BuildRequires:  python3dist(pyjwt) >= 2.7.0
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(defusedxml)
BuildRequires:  python3dist(python3-openid) >= 3.0.10
BuildRequires:  python3dist(python3-saml)

# Requirements for running tests
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(httpretty)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
%py_provides python3-%{pypi_name}

Requires:       python3dist(cryptography) >= 2.1.1
Requires:       python3dist(defusedxml)
Requires:       python3dist(oauthlib)
Requires:       python3dist(pyjwt) >= 2.7.0
Requires:       python3dist(python3-openid) >= 3.0.10
Requires:       python3dist(requests)
Requires:       python3dist(requests-oauthlib)

%description -n python3-%{pypi_name}
%{desc}
If you want social-core to work with azuread (the Azure Active Directory), this
is the package you need.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

rm -rf %{egginfo_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module_name}

rm -r %{buildroot}%{python3_sitelib}/%{module_name}/tests/

%check
%{pytest} %{module_name}/tests/

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
* Mon Aug 19 2024 Chenxiong Qi <qcxhome@gmail.com> - 4.5.4-2
- Update package description

* Sat Aug 17 2024 Chenxiong Qi <qcxhome@gmail.com> - 4.5.4-1
- Build upstream release 4.5.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Chenxiong Qi <qcxhome@gmail.com> - 4.3.0-5
- Switch to SPDX license identifier

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Python Maint <python-maint@redhat.com> - 4.3.0-2
- Rebuilt for Python 3.11

* Sat Jun 18 2022 Chenxiong Qi <qcxhome@gmail.com> - 4.3.0-1
- Build upstream release 4.3.0

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 4.2.0-3
- Rebuilt for Python 3.11

* Sun Feb 27 2022 Chenxiong Qi <qcxhome@gmail.com> - 4.2.0-2
- Exclude saml subpackage temporarily

* Sat Jan 22 2022 Chenxiong Qi <qcxhome@gmail.com> - 4.2.0-1
- Bump release to 4.2.0-1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Chenxiong Qi <qcxhome@gmail.com> - 4.1.0-3
- Backport patches in order to run tests

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.10

* Thu May 06 2021 Chenxiong Qi <qcxhome@gmail.com> - 4.1.0-1
- Rebuilt for upstream version 4.1.0

* Sat Mar 06 2021 Chenxiong Qi <qcxhome@gmail.com> - 4.0.2-2
- Bump release 4.0.2-2

* Sat Mar 06 2021 Chenxiong Qi <qcxhome@gmail.com> - 4.0.2-1
- Rebuilt for upstream version 4.0.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Chenxiong Qi <qcxhome@gmail.com> - 3.3.3-3
- Fix subpackage requires

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Chenxiong Qi <qcxhome@gmail.com> - 3.3.3-1
- Rebuilt version 3.3.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.0-9
- Remove dependency on unittest2 (#1789200)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-5
- Change the defusedxml requirement to not have rc1, which confused the python auto dep script.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.7.0-1
- Initial package.
