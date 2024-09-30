%global debug_package %{nil}

# Created by pyp2rpm-3.3.7
%global pypi_name crcmod
%global pypi_version 1.7

%global common_description %{expand:
The software in this package is a Python module for generating objects that
compute the Cyclic Redundancy Check (CRC).}

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        CRC Generator

License:        MIT
URL:            http://crcmod.sourceforge.net/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  sed
BuildRequires:  python3dist(sphinx)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%package -n python-%{pypi_name}-doc
Summary:        crcmod documentation
BuildArch:      noarch

%description -n python-%{pypi_name}-doc
Documentation for crcmod

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Use local intersphinx inventory
sed -r \
    -e 's|http://docs.python.org|%{_docdir}/python3-docs/html|' \
    -i docs/source/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
for test in test/*; do
  PYTHONPATH="%{buildroot}%{python3_sitearch}" %python3 $test
done

%files -n python3-%{pypi_name} -f %{pyproject_files}

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
