%global modname prov

Name:           python-%{modname}
Version:        2.0.0
Release:        8%{?dist}
Summary:        W3C Provenance Data Model supporting PROV-JSON and PROV-XML import/export

License:        MIT
URL:            https://pypi.python.org/pypi/prov
Source0:        https://github.com/trungdong/prov/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
A library for W3C Provenance Data Model supporting PROV-JSON and PROV-XML\
import/export.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '%{modname}*'

%files -n python3-%{modname} -f %{pyproject_files}
%doc AUTHORS.rst HISTORY.rst README.rst
%{_bindir}/%{modname}-*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jonathan Wright <jonathan@almalinux.org> - 2.0.0-1
- update to 2.0.0 rhbz#1893550

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.2-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.2-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.2-3
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Thu Jun 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.5.0-5
- use python2- prefix

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Require and BuildRequire python3-rdflib >= 4.2.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuild for Python 3.6

* Thu Oct 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-1
- Initial package
