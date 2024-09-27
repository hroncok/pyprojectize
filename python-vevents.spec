%global commit0 3ff37a2a93f05f33ddd2baef017a677e8d02d18e
%global date0   20149631
%global scommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           python-vevents
# version 0.1.0 unofficially mentioned in sitepackages
Version:        0.1.0
Release:        0.19.%{date0}git%{scommit0}%{?dist}
Summary:        vSphere Events from the command-line

# license header in src/vevents-cli for BSD, PR#2
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/dnaeon/py-vevents
Source0:        %{url}/archive/%{commit0}/%{name}-%{scommit0}.tar.gz

BuildArch:      noarch

%description
vEvents is an application that allows you to view and monitor
vSphere Events from the command-line.

%package     -n python%{python3_pkgversion}-vevents
Summary:        vSphere Events from the command-line
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pyvmomi
BuildRequires:  python%{python3_pkgversion}-docopt
BuildRequires:  python%{python3_pkgversion}-vconnector 
%{?python_provide:%python_provide python%{python3_pkgversion}-vevents}
# no magic dependencies in epel
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-pyvmomi
Requires:       python%{python3_pkgversion}-docopt
Requires:       python%{python3_pkgversion}-vconnector
%endif

%description -n python%{python3_pkgversion}-vevents
vEvents is an application that allows you to view and monitor
 vSphere Events from the command-line.


%prep
%autosetup -npy-vevents-%{commit0}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}


%files -n python%{python3_pkgversion}-vevents
#%%license add-license-file-here
%doc README.md
# egg-info only due to single binary
%{python3_sitelib}/vevents-%{version}.dist-info/
%{_bindir}/vevents-cli


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.0-0.19.20149631git3ff37a2
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.18.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.1.0-0.17.20149631git3ff37a2
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.16.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.15.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.14.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.13.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.12.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.1.0-0.11.20149631git3ff37a2
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.10.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.9.20149631git3ff37a2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.0-0.8.20149631git3ff37a2
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.7.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.6.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-0.5.20149631git3ff37a2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.4.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-0.3.20149631git3ff37a2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 0.1.0-0.2.20149631git3ff37a2
- drop brand

* Thu Jul 25 2019 Raphael Groner <projects.rg@smart.ms> - 0.1.0-0.1.20149631git3ff37a2
- initial
