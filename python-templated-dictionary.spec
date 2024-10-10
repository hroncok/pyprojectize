%global srcname templated-dictionary
%global python3_pkgversion 3

%if 0%{?rhel} == 7
%global python3_pkgversion 36
%endif

Name:       python-%{srcname}
Version:    1.5
Release:    1%{?dist}
Summary:    Dictionary with Jinja2 expansion

License:    GPL-2.0-or-later
URL:        https://github.com/xsuchy/templated-dictionary

# Source is created by:
# git clone https://github.com/xsuchy/templated-dictionary && cd templated-dictionary
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch: noarch

BuildRequires: python%{python3_pkgversion}-devel
Requires:      python%{python3_pkgversion}-jinja2

%global _description\
Dictionary where __getitem__() is run through Jinja2 template.

%description %_description


%package -n python3-%{srcname}
Summary: %{summary}
%{?py_provides:%py_provides python3-%{srcname}}
%description -n python3-%{srcname} %_description


%prep
%setup -q


%generate_buildrequires
%pyproject_buildrequires


%build
export version="%version"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l templated_dictionary


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
* Tue Sep 17 2024 Pavel Raiskup <praiskup@redhat.com> 1.5-1
- The dictionary.copy() method should copy aliases

* Tue Jan 16 2024 Pavel Raiskup <praiskup@redhat.com>
- make the TemplatedDictionary objects picklable
- use a sandboxed jinja2 environment, fixes CVE-2023-6395

* Tue Jan 16 2024 Pavel Raiskup <praiskup@redhat.com>
- make the TemplatedDictionary objects picklable
- Use a sandboxed jinja2 environment, CVE-2023-6395

* Wed Nov 30 2022 Miroslav Suchý <msuchy@redhat.com> 1.2-1
- use spdx license

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 09 2020 Miroslav Suchý <msuchy@redhat.com> 1.1-1
- require python3- variants and more specifis files section
- remove python2 support

* Wed Nov 18 2020 Miroslav Suchý <msuchy@redhat.com> 1.0-1
- new package
