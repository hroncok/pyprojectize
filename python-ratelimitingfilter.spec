# Created by pyp2rpm-3.2.2
%global pypi_name ratelimitingfilter

Name:           python-%{pypi_name}
Version:        1.5
Release:        12%{?dist}
Summary:        A rate limiting filter for the Python logging system

License:        MIT
URL:            https://github.com/wkeeling/ratelimitingfilter
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
The RateLimitingFilter is a filter for the Python logging system that allows
you to restrict the rate at which messages can pass through your logging
handlers. The filter can be useful if you're using a handler such as Python's
logging.handlers.SMTPHandler to send error notification emails.
Error notification emails provide a useful means of keeping an eye on.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The RateLimitingFilter is a filter for the Python logging system that allows
you to restrict the rate at which messages can pass through your logging
handlers. The filter can be useful if you're using a handler such as Python's
logging.handlers.SMTPHandler to send error notification emails.
Error notification emails provide a useful means of keeping an eye on.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%pyproject_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5-11
- Rebuilt for Python 3.13

* Thu Feb 22 2024 Michel Lind <salimma@fedoraproject.org> - 1.5-10
- Remove unnecessary and deprecated python3-mock BR

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5-3
- Rebuilt for Python 3.11

* Thu Apr 28 2022 Martin Kutlak <mkfedora@outlook.com> - 1.5-2
- Fix name of spec file

* Thu Apr 28 2022 Martin Kutlak <mkfedora@outlook.com> - 1.5-1
- Update to latest upstream release 1.5

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Martin Kutlak <mkfedora@outlook.com> - 1.1-9
- Drop python2
- Fix BZ#1900528

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-4
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Martin Kutlak <mkutlak@redhat.com> - 1.1-3
- Drop python2 from epel8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Martin Kutlak <mkutlak@redhat.com> - 1.1-1
- Update to upstream version 1.1.
- Remove check section as it is not provided in sources.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Rebuilt for Python 3.7

* Wed Mar 14 2018 Martin Kutlak <mkutlak@redhat.com> - 0.6-1
- Drop python2 subpackage from Fedora 29+

* Wed Mar 14 2018 Martin Kutlak <mkutlak@redhat.com> - 0.6-1
- Initial package.
