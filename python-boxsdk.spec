%global modname boxsdk

%bcond_with tests

Name:               python-boxsdk
Version:            3.13.0
Release:            1%{?dist}
Summary:            Python wrapper for the Box API


License:            Apache-2.0 
URL:                https://github.com/box/box-python-sdk
Source0:            %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz
BuildArch:          noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-requests
BuildRequires:      python%{python3_pkgversion}-six
BuildRequires:      python%{python3_pkgversion}-wrapt
BuildRequires:      python%{python3_pkgversion}-requests-toolbelt
BuildRequires:      python%{python3_pkgversion}-attrs
# Tests don't pass at the moment.
# https://github.com/box/box-python-sdk/issues/494
%if %{with tests}
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-bottle
BuildRequires:      python%{python3_pkgversion}-redis
BuildRequires:      python%{python3_pkgversion}-mock
BuildRequires:      python%{python3_pkgversion}-sqlalchemy
BuildRequires:      python%{python3_pkgversion}-jsonpatch
BuildRequires:      python%{python3_pkgversion}-cryptography
BuildRequires:      python%{python3_pkgversion}-pytz
BuildRequires:      python%{python3_pkgversion}-jwt
%endif

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
%autosetup -n box-python-sdk-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with tests}
%check
pytest-3
%endif

%files -n python%{python3_pkgversion}-%{modname}
%doc *.md
%license LICENSE
%{python3_sitelib}/boxsdk/
%{python3_sitelib}/%{modname}-*.dist-info/

%changelog
* Thu Aug 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.13.0-1
- 3.13.0

* Tue Aug 06 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.12.0-1
- 3.12.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.11.0-1
- 3.11.0

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.10.0-2
- Rebuilt for Python 3.13

* Wed May 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.10.0-1
- 3.10.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.9.2-1
- 3.9.2

* Thu Sep 14 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.9.1-1
- 3.9.1

* Wed Sep 06 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.9.0-1
- 3.9.0

* Tue Aug 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.8.1-1
- 3.8.1

* Tue Jul 25 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.8.0-1
- 3.8.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.7.3-1
- 3.7.3

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.7.2-2
- Rebuilt for Python 3.12

* Fri May 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.7.2-1
- 3.7.2

* Thu May 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.7.1-2
- Unpin python-requests-toolbelt.

* Tue Apr 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.7.1-1
- 3.7.1

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.7.0-1
- 3.7.0

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.6.2-2
- migrated to SPDX license

* Tue Feb 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.6.2-1
- 3.6.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.6.1-1
- 3.6.1

* Wed Jan 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.6.0-1
- 3.6.0

* Wed Nov 30 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.5.1-1
- 3.5.1

* Fri Sep 23 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.5.0-1
- 3.5.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.4.0-1
- 3.4.0

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.11

* Mon May 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.3.0-1
- 3.3.0

* Fri Mar 11 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.2.0-1
- 3.2.0

* Wed Feb 16 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.1.0-1
- 3.1.0

* Wed Jan 26 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.1-1
- 3.0.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.0-1
- 3.0.0

* Wed Dec 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.14.0-1
- 2.14.0

* Thu Sep 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.13.0-1
- 2.13.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.12.1-1
- 2.12.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.12.0-2
- Rebuilt for Python 3.10

* Fri Apr 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.12.0-1
- 2.12.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.11.0-1
- 2.11.0

* Fri Oct 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.10.0-1
- 2.10.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.9.0-1
- 2.9.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.0-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.8.0-1
- 2.8.0

* Thu Mar 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.1-1
- Initial build
