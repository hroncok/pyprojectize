Summary: Git commit message linting tool
Name: gitlint
Version: 0.15.0
Release: 14%{?dist}
License: MIT
Source: %pypi_source
Patch0: strict-dependencies.patch
URL: https://jorisroovers.github.io/gitlint
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: %{py3_dist Click} >= 7.1.2
BuildRequires: %{py3_dist arrow} >= 0.15.6
BuildRequires: %{py3_dist sh} >= 1.13.1
BuildRequires: %{py3_dist coverage}
BuildRequires: git-core
Requires: git-core

%description
gitlint checks git commit messages for style, using validations based on
well-known community standards or on checks which have proved useful:
maximum title length, trailing white-space checks, punctuation, tabs,
minimum body length, valid email addresses...

%prep
%autosetup -p1

%build
%py3_build

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m coverage run --omit='/usr/*,$(pwd)/gitlint/tests/*,$(pwd)/gitlint/qa/*' -m unittest discover -v -s $(pwd)/gitlint/tests

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/qa

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/
%{_bindir}/gitlint

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.15.0-13
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 0.15.0-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.15.0-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.15.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Stephen Kitt <skitt@fedoraproject.org> - 0.15.0-1
- new upstream release

* Mon Sep 14 2020 Stephen Kitt <skitt@fedoraproject.org> - 0.13.1-1
- initial package
