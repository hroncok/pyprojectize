%if 0%{?rhel}
%if 0%{?el9}
# Skip tests on EL9 due to missing dependencies
%bcond_with check
%else
%bcond_without check
%endif
# pypandoc is an optional dependency and is not available in EPEL
%bcond_with doc
%else
%bcond_without check
%bcond_without doc
%endif

# Created by pyp2rpm-3.3.5
%global pypi_name dcrpm

Name:           python-%{pypi_name}
Version:        0.6.3
Release:        %autorelease
Summary:        A tool to detect and correct common issues around RPM database corruption

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/facebookincubator/dcrpm
Source:         %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(setuptools)
%if %{with check}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(testslide)
BuildRequires:  dnf
BuildRequires:  libdb-utils
BuildRequires:  lsof
%endif
%if %{with doc}
BuildRequires:  python3dist(pypandoc)
%endif

%global _description %{expand:
dcrpm is a tool to detect and correct common issues around RPM database
corruption.}

%description %{_description}


%package -n     %{pypi_name}
Summary:        %{summary}
%if 0%{?el8}
%py_provides    python3-%{pypi_name}
%endif

Requires:       python3dist(psutil)
Requires:       python3dist(setuptools)
Requires:       lsof
Recommends:     libdb-utils

%description -n %{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove unnecessary shebang
sed -e '\|#!/usr/bin/env python|d' -i dcrpm/*.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%if 0%{?el8}
# needed with setuptools < 40.9.0
mv legacy_setup.py setup.py
%endif


%build
%py3_build


%install
%py3_install


%check
%py3_check_import %{pypi_name}
%if %{with check}
%if 0%{?fedora} >= 37
# https://github.com/facebookincubator/dcrpm/issues/54
%pytest -v --deselect=tests/test_end_to_end.py::DcrpmIntegrationTest::test_rpmdb_centos7_missing_index
%else
%pytest -v
%endif
%endif


%files -n %{pypi_name}
%license LICENSE
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%doc HISTORY.md MANUAL_RPM_CLEANUP.md
%{_bindir}/dcrpm
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
%autochangelog
