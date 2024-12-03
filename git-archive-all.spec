%global modname %(n=%{name}; echo ${n//-/_})

Name:           git-archive-all
Version:        1.23.1
Release:        8%{?dist}
Summary:        Archive git repository with its submodules

License:        MIT
URL:            https://github.com/Kentzo/git-archive-all
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
# git-submodule is in git, not in git-core
Requires:       git

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup
#sed -i -e '1{\@^#! /usr/bin/env python@d}' %{modname}.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/%{name}

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.23.1-7
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.23.1-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 09 2022 Richard Shaw <hobbes1069@gmail.com> - 1.23.1-1
- Update to 1.23.1.

* Mon Sep 05 2022 Richard Shaw <hobbes1069@gmail.com> - 1.23.0-1
- Update to 1.23.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.17.1-15
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.17.1-12
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-2
- Rebuilt for Python 3.7

* Thu Feb 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.17.1-1
- Update to 1.17.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16.4-1
- Update to 1.16.4

* Sat Mar 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16-1
- Update to 1.16 (RHBZ #1428620)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.15-2
- Rebuild for Python 3.6

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.15-1
- Initial package
