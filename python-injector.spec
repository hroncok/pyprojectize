# Created by pyp2rpm-3.3.2
%global pypi_name injector

Name:           python-%{pypi_name}
Version:        0.21.0
Release:        %autorelease
Summary:        Python dependency injection framework inspired by Guice

License:        BSD-3-Clause
URL:            https://github.com/alecthomas/injector
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel >= 3.10

%global _description %{expand:
Dependency injection as a formal pattern is less useful in Python than in other
languages, primarily due to its support for keyword arguments, the ease with
which objects can be mocked, and its dynamic nature.

That said, a framework for assisting in this process can remove a lot of
boiler-plate from larger applications. That's where Injector can help. It
automatically and transitively provides keyword arguments with their values. As
an added benefit, Injector encourages nicely compartmentalised code through the
use of `Module` s.

While being inspired by Guice, it does not slavishly replicate its API.
Providing a Pythonic API trumps faithfulness.}

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%package -n     python3-%{pypi_name}-doc
Summary:        Documentation for Python dependency injection framework

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(typing-extensions)

%description -n python3-%{pypi_name}-doc %{_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install


%files -n python3-%{pypi_name}
%license COPYING
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%files -n python3-%{pypi_name}-doc
%doc html


%changelog
%autochangelog
