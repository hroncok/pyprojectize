%global debug_package %{nil}

Name:		cranc
Version:	1.1.0
Release:	18%{?dist}
Summary:	Pagure CLI for handling pull requests

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://pagure.io/cranc
Source0:	https://releases.pagure.org/cranc/cranc-%{version}.tar.gz

BuildArch:	noarch
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-black
%endif
BuildRequires:	python3-devel
Requires:	python3-click
Requires:	python3-libpagure
Requires:	python3-requests
Requires:	python3-pygit2
Requires:	python3-git-url-parse

%description
Cranc is a Pagure command line interface tool

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cranc

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -v
%endif


%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
# For noarch packages: sitelib
%{_bindir}/cranc


%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.0-16
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.0-12
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-9
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Lenka Segura <lenka@sepu.cz> - 1.1.0
- Drop pbr dependency
- update to version 1.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-5
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Lenka Segura <lenka@sepu.cz> - 1.0.1
- update to version 1.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Lenka Segura <lenka@sepu.cz> - 0.2.2-3
- python-cranc renamed to cranc
- typos fixed (BuildRequires
- changelog fixed

* Mon Feb 25 2019 Lenka Segura <lenka@sepu.cz> - 0.2.2-2
- Python2 removed
- %%{_bindir} used
- cranc specified for %%{python3_sitelib}
- version-release info corrected in changelog

* Tue Feb 19 2019 Lenka Segura <lenka@sepu.cz> - 0.2.2
- Update to 0.2.2
