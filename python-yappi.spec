%global srcname yappi

Name:           python-%{srcname}
Version:        1.6.0
Release:        2%{?dist}
Summary:        Yet Another Python Profiler, supports Multithread/CPU time profiling

License:        MIT
URL:            https://github.com/sumerc/yappi
Source0:        https://files.pythonhosted.org/packages/source/y/%{srcname}/%{srcname}-%{version}.tar.gz
Patch01:        0001-Add-support-for-python-3.13.patch

BuildRequires:  git
BuildRequires:  gcc

%description
Yappi, Yet Another Python Profiler, provides multithreading and cpu-time
support to profile python programs.

%package -n python3-%{srcname}
Summary:        Yet Another Python Profiler, supports Multithread/CPU time profiling.

BuildRequires:  python3-devel

%description -n python3-%{srcname}
Yappi, Yet Another Python Profiler, provides multithreading and cpu-time
support to profile python programs.

%prep
%autosetup -n %{srcname}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
mv %{buildroot}%{_bindir}/%{srcname} %{buildroot}%{_bindir}/%{srcname}-%{python3_version}
ln -s %{srcname}-%{python3_version} %{buildroot}%{_bindir}/%{srcname}-3
ln -s %{srcname}-3 %{buildroot}%{_bindir}/%{srcname}

%check
export PATH=$PATH:%{buildroot}/usr/bin
export PYTHONPATH=%{buildroot}/%{python3_sitearch}
%{__python3} run_tests.py

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{srcname}.py*
%{python3_sitearch}/_%{srcname}*.so
%{python3_sitearch}/__pycache__/%{srcname}*
%{python3_sitearch}/%{srcname}-*.dist-info
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-3*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Alfredo Moralejo <amoralej@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Include patch to support 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.6-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.3.6-5
- Rebuilt for Python 3.12

* Fri Apr 21 2023 Florian Weimer <fweimer@redhat.com> - 1.3.6-4
- Drop 0010-Unconditionally-set-LIB_RT_AVAILABLE-and-link-with-l.patch,
  python3-setuptools has been fixed.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Florian Weimer <fweimer@redhat.com> - 1.3.6-2
- Work around broken has_function setup check (#2153038)

* Wed Sep 14 2022 Alfredo Moralejo <amoralej@redhat.com> - 1.3.6-1
- Update to 1.3.6
- Backport upstream patches required to support python 3.11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.3.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Joel Capitao <jcapitao@redhat.com> - 1.3.2-1
- Update to 1.3.2 version (#1902302)
- Included patch to support python 3.10 (#1958896)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Alfredo Moralejo <amoralej@redhat.com> - 1.3.1-1
- Update to 1.3.1 version

* Tue Nov 10 2020 Alfredo Moralejo <amoralej@redhat.com> - 1.3.0-1
- Update to 1.3.0 version

* Fri Aug 28 2020 Alfredo Moralejo <amoralej@redhat.com> - 1.2.5-1
- Update to 1.2.5 version
- Removed python2 subpackage

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.0-1
- Initial version
