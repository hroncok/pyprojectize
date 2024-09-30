%global upname mistune

%global common_description %{expand:
The fastest markdown parser in pure Python, inspired by marked.}

Name:           python-mistune08
Version:        0.8.4
Release:        14%{?dist}
Summary:        Markdown parser for Python 

License:        BSD
URL:            https://github.com/lepture/mistune
Source0:        https://github.com/lepture/mistune/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description %{common_description}


%package -n python3-%{upname}08
Summary:        %{summary}
Conflicts:      python3-%{upname}
Obsoletes:      python3-%{upname} < 1
# This is a compatibility package for software that isn't yet updated to work with mistune 2.x
Provides:       deprecated()

%description -n python3-%{upname}08 %{common_description}


%prep
%setup -q -n %{upname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{upname}

%py3_shebang_fix %{buildroot}%{python3_sitelib}
%{_fixperms} %{buildroot}/*


%check
%pytest


%files -n python3-%{upname}08 -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.4-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.4-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 12 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.4-7
- Add `Obsoletes` to provide an upgrade path
- Mark as deprecated()

* Tue Oct 11 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.4-6
- New python-mistune08 compatibility package, forked off python-mistune

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.4-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.8.4-1
- Update to 0.8.4

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.3-16
- Rebuilt for Python 3.10

* Mon Feb 08 2021 Charalampos Stratakis <cstratak@redhat.com> - 0.8.3-15
- Run the tests with pytest instead of nose

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-10
- Subpackage python2-mistune has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Sep 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-9
- Modernize packaging, drop build dependency on python2-Cython

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Dec 19 2017 Christian Dersch <lupinix@fedoraproject.org> - 0.8.3-1
- new version (0.8.3)
- fixes CVE-2017-15612 and CVE-2017-16876

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.3-7
- Python 2 binary package renamed to python2-mistune
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Christian Dersch <lupinix@mailbox.org> - 0.7.3-1
- new version

* Sat Feb 27 2016 Christian Dersch <lupinix@mailbox.org> - 0.7.2-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 23 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.7.1-1
- new version

* Wed Jun 17 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.6-1
- new upstream release

* Mon Apr 20 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.5.1-1
- new upstream release (0.5.1)

* Fri Dec  5 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.5-1
- new upstream release
- enabled tests

* Thu Dec  4 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.4.1-2
- spec fixes

* Thu Dec  4 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.4.1-1
- initial spec  
