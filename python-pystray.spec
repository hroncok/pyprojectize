# Testsuite needs human interaction.
%bcond_with test

%global common_sum Provides system tray integration
%global common_desc This library allows you to create a system tray icon.

%global upname pystray


Name:		python-%{upname}
Version:	0.17.3
Release:	14%{?dist}
Summary:	%{common_sum}

License:	LGPL-3.0-or-later
URL:		https://github.com/moses-palmer/%{upname}
Source0:	%{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildArch:	noarch

%description
%{common_desc}


%package -n python3-%{upname}
Summary:	%{common_sum}

BuildRequires:	python3-devel >= 3.4
BuildRequires:	python3-pillow
BuildRequires:	python3-six
BuildRequires:	python3-xlib >= 0.17

Requires:	libappindicator-gtk3
Requires:	python3-pillow
Requires:	python3-six
Requires:	python3-xlib		>= 0.17

%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname}
%{common_desc}


%package -n python3-%{upname}-doc
Summary:	Documentation-files for python3-%{upname}

BuildRequires:	fdupes
BuildRequires:	python3-sphinx >= 1.3.1

%description -n python3-%{upname}-doc
This package contains the Documentation-files for python3-%{upname}.


%prep
%autosetup -n %{upname}-%{version}

# Remove pre-built and bundled crap.
%{__rm} -fr *.egg*


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
sphinx-build-3 docs docs/build-%{python3_version}/html
%fdupes -s docs/build-%{python3_version}
for f in .buildinfo .doctrees .inv ; do
	%{_bindir}/find docs/ -name "*${f}*" -print0 |			\
		%{_bindir}/xargs -0 %{__rm} -frv
done


%install
%pyproject_install

%if %{with test}
%check
%{__python3} setup.py test
%endif # with test


%files -n python3-%{upname}
%license COPYING*
%doc README.rst
%{python3_sitelib}/%{upname}
%{python3_sitelib}/%{upname}-%{version}.dist-info

%files -n python3-%{upname}-doc
%doc CHANGES.rst docs/build-%{python3_version}/html


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.17.3-13
- convert license to SPDX

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.17.3-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.17.3-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.17.3-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.17.3-2
- Rebuilt for Python 3.10

* Sun May 02 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.17.3-1
- Update to 0.17.3 (fixes rhbz#1903824)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Neal Gompa <ngompa13@gmail.com> - 0.17.1-2
- Add missing dependency on libappindicator-gtk3

* Sat Oct 10 2020 Neal Gompa <ngompa13@gmail.com> - 0.17.1-1
- Update to 0.17.1 (#1873893)

* Mon Aug 03 2020 Neal Gompa <ngompa13@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.3-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-5
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.14.3-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.3-1
- New upstream release (rhbz#1437277)

* Wed Mar 29 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.2-1
- Initial import (rhbz#1436347)

* Tue Mar 28 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.2-0.2
- Added versioned (Build)Requires

* Mon Mar 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.2-0.1
- New upstream release

* Mon Mar 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.1-0.1
- Initial rpm-release (rhbz#1436347)
