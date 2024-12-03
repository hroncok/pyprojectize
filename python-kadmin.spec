%global modname kadmin
%global commit          94e50ed0a788d9ff9e4b47a35a65ca22c69b703a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20181207

Name:               python-kadmin
Version:            0.1.2
Release:            25.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:            Python module for kerberos admin (kadm5)

License:            MIT
URL:                https://github.com/rjancewicz/python-%{modname}
Source0:            %{url}/archive/%{commit}/python-%{modname}-%{shortcommit}.tar.gz
Patch0:             https://patch-diff.githubusercontent.com/raw/rjancewicz/python-kadmin/pull/59.patch#/0001-build-one-package-with-two-extensions.patch
Patch1:             12de82aa48a7faeb5bfc618a226f2cc388e2eb4d.patch
Patch2:             python-kadmin-c99.patch
Patch3:             pointer_types.patch
%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      krb5-devel
BuildRequires:      bison
BuildRequires:      gcc

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
%autosetup -p1 -n python-%{modname}-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
export CFLAGS="$CFLAGS -fcommon"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '%{modname}*'

%check
%pyproject_check_import

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-25.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.2-24.20181207git94e50ed
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-23.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-22.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 0.1.2-21.20181207git94e50ed
- Fix C compatibility issue

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-20.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.2-19.20181207git94e50ed
- Rebuilt for Python 3.12

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-18.20181207git94e50ed
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-17.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-16.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.2-15.20181207git94e50ed
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-14.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.2-12.20181207git94e50ed
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-9.20181207git94e50ed
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-8.20181207git94e50ed
- Patch for bad call flags.

* Fri Mar 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-7.20181207git94e50ed
- krb5 rebuild.

* Wed Jan 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-6.20181207git94e50ed
- Build with -fcommon for gcc10.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-5.20181207git94e50ed
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-3.20181207git94e50ed
- Rebuild for krb5.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.1.2-1.20181207git94e50ed
- Corrected URL/Source/Patch, from review.

* Fri Dec 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.1.2-1.20181207
- Initial package.
