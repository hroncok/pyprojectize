%bcond_without tests

%global srcname progressbar2

%global desc %{expand: \
A text progress bar is typically used to display the progress of a long running
operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of the line
is given by a number of widgets.

The progressbar module is very easy to use, yet very powerful. It will also
automatically enable features like auto-resizing when the system supports it.}

Name:           python-%{srcname}
Version:        3.53.2
Release:        %autorelease
Summary:        Library to provide visual progress to long running operations

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

# https://github.com/WoLpH/python-progressbar/pull/256
Patch0001:      0001-Stop-using-deprecated-distutils.util.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       %{py3_dist python-utils}
Requires:       %{py3_dist six}
BuildRequires:  %{py3_dist python-utils}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist pytest}
%if %{with tests}
BuildRequires:  %{py3_dist freezegun} >= 0.3.10
%endif

# obsolete python-progressbar
Obsoletes:      python3-progressbar < 2.3-14
Provides:       python3-progressbar == %{version}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version} -p1
rm -rfv %{srcname}.egg-info

find . -name '*.pyc' -print -delete
find . -name '*.swp' -print -delete
rm -rfv tests/__pycache__/

# do not run coverage in pytest
sed -i -E '/--(no-)?cov/d' pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%if %{with tests}
PYTHONPATH=. %pytest tests
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGES.rst CONTRIBUTING.rst
%{python3_sitelib}/%{srcname}-%{version}-py3.*.dist-info/
%{python3_sitelib}/progressbar

%changelog
%autochangelog
