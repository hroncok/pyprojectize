Name:           python-hgapi
Version:        1.7.4
Release:        26%{?dist}
Summary:        Python API to Mercurial using the command-line interface

License:        MIT
URL:            https://bitbucket.org/haard/hgapi
Source0:        https://files.pythonhosted.org/packages/36/db/6ad72214343e361c3fae732230e64bb7a5e4580002027782a4406748aee6/hgapi-1.7.4.tar.gz
Source1:        LICENSE

BuildArch:      noarch

%global _description\
hgapi is a pure-Python API to Mercurial, that uses the command-line interface\
instead of the internal Mercurial API. The rationale for this is twofold: the\
internal API is unstable, and it is GPL.\
\
hgapi works for all versions of Mercurial, and will instantly reflect any\
changes to the repository (including hgrc).

%description %_description

%package -n     python3-hgapi
Summary:        Python 3 API to Mercurial using the command-line interface
BuildRequires:  python3-devel
BuildRequires:  mercurial
Requires:       mercurial

%description -n python3-hgapi
hgapi is a pure-Python API to Mercurial, that uses the command-line interface
instead of the internal Mercurial API. The rationale for this is twofold: the
internal API is unstable, and it is GPL.

hgapi works for all versions of Mercurial, and will instantly reflect any
changes to the repository (including hgrc).

%prep
%setup -q -n hgapi-%{version}
cp %{SOURCE1} .
# Remove egg
rm -r hgapi.egg-info
# Apply patch
sed -i 's/\r$//' hgapi/testhgapi.py
# Correct end of line encoding for README.rst
sed -i 's/\r$//' README.rst

rm -rf %{py3dir}
cp -a . %{py3dir}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files hgapi


%check
%pyproject_check_import

%{__python3} setup.py test || true


%files -n python3-hgapi -f %{pyproject_files}
%doc README.rst LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.7.4-25
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.7.4-21
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.7.4-18
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.4-15
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.4-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.4-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.4-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Julien Enselme <jujens@jujens.eu> - 1.7.4-6
- Remove Python 2 subpackage (#1634939)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.4-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.7.4-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Nov 06 2017 Julien Enselme <jujens@jujens.eu> - 1.7.4-1
- Update to 1.7.4
- Update spec file
- Disable tests (they are sloppy)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.2-9
- Python 2 binary package renamed to python2-hgapi
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 1.7.2-3
- Rebuilt for python 3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 14 2014 Julien Enselme <jujens@jujens.eu> - 1.7.2-1
- Update to 1.7.2

* Thu Aug 14 2014 Julien Enselme <jujens@jujens.eu> - 1.7.1-3
- Remove egg-info from upstream.

* Thu Aug 14 2014 Julien Enselme <jujens@jujens.eu> - 1.7.1-2
- Add mercurial as a BuildRequires in order for the tests to succeed.

* Sun Aug 03 2014 Julien Enselme <jujens@jujens.eu> - 1.7.1-1
- Initial packaging
