%global srcname pytools

Name:           python-%{srcname}
Version:        2024.1.3
Release:        %autorelease
Summary:        Collection of tools for Python

License:        MIT
URL:            https://pypi.python.org/pypi/pytools
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description \
Pytools is a big bag of things that are "missing" from the Python standard\
library. This is mainly a dependency of my other software packages, and is\
probably of little interest to you unless you use those. If you're curious\
nonetheless, here's what's on offer:\
\
  * A ton of small tool functions such as `len_iterable`, `argmin`,\
    tuple generation, permutation generation, ASCII table pretty printing,\
    GvR's mokeypatch_xxx() hack, the elusive `flatten`, and much more.\
  * Michele Simionato's decorator module\
  * A time-series logging module, `pytools.log`.\
  * Batch job submission, `pytools.batchjob`.\
  * A lexer, `pytools.lex`.

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(platformdirs)


%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst PKG-INFO

%changelog
%autochangelog
