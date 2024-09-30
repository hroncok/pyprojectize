%global srcname mongoquery

Name:           python-%{srcname}
Version:        1.4.2
Release:        8%{?dist}
Summary:        Python implementation of mongodb queries

License:        Unlicense
URL:            https://github.com/kapouille/mongoquery
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
A utility library that provides a MongoDB-like query language for querying
Python collections. It's mainly intended to parse objects structured as
fundamental types in a similar fashion to what is produced by JSON or YAML
parsers. It follows the specification of queries for MongoDB version 3.2.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname}
A utility library that provides a MongoDB-like query language for querying
Python collections. It's mainly intended to parse objects structured as
fundamental types in a similar fashion to what is produced by JSON or YAML
parsers. It follows the specification of queries for MongoDB version 3.2.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest -v tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.2-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.2-1
- Update to latest upstream release 1.4.2 (closes #2090356)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.11

* Wed Feb 23 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update to latest upstream release 1.4.1 (closes rhbz#2048020)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.6-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.6-5
- Clean-up spec file

* Wed Aug 05 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.6-4
- BuildRequires python3-setuptools, fix RHBZ#1850951

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-2
- Rebuilt for Python 3.9

* Mon Feb 03 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.6-1
- Release 1.3.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.5-1
- Update to latest upstream: 1.3.5
- Drop Python 2 support

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.3-1
- Update to latest upstream: 1.3.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuild for Python 3.6

* Thu Jun 02 2016 Josef Skladanka <jskladan@redhat.com> - 1.1.0-1
- initial packaging
