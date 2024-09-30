# See BZ 1706315
%{?python_disable_dependency_generator}
%global modname Mastodon

Name:               python-Mastodon
Version:            1.8.1
Release:            7%{?dist}
Summary:            Python wrapper for the Mastodon API


License:            MIT
URL:                https://github.com/halcy/%{modname}.py
Source0:            %{url}/archive/%{version}/%{modname}.py-%{version}.tar.gz
BuildArch:          noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-six
BuildRequires:      python%{python3_pkgversion}-requests
BuildRequires:      python%{python3_pkgversion}-pytest-runner
BuildRequires:      python%{python3_pkgversion}-dateutil
BuildRequires:      python%{python3_pkgversion}-pytz
BuildRequires:      python%{python3_pkgversion}-decorator
BuildRequires:      python%{python3_pkgversion}-pytest-mock
BuildRequires:      python%{python3_pkgversion}-pytest-vcr
BuildRequires:      python%{python3_pkgversion}-pytest-cov
BuildRequires:      python%{python3_pkgversion}-yarl
#BuildRequires:      python%%{python3_pkgversion}-cryptography For test, but need other modules not in Fedora. TODO.
Requires:           python%{python3_pkgversion}-six
Requires:           python%{python3_pkgversion}-pytz
Requires:           python%{python3_pkgversion}-http-ece
Requires:           python%{python3_pkgversion}-magic
%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
%autosetup -n %{modname}.py-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mastodon

#%check
#%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc README.rst *.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.8.1-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 1.8.1-2
- Rebuilt for Python 3.12

* Mon Apr 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.8.1-1
- 1.8.1

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.8.0-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.8.0-1
- 1.8.0

* Mon Nov 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.7.0-1
- 1.7.0

* Mon Nov 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.6.3-1
- 1.6.3

* Thu Nov 17 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.6.1-1
- 1.6.1

* Mon Nov 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.5.2-1
- 1.5.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.1-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.9

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.1-1
- 1.5.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.5.0-1
- 1.5.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.6-1
- 1.4.6

* Mon Jun 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.5-1
- 1.4.5

* Wed Jun 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.3-2
- Patch out blurhash.

* Fri May 31 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.3-1
- 1.4.3

* Mon May 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.2-1
- 1.4.2

* Mon May 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- 1.4.1

* Fri May 10 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-2
- Disable auto-deps.

* Mon Apr 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-1
- 1.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.3.1-2
- Fix broken deps.

* Thu Sep 13 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.3.1-1
- 1.3.1, drop Python2 per BZ 1627376.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.3.0-1
- 1.3.0
- Disabled Python 3 tests, failing in mock.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.2-1
- 1.2.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.2.1-1
- 1.2.1, 2.1.0 compatibility.
- Disabled Python 2 tests, failing in mock.

* Tue Nov 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.1.2-1
- 1.1.2, full Mastodon 2.0.0 support.

* Mon Oct 16 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.1.1-2
- Fix macro usage for review.

* Fri Oct 13 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.1.1-1
- Initial package.
