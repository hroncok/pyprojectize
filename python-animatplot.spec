%{?python_enable_dependency_generator}
%global srcname animatplot

Name:           python-%{srcname}
Version:        0.4.4
Release:        2%{?dist}
Summary:        Making animating in Matplotlib easy

License:        MIT
URL:            https://github.com/boutproject/animatplot-ng
Source0:        https://github.com/boutproject/animatplot-ng/archive/v%{version}/animatplot-ng-v%{version}.tar.gz
Patch:          https://github.com/boutproject/animatplot-ng/pull/19.patch

BuildArch:      noarch

BuildRequires:  git-core

%description
A Python package for making interactive animated plots build on Matplotlib.


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx) >= 1.5.1
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(matplotlib) >= 2.2
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(setuptools-scm) >= 7

%description -n python3-%{srcname}
A Python package for making interactive animated plots build on Matplotlib.


%package -n     python3-%{srcname}-doc
Summary:        Documentation for python3-%{srcname}

%description -n python3-%{srcname}-doc
Documentation for python3-%{srcname}.


%prep
%autosetup -n %{srcname}-ng-%{version} -p1 -S git

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
# %py3_build

pushd docs
%{__python3} -m sphinx source html
# remove the sphinx-build leftovers
rm -rf html/.{buildinfo,doctrees}
popd


%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install


%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{pytest}


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}_ng-%{version}.dist-info

%files -n python3-%{srcname}-doc
%doc docs/html


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 David Bold <davidsch@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4
- Add patch for Matplotlib 0.3.9

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.4.3-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 04 2023 David Bold <davidsch@fedoraproject.org> - 0.4.3-2
- Fix FTBFS

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.4.1-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 07 2022 David Bold <davidsch@fedoraproject.org> - 0.4.1-15
- Add patch to work around changes in matplotlib

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.4.1-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 David <davidsch@fedoraproject.org> - 0.4.1-11
- Add backport of 0.4.2

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.1-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-2
- Add explicit sphinx_rtd_theme BuildRequires

* Tue Mar 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-1
- Update to latest version

* Sat Feb 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-2
- Enable python dependency generator

* Sat Jan 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version

* Fri Aug 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-2
- Fix license file listing

* Wed Aug 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Initial package.
