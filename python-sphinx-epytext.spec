%global pypi_name sphinx-epytext
Name:           python-%{pypi_name}
Version:        0.0.4
Release:        %autorelease
Summary:        Sphinx epytext extension

License:        MIT
URL:            https://github.com/jayvdb/sphinx-epytext
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package provides basic support for epytext docstrings in Sphinx autodoc.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_epytext

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
