%global srcname	Flask-Admin
%global pkgname flask-admin
%global sum Simple and extensible admin interface framework for Flask

Name:		python-%{pkgname}
Version:	1.6.1
Release:	6%{?dist}
Summary:	%{sum}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/flask-admin/flask-admin/
Source0:	https://files.pythonhosted.org/packages/source/F/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python%{python3_pkgversion}-devel

%global _description\
Flask-Admin is advanced, extensible and simple to use administrative interface\
building extension for Flask framework.\
\
It comes with batteries included: model scaffolding for SQLAlchemy,\
MongoEngine, MongoDB and Peewee ORMs, simple file management interface\
and a lot of usage samples.\
\
You're not limited by the default functionality - instead of providing simple\
scaffolding for the ORM models, Flask-Admin provides tools that can be used to\
construct administrative interfaces of any complexity, using a consistent look\
and feel.\


%description %_description

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:	%{sum}
Requires:	python%{python3_pkgversion}-flask
Requires:	python%{python3_pkgversion}-wtforms

%description -n python%{python3_pkgversion}-%{pkgname} %_description


%prep
%autosetup -n %{srcname}-%{version}
for f in \
	flask_admin/contrib/pymongo/typefmt.py \
	flask_admin/tests/mock.py \
	flask_admin/tests/fileadmin/files/dummy.txt \
; do
	echo "#Empty file" > $f
done

rm -rf examples
rm flask_admin/translations/README.md


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l flask_admin

%check
%pyproject_check_import
# Tests are not included as they require mongod running


%files -n python%{python3_pkgversion}-%{pkgname} -f %{pyproject_files}
%doc README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.1-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 14 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.6.1-1
- Update to 1.6.1 (Fixes RHBZ#2172123)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.0-2
- Rebuilt for Python 3.11

* Sun May 29 2022 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0. Fixes rhbz#2048301

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.8-2
- Rebuilt for Python 3.10

* Sat May 22 2021 Kevin Fenzi <kevin@scrye.com> - 1.5.8-1
- Update to 1.5.8. Fixes rhbz#1891511

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Kevin Fenzi <kevin@scrye.com> - 1.5.6-1
- Update to 1.5.6. Fixes CVE-2018-16516.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-2
- Subpackage python2-flask-admin has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 27 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.5.2-1
- New version 1.5.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.5.1-1
- New version 1.5.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-5
- Rebuilt for Python 3.7

* Thu Feb 15 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.5.0-4
- make spec file compatible with epel7
- fix bz #1389045

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Lumír Balhar <lbalhar@redhat.com> - 1.5.0-2
- Fix directory ownership in python3 subpackage

* Mon Dec 18 2017 Jan Beran <jberan@redhat.com> - 1.5.0-1
- New version 1.5.0
- Fix of the single package dependence on both Python 2 and Python 3

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.2-5
- Python 2 binary package renamed to python2-flask-admin
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuild for Python 3.6

* Sat Oct 08 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.4.2-1
- Unretired and upgrade to new upstream release

* Fri Feb 12 2016 Sebastian Dyroff <sdyroff@fedoraproject.org> - 1.2.0-2
- add python3 package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 09 2015 Matej Stuchlik <mstuchli@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.0.8-1
- Updated to 1.0.8
- Removed unnecessary requires

* Wed Jan 08 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.0.7-1
- Updated to 1.0.7

* Tue Aug 13 2013 Matej Stuchlik <mstuchli@redhat.com> - 1.0.6-1
- Updated to 1.0.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 08 2013 Matej Stuchlik <mstuchli@redhat.com> - 1.0.5-3
- Requires fixes

* Wed Apr 24 2013 Matej Stuchlik <mstuchli@redhat.com> - 1.0.5-2
- Review fixes

* Tue Mar 19 2013 mstuchli <mstuchli@redhat.com> - 1.0.5-1
- Initial spec
