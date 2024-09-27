Name:		python-pandocfilters
Version:	1.5.1
Release:	%autorelease
Summary:	Python module for writing pandoc filters

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/jgm/pandocfilters
Source0:	https://files.pythonhosted.org/packages/source/p/pandocfilters/pandocfilters-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel

%global _docdir_fmt %{name}

%global _description %{expand:
This package provides a few utility functions which make it easier to
write pandoc filters in Python.}

%description %_description

%package -n python3-pandocfilters
Summary:	Python module for writing pandoc filters
%{?python_provide:%python_provide python3-pandocfilters}

%description -n python3-pandocfilters %_description

%prep
%autosetup -n pandocfilters-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-pandocfilters
%license LICENSE
%doc README.rst
%{python3_sitelib}/pandocfilters.py
%{python3_sitelib}/pandocfilters-%{version}.dist-info
%{python3_sitelib}/__pycache__/*

%changelog
%autochangelog
