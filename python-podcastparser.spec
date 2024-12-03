%global modname podcastparser
%global sum     Simplified, fast RSS parsing library

Name:               python-%{modname}
Version:            0.6.10
Release:            7%{?dist}
Summary:            %{sum}

License:            ISC
URL:                https://github.com/gpodder/%{modname}
Source0:            %{url}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz

BuildRequires:      python3-devel

BuildArch:          noarch

%description
The podcast parser project is a library from the gPodder project to provide
an easy and reliable way of parsing RSS- and Atom-based podcast feeds in
Python.


%package -n python3-%{modname}
Summary:            %{sum}


%description -n python3-%{modname}
%{sum}.


%prep
%autosetup -n %{modname}-%{version}

# Better safe than sorry
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '%{modname}*'

%{!?_licensedir: %global license %doc}

%check
%pyproject_check_import

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.md


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.10-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.10-2
- Rebuilt for Python 3.12

* Wed Apr 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.6.10-1
- 0.6.10

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.6.9-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 15 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.6.9-1
- 0.6.9

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.8-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.6.8-1
- 0.6.8

* Fri Aug 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.6.7-1
- 0.6.7

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.6-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.6.6-1
- 0.6.6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.5-2
- Rebuilt for Python 3.9

* Wed Apr 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.6.5-1
- 0.6.5-1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 0.6.4-1
- 0.6.4

* Thu Oct 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.6.3-6
- Drop python2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.6.3-1
- 0.6.3.

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.6.2-1
- 0.6.2.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.1-1
- Buxfix release.

* Fri Dec 09 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.0-2
- Fixed Source, License and macro usage for review.

* Wed Nov 30 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.0-1
- Initial package.
