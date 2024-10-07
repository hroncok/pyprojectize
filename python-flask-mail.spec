%global pkg_name flask-mail
%global mod_name Flask-Mail

Name:       python-%{pkg_name}
Version:    0.9.1
Release:    26%{?dist}
Summary:    Flask extension for sending email
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://github.com/mattupstate/%{pkg_name}/
Source0:    %{pypi_source %{mod_name}}
BuildArch:  noarch

%description
A Flask extension for sending email messages.


%package -n python3-%{pkg_name}
Summary:    Flask extension for sending email
BuildRequires:   python3-devel
BuildRequires:   python3-flask

%description -n python3-%{pkg_name}
A Flask extension for sending email messages.


%prep
%autosetup -n %{mod_name}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l flask_mail


%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.1-26
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.9.1-24
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.9.1-20
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.9.1-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.9.1-15
- Small cleanups to the spec

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-6
- Enable python dependency generator

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-5
- Subpackage python2-flask-mail has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.7

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.9.1-2
- improve spec file

* Tue Jan  3 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 0.9.1-1
- Initial package
