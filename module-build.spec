Name: module-build
Version: 0.2.1
Release: 9%{?dist}
Summary: Tool/library for building module streams locally.
License: MIT
BuildArch: noarch

URL: https://github.com/mcurlej/module-build
Source0: https://github.com/mcurlej/module-build/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: libmodulemd >= 2.13.0
BuildRequires: python3-gobject
BuildRequires: mock

Requires: createrepo_c
Requires: libmodulemd >= 2.13.0
Requires: mock
Requires: mock-scm


%description
A library and a cli tool for building module streams. 


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files module_build


%check
%pytest


%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/module-build


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.1-8
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.2.1-4
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Martin Curlej <mcurlej@redhat.com> - 0.2.1-2
- Require mock-scm

* Thu Sep 08 2022 Martin Čurlej <mcurlej@redhat.com> - 0.2.1-1
- Build failure fix.
- Added MANIFEST.in file

* Fri Aug 19 2022 Marek Kulik <mkulik@redhat.com> - 0.2.0-1
- Rebase to v0.2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.11

* Tue Feb 01 2022 Martin Čurlej <mcurlej@redhat.com> - 0.1.0-1
- Added the ability to build stand-alone module streams (mcurlej@redhat.com)
- Uses modular dependencies when building module streams (mcurlej@redhat.com)
- Resuming of a failed module stream build on the component level (mcurlej@redhat.com)
