%global mod_name flask-whooshee

Name:           python-flask-whooshee
Version:        0.9.0
Release:        7%{?dist}
Summary:        Whoosh integration

License:        BSD-3-Clause
URL:            https://github.com/fedora-copr/flask-whooshee
Source0:        https://pypi.python.org/packages/source/f/%{mod_name}/%{mod_name}-%{version}.tar.gz
# https://github.com/bkabrda/flask-whooshee/pull/19
BuildArch:      noarch


%global _description \
Whoosh integration that allows to create and search custom indexes.

%description %{_description}

%package -n python3-%{mod_name}
Summary:        Whoosh integration
BuildRequires:  python3-devel
BuildRequires:  python3-whoosh
BuildRequires:  python3-flask
BuildRequires:  python3-flask-sqlalchemy
BuildRequires:  python3-flexmock
BuildRequires:  python3-blinker
BuildRequires:  python3-pytest

Requires:       python3-flask-sqlalchemy
Requires:       python3-whoosh
Requires:       python3-blinker
Requires:       python3-flask

%description -n python3-%{mod_name} %{_description}

Python 3 version.

%prep
%autosetup -n %{mod_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
%pyproject_check_import
%{__python3} -m pytest -vv test.py


%install
%pyproject_install
%pyproject_save_files flask_whooshee


%files -n python3-%{mod_name} -f %{pyproject_files}
%doc LICENSE README.md


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.9.0-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.12

* Mon Apr 17 2023 Pavel Raiskup <praiskup@redhat.com> - 0.9.0-1
- New upstream release, https://github.com/fedora-copr/flask-whooshee/releases/tag/v0.9.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 msuchy <msuchy@redhat.com> - 0.8.2-4
- use spdx id
- change license to BSD-3-Clause

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.11

* Tue Jan 25 2022 Jakub Kadlcik <frostyx@email.cz> - 0.8.2-1
- Update to the new upstream version
- Update URL to https://github.com/fedora-copr/flask-whooshee

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Pavel Raiskup <praiskup@redhat.com> - 0.8.1-2
- don't own the whole sitelib, rhbz#1672097

* Fri Jul 16 2021 Pavel Raiskup <praiskup@redhat.com> - 0.8.1-1
- new upstream release, fixed compatibility with SQLAlchemy 1.4 (rhbz#1968979)

* Thu Jul 08 2021 Pavel Raiskup <praiskup@redhat.com> - 0.4.1-19
- port to SQLAlchemy 1.4

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.1-18
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.1-9
- Subpackage python2-flask-whooshee has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 clime <clime@redhat.com> - 0.4.1-3
- Make it f24 compatible

* Sun Feb 05 2017 Robert Kuska <rkuska@gmail.com> - 0.4.1-2
- Follow the latest guidelines

* Tue Jan 31 2017 Robert Kuska <rkuska@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.7-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 02 2015 Robert Kuska <rkuska@redhat.com> - 0.0.7-1
- Update to 0.0.7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 03 2014 Robert Kuska <rkuska@redhat.com> - 0.0.6-4
- Move Python 3 Requires into correct place

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Robert Kuska <rkuska@redhat.com> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Dec 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.0.6-1
- Update to flask-whooshee 0.0.6.
- Drop py3 compat patch, since it's now upstream.
- Use buildroot macro consistently.

* Fri Oct 04 2013 Robert Kuska <rkuska@redhat.com> 0.0.5-4
- Add python3 subpackage

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Robert Kuska <rkuska@redhat.com> 0.0.5-2
- Review fixes

* Wed Apr 10 2013 Robert Kuska <rkuska@redhat.com> 0.0.5-1
- Initial package
