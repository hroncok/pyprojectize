%global srcname dulwich
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

Name:           python-%{srcname}
Version:        0.21.7
Release:        %autorelease
Summary:        Python implementation of the Git file formats and protocols

# Automatically converted from old format: GPLv2+ or ASL 2.0 - review is highly recommended.
License:        GPL-2.0-or-later OR Apache-2.0
URL:            https://www.dulwich.io/
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx-epytext

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install
# Remove extra copy of text docs
rm -rf %{buildroot}%{python3_sitearch}/docs/tutorial/

#%check
# FIXME test_non_ascii fails cause of unicode issue
#nosetests -e non_ascii -w dulwich/tests -v

%files -n python3-%{srcname}
%doc AUTHORS README.rst
%license COPYING
%{_bindir}/dul-*
%{_bindir}/%{srcname}
%{python3_sitearch}/%{srcname}*
%exclude %{python3_sitearch}/%{srcname}/tests*

%files -n %{name}-doc
%doc AUTHORS README.rst
%license COPYING
%doc html

%changelog
%autochangelog
