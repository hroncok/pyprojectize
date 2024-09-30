Name:               pag
Version:            0.8
Release:            23%{?dist}
Summary:            Commandline interaction with pagure.io

License:            GPL-3.0-or-later
URL:                https://pagure.io/pag
Source0:            https://pypi.io/packages/source/p/pag/pag-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-click
BuildRequires:      python3-PyYAML
BuildRequires:      python3-beautifulsoup4
BuildRequires:      python3-requests
BuildRequires:      python3-fedora

Requires:           python3-click
Requires:           python3-PyYAML
Requires:           python3-beautifulsoup4
Requires:           python3-requests
Requires:           python3-fedora
Requires:           git-core

%description
pag is a command line tool for interacting with the git repository hosting
service https://pagure.io.  It provides support for cloning projects and
opening new ones.

It is under active development and will be gaining new features over time.

%prep
%autosetup -n pag-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pag

# For rpmlint
find %{buildroot}/%{python3_sitelib}/pag -name "*.py" -exec chmod -x {} \;

# This is a duplicate command
rm -f %{buildroot}/%{_bindir}/pagcli

# And, we're on python3, thank you setuptools.
sed -i 's|/usr/bin/python$|/usr/bin/python3|' %{buildroot}/%{_bindir}/pag

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/pag

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.8-22
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 0.8-18
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.8-15
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8-12
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-9
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8-2
- Rebuilt for Python 3.7

* Sat Apr 28 2018 Lubomír Sedlář <lsedlar@redhat.com> - 0.8-1
- New upstream release 0.8

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 18 2017 Lubomír Sedlář <lsedlar@redhat.com> - 0.7-1
- New upstream release 0.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6-4
- Rebuild for Python 3.6

* Thu Aug  4 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.6-3
- Add dependency on git-core

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Jun 04 2016 Ralph Bean <rbean@redhat.com> - 0.6-1
- new version

* Mon Apr 25 2016 Ralph Bean <rbean@redhat.com> - 0.5-1
- new version

* Mon Apr 11 2016 Ralph Bean <rbean@redhat.com> - 0.4-1
- Latest upstream resolves license ambiguity.
- Fix license field in the spec file to match upstream.
- Elongate description.

* Fri Apr 08 2016 Ralph Bean <rbean@redhat.com> - 0.3-1
- Initial packaging for Fedora
