%global pypi_name blessed
%global summary A thin, practical wrapper around terminal capabilities in Python
%global _description \
Blessed is a thin, practical wrapper around terminal styling, screen \
positioning, and keyboard input. \
\
It provides: \
- Styles, color, and maybe a little positioning without necessarily clearing \
  the whole screen first. \
- Works great with standard Python string formatting. \
- Provides up-to-the-moment terminal height and width, so you can respond \
  to terminal size changes. \
- Avoids making a mess if the output gets piped to a non-terminal: outputs \
  to any file-like object such as StringIO, files, or pipes. \
- Uses the terminfo(5) database so it works with any terminal type and \
  supports any terminal capability: No more C-like calls to tigetstr and \
  tparm. \
- Keeps a minimum of internal state, so you can feel free to mix and match \
  with calls to curses or whatever other terminal libraries you like. \
- Provides plenty of context managers to safely express terminal modes, \
  automatically restoring the terminal to a safe state on exit. \
- Act intelligently when somebody redirects your output to a file, omitting \
  all of the terminal sequences such as styling, colors, or positioning. \
- Dead-simple keyboard handling: safely decoding unicode input in your \
  system’s preferred locale and supports application/arrow keys. \
- Allows the printable length of strings containing sequences to be \
  determined.

%bcond_without python3

# Disable dependency generator until it has test code
%{?python_disable_dependency_generator}

# Drop Python 2 with Fedora 30 and EL8
%if (0%{?fedora} && 0%{?fedora} < 30) || (0%{?rhel} && 0%{?rhel} < 8)
  %bcond_without python2
%else
  %bcond_with python2
%endif

Name:       python-%{pypi_name}
Version:    1.20.0
Release:    3%{?dist}
Summary:    %{summary}

License:    MIT
URL:        https://github.com/jquast/blessed
Source0:    %{pypi_source}
BuildArch:      noarch

%if 0%{?el7}
Patch0:     el7_req_fixes.patch
Patch1:     el7_pytest_fixes.patch
%endif

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
BuildRequires:  python2-wcwidth
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-backports-functools_lru_cache
%endif

%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-wcwidth
BuildRequires:  python%{python3_pkgversion}-pytest
%endif

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-six
BuildRequires:  python%{python3_other_pkgversion}-wcwidth
BuildRequires:  python%{python3_other_pkgversion}-pytest
%endif

%description %{_description}


# Python 2 package
%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}

Requires:       python2-six
Requires:       python2-wcwidth
Requires:       python2-backports-functools_lru_cache


%description -n python2-%{pypi_name} %{_description}
%endif

# Python 3 package
%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-wcwidth

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}
%endif

# Python 3 other package
%if 0%{?with_python3_other}
%package -n     python%{python3_other_pkgversion}-%{pypi_name}
Summary:        %{summary}

Requires:       python%{python3_other_pkgversion}-six
Requires:       python%{python3_other_pkgversion}-wcwidth

%description -n python%{python3_other_pkgversion}-%{pypi_name} %{_description}
%endif


%prep
%autosetup -p1 -n %{pypi_name}-%{version}



%generate_buildrequires
%pyproject_buildrequires


%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%pyproject_wheel
%endif

%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%if %{with python3}
%pyproject_install
%pyproject_save_files -l %{pypi_name}
%endif

%if %{with python2}
%py2_install
%endif


%check
%pyproject_check_import

export PYTHONIOENCODING=UTF8
export TERM=xterm-256color
%if %{with python2}
# Skip test that uses pytest.warn, since it's not supported in older versions
%{__python2} -m pytest --strict --verbose --verbose --exitfirst -c /dev/null \
-k 'not test_unknown_preferredencoding_warned_and_fallback_ascii'
%endif

%if %{with python3}
%{__python3} -m pytest --strict --verbose --verbose --exitfirst -c /dev/null
%endif

%if 0%{?with_python3_other}
%{__python3_other} -m pytest --strict --verbose --verbose --exitfirst -c /dev/null
%endif


%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst docs/*.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*.egg-info
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.rst docs/*.rst
%endif

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst docs/*.rst
%{python3_other_sitelib}/%{pypi_name}
%{python3_other_sitelib}/%{pypi_name}-*.egg-info
%endif


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.20.0-2
- Rebuilt for Python 3.13

* Sat Apr 20 2024 Avram Lubkin <aviso@rockhopper.net> - 1.20.0-1
- Update to 1.20.0 (#2167042)
- Remove EL6 patches

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.19.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.19.1-2
- Rebuilt for Python 3.11

* Wed Mar 30 2022 Avram Lubkin <aviso@rockhopper.net> - 1.19.1-1
- Update to 1.19.1 (#2043269)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Avram Lubkin <aviso@rockhopper.net> - 1.19.0-1
- Update to 1.19.0 (#2006163)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Fedora Release Monitoring <aviso@rockhopper.net> - 1.18.1-1
- Update to 1.18.1 (#1932716)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.17.12-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Avram Lubkin <aviso@rockhopper.net> - 1.17.12-1
- Updated to 1.17.12

* Mon Sep 14 2020 Avram Lubkin <aviso@rockhopper.net> - 1.17.10-1
- Updated to 1.17.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Avram Lubkin <aviso@rockhopper.net> - 1.17.8-2
- Add EL7 pytest patch

* Fri Jun 19 2020 Avram Lubkin <aviso@rockhopper.net> - 1.17.8-1
- Updated to 1.17.8

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.4-3
- Rebuilt for Python 3.9

* Sat Mar 28 2020 Avram Lubkin <aviso@rockhopper.net> - 1.17.4-2
- Updated requirements file for EL7

* Sat Mar 28 2020 Avram Lubkin <aviso@rockhopper.net> - 1.17.4-1
- Updated to 1.17.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Avram Lubkin <aviso@rockhopper.net> - 1.16.1-2
- Fix epel6 requirements patch

* Sun Oct 27 2019 Avram Lubkin <aviso@rockhopper.net> - 1.16.1-1
- Updated to 1.16.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Avram Lubkin <aviso@rockhopper.net> - 1.15.0-8
- Disable Python dependency generator until it has test code

* Mon Dec 24 2018 Avram Lubkin <aviso@rockhopper.net> - 1.15.0-7
- Remove Python 2 packages in Fedora 30+ (bz#1661354)
- Clean up spec

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.15.0-6
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Tue Nov 13 2018 Avram Lubkin <aviso@rockhopper.net> - 1.15.0-5
- Build Python 3 version on all platforms

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-3
- Rebuilt for Python 3.7

* Wed Jun 20 2018 Avram Lubkin <aviso@rockhopper.net> - 1.15.0-2
- Fixed spec changelog error

* Wed Jun 20 2018 Avram Lubkin <aviso@rockhopper.net>- 1.15.0-1
- Updated to 1.15.0 (Python 3.7 Support)
- Exit tests on first failure to avoid loops

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.14.1-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.14.1-5
- Fix creation of python2- subpackage

* Wed Oct 04 2017 Avram Lubkin <aviso@rockhopper.net> - 1.14.1-4
- Conflicting ordereddict requirements in EL6

* Wed Oct 04 2017 Avram Lubkin <aviso@rockhopper.net> - 1.14.1-3
- Add EL6 build support

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Aurelien Bompard <abompard@fedoraproject.org> - 1.14.1
- Initial package.
