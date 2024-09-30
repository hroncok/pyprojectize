%{?python_enable_dependency_generator}
%global with_tests 0

Name:           adapt
Version:        1.0.0
Release:        11%{?dist}
Summary:        Mycroft's Adapt Intent Parser
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://adapt.mycroft.ai/
Source0:        https://github.com/MycroftAI/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  libicu-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-devel

%if 0%{?with_tests}
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pyee) = 5
BuildRequires:  python3-pep8
%endif

%description
The Adapt Intent Parser is a flexible and extensible intent definition and 
determination framework. It is intended to parse natural language text into a 
structured intent that can then be invoked programatically.

%package -n python3-adapt
Summary:        A python3 library for Adapt Intent Parser

%description -n python3-adapt
A python3 library for Adapt Intent Parser.

%prep
%autosetup -p1 -n %{name}-release-v%{version}
rm -rf adapt-parser.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-adapt -f %{pyproject_files}
%license LICENSE.md

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.0-9
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.11

* Sun Jan 30 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 24 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.7-3
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.7-1
- Update to 0.3.7

* Thu Jul 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.5-2
- Rebuilt for Python 3.9

* Sun May 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Sat Feb  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.4-3
- Handle newer pyee

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.4-1
- Update to 0.3.4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.3-1
- Update to 0.3.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-2
- Enable python dependency generator

* Sat Dec 22 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.2-1
- Update to 0.3.2
- License changed to Apache 2.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-6
- Rebuilt for Python 3.7

* Sun May 20 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-5
- Drop python2 support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.0-3
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-1
- Initial package
