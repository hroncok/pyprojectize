%global sum()   A simple %* wrapper around inotify
%global desc \
inotify_simple is a simple Python wrapper around inotify. No fancy bells and \
whistles, just a literal wrapper with ctypes. Only 122 lines of code!

%if 0%{?fedora}
  %bcond_without python3
  %if 0%{?fedora} > 29
    %bcond_with python2
  %else
    %bcond_without python2
  %endif
%else
  %if 0%{?rhel} > 7
    %bcond_with    python2
    %bcond_without python3
  %else
    %bcond_without python2
    %bcond_with    python3
  %endif
%endif

%global sname inotify_simple

Name:           python-%sname
Version:        1.3.5
Release:        11%{?dist}
Summary:        %{sum Python}
BuildArch:      noarch

License:        BSD-2-Clause
URL:            https://github.com/chrisjbillington/%sname
Source0:        https://pypi.org/packages/source/i/%sname/%sname-%version.tar.gz

%if %{with python2}
BuildRequires: python2-devel
BuildRequires: python2-enum34
BuildRequires: python2-setuptools
%endif
%if %{with python3}
BuildRequires: python3-devel
%endif


%description
%desc


%if %{with python2}
%package -n     python2-%sname
Summary:        %{sum Python 2}
Requires:       python2-enum34

%description -n python2-%sname
%{desc}
%endif


%if %{with python3}
%package -n     python3-%sname
Summary:        %{sum Python 3}

%description -n python3-%sname
%{desc}
%endif


%prep
%autosetup -n %sname-%version -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%{?with_python2:%py2_build}
%{?with_python3:%pyproject_wheel}


%install
%{?with_python2:%py2_install}
%{?with_python3:%pyproject_install}
%pyproject_save_files -l %sname


%if %{with python2}
%files -n python2-%sname
%license LICENSE
%python2_sitelib/%sname.py*
%python2_sitelib/%sname-%{version}*.egg-info
%endif


%if %{with python3}
%files -n python3-%sname -f %{pyproject_files}
%endif


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.5-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.5-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.5-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Pavel Raiskup <praiskup@redhat.com> - 1.3.5-1
- new upstream release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Pavel Raiskup <praiskup@redhat.com> - 1.3.4-1
- new upstream release, per release notes:
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.3.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Pavel Raiskup <praiskup@redhat.com> - 1.3.3-1
- new upstream release, per release notes:
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.3.2
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.3.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Pavel Raiskup <praiskup@redhat.com> - 1.3.1-1
- new upstream release, per release notes:
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.3.1
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.2.1
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 12 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-2
- Drop Python 2 package on Fedora > 29 (#1627432)

* Fri Aug 17 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1.8-1
- initial RPM packaging
