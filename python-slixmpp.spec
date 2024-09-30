# set upstream name variable
%global srcname slixmpp


Name:           python-slixmpp
Version:        1.8.5
Release:        3%{?dist}
Summary:        Slixmpp is an XMPP library for Python 3.5+

License:        MIT
URL:            https://codeberg.org/poezio/%{srcname}
Source0:        https://codeberg.org/poezio/%{srcname}/archive/slix-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  gcc
BuildRequires:  libidn-devel
# for docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinx_rtd_theme
# for tests
#BuildRequires:  python3-nose
#BuildRequires:  python3-aiohttp
#BuildRequires:  gnupg
#BuildRequires:  python3-aiodns
#BuildRequires:  python3-pytest

%description
Slixmpp is an MIT licensed XMPP library for Python 3.5+. It is a fork
of SleekXMPP. Goals is to only rewrite the core of the library (the low
level socket handling, the timers, the events dispatching) in order to
remove all threads.



%package -n python3-%{srcname}
Summary:        Slixmpp is an XMPP library for Python 3.5+
Requires:       python3-pyasn1-modules
Requires:       python3-aiodns
Requires:       python3-aiohttp
Requires:       python3-emoji
Requires:       python3-defusedxml

%description -n python3-%{srcname}
Slixmpp is an MIT licensed XMPP library for Python 3.5+. It is a fork
of SleekXMPP. Goals is to only rewrite the core of the library (the low
level socket handling, the timers, the events dispatching) in order to
remove all threads.



%package -n python-%{srcname}-doc
Summary:        Documentation for Slixmpp
BuildArch:      noarch
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n python-%{srcname}-doc
Slixmpp is an MIT licensed XMPP library for Python 3.4+. It is a fork
of SleekXMPP. Goals is to only rewrite the core of the library (the low
level socket handling, the timers, the events dispatching) in order to
remove all threads.

This package contains documentation in reST and HTML formats.



%prep
%autosetup -n %{srcname}
# The spinx theme "furo" is not packaged in Fedora yet. Using theme
# from "Read The Doc" instead.
sed -i "s|html_theme = 'furo'|html_theme = 'sphinx_rtd_theme'|" docs/conf.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Build sphinx documentation
pushd docs/
make html
popd # docs


%install
%pyproject_install

# Install html docs
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -pr docs/_build/html %{buildroot}%{_pkgdocdir}/

# Remove buildinfo sphinx documentation
rm -rf %{buildroot}%{_pkgdocdir}/html/.buildinfo

# Fix non-standard modes (775)
chmod 755 %{buildroot}%{python3_sitearch}/%{srcname}/stringprep.cpython-*.so


%check
# Most of the tests availables are failing: temporary disabled



%files -n python3-%{srcname}
%license LICENSE
%doc CONTRIBUTING.rst README.rst
# For arch-specific packages: sitearch
%{python3_sitearch}/%{srcname}-%{version}.dist-info/
%{python3_sitearch}/%{srcname}/


%files -n python-%{srcname}-doc
%doc examples/
%{_pkgdocdir}/



%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.8.5-2
- Rebuilt for Python 3.13

* Wed Feb 28 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 29 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 1.8.4-1
- Update to 1.8.4
- Update SourceURL
- Minor fix in the doc subpackage (no need to move rst files in another directory)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.8.3-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 1.8.3-1
- Update to 1.8.3
- Update SourcesURL

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.8.2-2
- Rebuilt for Python 3.11

* Sun Apr 24 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Sun Mar 27 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1

* Wed Mar 9 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0
- Remove fix-deprecation-warning-8b76485.patch for rawhide and f36
- Fix Requires tag of the doc subpackage
- Add sed scriplet in %%prep section to switch sphinx theme from "furo" to "sphinx_rtd_theme"

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 18 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 1.7.1-4
- Add patch to fix poezio not working on f35

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.1-2
- Rebuilt for Python 3.10

* Fri Apr 30 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Sat Apr 17 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 1.7.0-2
- Add optional requirements (aiohttp, emoji, defusedxml)
- Remove Requires tags from main package

* Tue Mar 30 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0
- Add new BuildRequires for sphinx documentation

* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 1.5.2-4
- Replace glob with %%{python3_version} in %%files section

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 1.5.2-2
- Add BuildRequires: make for
  https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot
- Bump release

* Sat Dec 05 2020 Matthieu Saulnier <fantom@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2
- Remove patch for Python 3.9 compat: fixed upstream in commit 98108d04

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.4.2-5
- Fix Python 3.9 compatibility (#1817778)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Matthieu Saulnier <fantom@fedoraproject.org> - 1.4.2-1
- Bump version to 1.4.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Florent Le Coz <louiz@louiz.org> - 1.4.0-1
- Update to 1.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Rebuilt for Python 3.7

* Sat Apr 28 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-5
- Disable tests in %%check section

* Wed Apr 25 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-4
- Add Requires python3-aiodns
- Remove Patch0 remove-aiodns-dependancy

* Wed Apr 18 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-3
- Fix file ownership in doc subpackage
- Add Requires python3-pyasn1-modules in python3 subpackage

* Mon Apr  2 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-2
- Rename main package to python-slixmpp
- Cleanup specfile
- Replace build and install commands with %%py3_build and %%py3_install
- Split in python3 subpackage
- Split in doc subpackage

* Sun Apr  1 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-1
- Initial package
