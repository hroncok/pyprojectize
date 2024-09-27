# Created by pyp2rpm-3.3.5
%global pypi_name codecov

%global common_description %{expand:
Find coverage reports for supported languages, gather them and submit them to
Codecov.}

Name:           python-%{pypi_name}
Version:        2.1.12
Release:        %autorelease
Summary:        Python report uploader for Codecov

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/codecov/codecov-python
# PyPI doesn't include tests so use the GitHub tarball instead
Source0:        %{url}/archive/v%{version}/codecov-python-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ddt)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(requests)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} == 32
%py_provides    python3-%{pypi_name}
%endif

%description -n python3-%{pypi_name}
%{common_description}

%prep
%autosetup -n codecov-python-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unneeded shebang
sed -e "\|#!/usr/bin/env python3|d" -i %{pypi_name}/*.py

%build
%py3_build

%install
%py3_install

%check
# Disable tests that require network access
%pytest tests/test.py \
  --deselect tests/test.py::TestUploader::test_bowerrc_none \
  --deselect tests/test.py::TestUploader::test_prefix \
  --deselect tests/test.py::TestUploader::test_send

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/codecov
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
