%global pypi_name snallygaster

Name:           snallygaster
Version:        0.0.12
Release:        %autorelease
Summary:        Tool to scan for secret files on HTTP servers

# Automatically converted from old format: CC0 - review is highly recommended.
License:        CC0-1.0
URL:            https://github.com/hannob/snallygaster
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-dns
BuildRequires:  python3-urllib3

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
snallygaster is a tool that looks for files accessible on web servers that
shouldn't be public and can pose a security risk.Typical examples include
publicly accessible git repositories, backup files potentially containing
passwords or database dumps.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python files or module parts for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# Not running the lint test
# Set RUN_ONLINETESTS to run the tests
%{__python3} tests/test_scan_testdata.py

%files
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%changelog
%autochangelog

