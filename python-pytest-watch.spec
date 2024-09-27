%global pypi_name pytest-watch
%global file_name pytest_watch
%global desc A zero-config CLI tool that runs [pytest][], and re-runs it \
when a file in your project changes. It beeps on failures and can run arbitrary \
commands on each passing and failing test run.


Name:           python-%{pypi_name}
Version:        4.2.0
Release:        21%{?dist}
Summary:        Local continuous test runner with pytest and watchdog

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-watch
Source0:        https://files.pythonhosted.org/packages/36/47/ab65fc1d682befc318c439940f81a0de1026048479f732e84fe714cd69c0/pytest-watch-4.2.0.tar.gz
Source1:        https://raw.githubusercontent.com/joeyespo/pytest-watch/master/LICENSE
BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-colorama >= 0.3.3
Requires:       python3-docopt >= 0.6.2
Requires:       python3-pytest >= 2.6.4
Requires:       python3-watchdog >= 0.6.0
# Require missing watchdog deps for the package to work
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1360383
Requires:       python3-PyYAML
Requires:       python3-pathtools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%prep
%setup -qn %{pypi_name}-%{version}
# Correct end of line encoding
sed -i 's/\r$//' *.md
sed -i 's/\r$//' %{file_name}/watcher.py
# %%patch0 -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
cp %{SOURCE1} .



%install
%pyproject_install
pushd %{buildroot}%{_bindir}
mv ptw ptw-%{python3_version}
ln -s ptw-%{python3_version} ptw-3
mv pytest-watch pytest-watch-%{python3_version}
ln -s pytest-watch-%{python3_version} pytest-watch-3
popd


%files -n python3-%{pypi_name}
%doc README.md CHANGES.md AUTHORS.md
%license LICENSE
%{python3_sitelib}/%{file_name}-%{version}.dist-info/
%{python3_sitelib}/%{file_name}/
%{_bindir}/ptw-3*
%{_bindir}/pytest-watch-3*


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.2.0-20
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.2.0-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.2.0-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Charalampos Stratakis <cstratak@redhat.com> - 4.2.0-11
- Removal of redundant python-argh dependency

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 4.2.0-1
- Update to 4.2.0
- Drop Python 2 sub-package.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.1.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-4
- Rebuild for Python 3.6

* Tue Sep 06 2016 Julien Enselme <jujens@jujens.eu> - 4.1.0-3
- Choose default py.test command based on Python version

* Thu Aug 11 2016 Julien Enselme <jujens@jujens.eu> - 4.1.0-2
- Remove usage of uneeded %%sum macro
- Correct symlink order
- Don't remove upstream egg-info

* Tue Jul 26 2016 Julien Enselme <jujens@jujens.eu> - 4.1.0-1
- Inital package
