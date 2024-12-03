# FIXME: Test won't work offline
%bcond_with check

%global pypi_name   BuildStream-external
%global sysname     bst_external

Name:           bst-external
Version:        0.30.0
Release:        %autorelease
Summary:        Additional BuildStream plugins
BuildArch:      noarch

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://gitlab.com/BuildStream/bst-external
Source0:        %{pypi_source}

BuildRequires:  python3-devel >= 3.11

BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest) >= 3.1.0
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(tomli)
%if %{with check}
# FIXME: Package was retired in Fedora
# * https://bugzilla.redhat.com/show_bug.cgi?id=1839789
# * https://gitlab.com/BuildStream/bst-external/-/issues/44
#BuildRequires:  python3dist(pep8)
#BuildRequires:  python3dist(pytest-pep8)

#BuildRequires:  python3dist(pytest-env)
BuildRequires:  python3dist(buildstream)
BuildRequires:  python3dist(coverage) >= 4.4
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-datafiles)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(ruamel-yaml)
%endif

%description
A collection of BuildStream plugins that don't fit in with the core plugins for
whatever reason.


%prep
%autosetup -n %{pypi_name}-%{version} -p1
sed 's|coverage == 4.4.0|coverage|' -i setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{sysname}


%if %{with check}
%check
%pyproject_check_import

export PATH=%{buildroot}%{_bindir}:${PATH} 
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{python3} -m pytest -v
%endif


%files -f %{pyproject_files}
%doc README.rst NEWS MAINTAINERS


%changelog
%autochangelog
