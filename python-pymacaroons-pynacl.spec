%{?python_enable_dependency_generator}
%global pkgname pymacaroons-pynacl

%global desc This is a Python re-implementation of the libmacaroons C library.\
Macaroons, like cookies, are a form of bearer credential. Unlike\
opaque tokens, macaroons embed caveats that define specific authorization\
requirements for the target service, the service that issued the root macaroon\
and which is capable of verifying the integrity of macaroons it receives.\
\
Macaroons allow for delegation and attenuation of authorization. They are\
simple and fast to verify, and decouple authorization policy from the\
enforcement of that policy.\


Name:           python-%{pkgname}
Version:        0.13.0
Release:        20%{?dist}
Summary:        Library providing non-opaque cookies for authorization

License:        MIT
URL:            https://github.com/ecordell/pymacaroons
Source0:        %{url}/archive/v%{version}/pymacaroons-v%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires: make
BuildRequires:  python3-devel

%description -n python3-%{pkgname}
%{desc}


%package doc
Summary: Documentation for python-pymacaroons-pynacl
BuildRequires:  python3-sphinx

%description doc
Documentation for the python-pymacaroons-pynacl package.

%{desc}


%prep
%autosetup -n pymacaroons-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

make %{?_smp_mflags} -C docs SPHINXBUILD=sphinx-build-3 html PYTHONPATH=$(pwd)
rm docs/_build/html/.buildinfo


%install
%pyproject_install
%pyproject_save_files -l '*'


# check
# Unfortunately, the test suite relies on an incredibly old version of python-hypothesis
# (1.0.0) which is not API compatible with the version we ship in Fedora.
# nosetests-3


%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.md


%files doc
%license LICENSE
%doc README.md docs/_build/html


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.13.0-19
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.13.0-15
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.13.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.13.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Dan Callaghan <djc@djc.id.au> - 0.13.0-1
- New upstream release 0.13.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.3-7
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-6
- Subpackage python2-pymacaroons-pynacl has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Jeremy Cline <jeremy@jcline.org> - 0.9.3-1
- Initial package
