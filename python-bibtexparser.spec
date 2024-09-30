%global srcname bibtexparser

Name:           python-%{srcname}
Version:        1.4.1
Release:        %autorelease
Summary:        A BibTeX parsing library

# Automatically converted from old format: BSD or LGPLv3 - review is highly recommended.
License:        LicenseRef-Callaway-BSD OR LGPL-3.0-only
URL:            https://github.com/sciunto-org/python-%{srcname}
Source0:        https://github.com/sciunto-org/python-%{srcname}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pyparsing
BuildRequires:  python3-sphinx

%description
BibtexParser is a python library to parse BibTeX files. The code relies
on pyparsing and is tested with unit tests.

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
BibtexParser is a python library to parse BibTeX files. The code relies
on pyparsing and is tested with unittests.

%package doc
Summary: python-bibtexparser documentation

%description doc
Documentation for python-bibtexparser.

%prep
%autosetup -n python-%{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Generate html documentation.
PYTHONPATH=${PWD} sphinx-build docs/source html
# Remove the sphinx-build leftovers.
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%files -n python3-%{srcname}
%doc CHANGELOG README.rst requirements.txt
%license COPYING
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%{python3_sitelib}/bibtexparser/

%files doc
%doc html
%license COPYING

%changelog
%autochangelog
