%global pkgname click-completion

Name:           python-click-completion
Version:        0.5.2
Release:        16%{?dist}
Summary:        Add automatic completion support for fish, Zsh, Bash and PowerShell to Click
License:        MIT
URL:            https://github.com/click-contrib/click-completion
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%{?python_enable_dependency_generator}

%description
Enhanced completion for Click

Add automatic completion support for fish, Zsh, Bash and PowerShell to Click.

All the supported shells are able to complete all the command line arguments
and options defined with click. In addition, fish and Zsh are also displaying
the options and commands help during the completion.


%package     -n python3-%{pkgname}
Summary:        %{summary}
%description -n python3-%{pkgname}
Enhanced completion for Click

Add automatic completion support for fish, Zsh, Bash and PowerShell to Click.

All the supported shells are able to complete all the command line arguments
and options defined with click. In addition, fish and Zsh are also displaying
the options and commands help during the completion.


%prep
%autosetup -n %{pkgname}-%{version}
sed -i 's|^#!/usr/bin/env python||' click_completion/__init__.py
sed -i 's|^#!/usr/bin/env python||' examples/click-completion-*
chmod -x examples/click-completion-*


%generate_buildrequires
%pyproject_buildrequires


%build
%{pyproject_wheel}


%install
%{pyproject_install}


%files -n python3-%{pkgname}
%license LICENSE
%doc examples README.md
%{python3_sitelib}/click_completion*/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.2-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.2-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.2-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.9

* Mon Feb 24 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.5.2
- Update to 0.5.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-1
- Update to 0.5.0
- Drop python2 subpackage

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.7

* Tue Apr  3 2018 Brett Lentz <brett.lentz@gmail.com> - 0.2.1-1
- initial package
