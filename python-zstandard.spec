%if 0%{?rhel}
%bcond_with check
%else
%bcond_without check
%endif

%global pypi_name zstandard
%if 0%{!?pytest:1}
%global pytest %{expand:\\\
  CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\\\
  PATH="%{buildroot}%{_bindir}:$PATH"\\\
  PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}"\\\
  PYTHONDONTWRITEBYTECODE=1\\\
  /usr/bin/pytest}
%endif

%global desc This project provides Python bindings for interfacing with the Zstandard\
compression library. A C extension and CFFI interface are provided.

Name: python-%{pypi_name}
Version: 0.22.0
Release: 5%{?dist}
Summary: Zstandard bindings for Python
License: (BSD-3-Clause OR GPL-2.0-only) AND MIT
URL: https://github.com/indygreg/python-zstandard
Source0: %{pypi_source}
Patch0: %{name}-py313.patch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: gcc
BuildRequires: libzstd-devel
BuildRequires: python3-devel
BuildRequires: python3-cffi
%if %{with check}
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
%endif
# https://github.com/indygreg/python-zstandard/issues/48
Provides: bundled(zstd) = 1.5.5

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -r %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%if %{with check}
%check
%pyproject_check_import

mv zstandard{,.src}
export ZSTD_SLOW_TESTS=1
%pytest -v\
        --numprocesses=auto
mv zstandard{.src,}
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license zstd/COPYING
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.22.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.22.0-1
- update to 0.22.0 (resolves rhbz#2247527)
- fix build with Python 3.13 (resolves rhbz#2245876)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.21.0-2
- Rebuilt for Python 3.12

* Wed May 24 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.21.0-1
- update to 0.21.0 (#2172363)
- bump bundled zstd version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Dominik Mierzejewski <dominik@greysector.net> 0.19.0-1
- update to 0.19.0 (#2138646)

* Wed Oct 05 2022 Dominik Mierzejewski <dominik@greysector.net> 0.18.0-1
- update to 0.18.0 (#2099853)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.17.0-2
- Rebuilt for Python 3.11

* Tue Feb 15 2022 Dominik Mierzejewski <dominik@greysector.net> 0.17.0-1
- update to 0.17.0 (#2042593)
- drop obsolete patch

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Dominik Mierzejewski <dominik@greysector.net> 0.16.0-1
- update to 0.16.0 (#2014873)
- drop obsolete patch
- improve patch for inconsistent `closed` attribute issue

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.15.2-2
- Rebuilt for Python 3.10

* Mon Mar 01 2021 Dominik Mierzejewski <dominik@greysector.net> 0.15.2-1
- update to 0.15.2 (#1933476)
- fix tests on s390x

* Wed Feb 03 2021 Dominik Mierzejewski <dominik@greysector.net> 0.15.1-1
- update to 0.15.1 (#1924620)
- work around weird test failure
- fix tests on i686 and s390x

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Dominik Mierzejewski <dominik@greysector.net> 0.13.0-1
- initial build
- skip some tests on s390x (https://github.com/indygreg/python-zstandard/issues/105)

