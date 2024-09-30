%global modname docker-squash

Name:           python-%{modname}
Version:        1.1.0
Release:        7%{?dist}
Summary:        Docker layer squashing tool
License:        MIT
URL:            https://github.com/goldmann/docker-squash
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

%global _description \
Tool to squash layers in Docker images.

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-six
BuildRequires:  python3-docker
Requires:       python3-six
Requires:       python3-docker

Provides:       python3-docker-scripts = %{version}-%{release}
Obsoletes:      python3-docker-scripts <= 1.0.0-0.2.rc2

%description -n python3-%{modname} %_description

Python 3 version.

%prep
%setup -q -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
py.test-%{python3_version} -v tests/test_unit*.py

%install
%pyproject_install
%pyproject_save_files docker_squash

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/docker-squash

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.12

* Wed May 17 2023 Marek Goldmann <mgoldman@redhat.com> - 1.1.0-1
- Release 1.1.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.0.9-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Marek Goldmann <mgoldman@redhat.com> - 1.0.9-1
- Release 1.0.9

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.8-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.8-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Marek Goldmann <mgoldman@redhat.com> - 1.0.8-1
- Release 1.0.8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-4
- Remove python2 subpackage (#1636933)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Marek Goldmann <mgoldman@redhat.com> - 1.0.7-1
- Release 1.0.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.5-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Adam Miller <maxamillion@gmail.com> - 1.0.5-7
- Include the docker-squash upstream patch to add docker client api 2.x support

* Wed Aug 23 2017 Adam Miller <maxamillion@gmail.com> - 1.0.5-6
- Migrate from python-docker-py to python-docker, the former is deprecated
  upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-3
- Rebuild for Python 3.6

* Wed Dec 07 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.5-2
- Added missing sources

* Wed Dec 07 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.5-1
- Upstream release 1.0.5

* Tue Nov 08 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Thu Sep 01 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Thu Aug 25 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Tue Aug 16 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-1
- 1.0.1 release

* Wed Jul 27 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-1
- 1.0.0 upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.9.rc6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 27 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.8.rc6
- Upstream 1.0.0rc6 release

* Mon May 23 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.7.rc5
- 1.0.0rc5 release

* Tue May 10 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.6.rc4
- Release bump

* Wed Apr 13 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.5.rc4
- Adapt to current guidelines thanks to Zbigniew Jędrzejewski-Szmek

* Fri Apr 08 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.4.rc4
- Upstream release 1.0.0rc4

* Fri Apr 01 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.3.rc3
- Project rename and new 1.0.0rc3 release

* Fri Apr 01 2016 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.2.rc2
- Someone forgot to upload sources...

* Fri Apr 01 2016 Marek Goldmann - 1.0.0-0.1.rc2
- Upstream release 1.0.0rc2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Martin Milata <mmilata@redhat.com> - 0.4.4-1
- Upstream release 0.4.4

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Marek Goldmann <mgoldman@redhat.com> - 0.4.2-1
- Upstream release 0.4.2

* Tue Jun 02 2015 Marek Goldmann <mgoldman@redhat.com> - 0.4.1-1
- Upstream release 0.4.1

* Wed May 27 2015 Marek Goldmann <mgoldman@redhat.com> - 0.4.0-1
- Upstream release 0.4.0
- Run unit tests at build time

* Mon May 18 2015 Marek Goldmann <mgoldman@redhat.com> - 0.3.8-1
- Upstream release 0.3.8

* Fri May 15 2015 Marek Goldmann <mgoldman@redhat.com> - 0.3.7-1
- Upstream release 0.3.7
- Make sure the /usr/lib/python2.7/site-packages/docker_scripts
  is owned by this package

* Thu May 14 2015 Marek Goldmann <mgoldman@redhat.com> - 0.3.6-1
- Upstream release 0.3.6

* Tue May 12 2015 Marek Goldmann <mgoldman@redhat.com> - 0.3.4-1
- Initial packaging

