# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

%global pypi_name qtconsole

Name:		python-%{pypi_name}
Version:	5.6.0
Release:	%autorelease
Summary:	Jupyter Qt console
License:	BSD-3-Clause

URL:		http://jupyter.org
Source0:	https://files.pythonhosted.org/packages/source/q/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-ipython-sphinx
BuildRequires:	python3-sphinx_rtd_theme

BuildRequires:	desktop-file-utils

%description
Qt-based console for Jupyter with support for rich media output

%package -n     python3-%{pypi_name}
Summary:	Jupyter Qt console
%{?python_provide:%python_provide python3-%{pypi_name}}

Provides:	python3-ipython-gui = %{version}-%{release}
%{?python_provide:%python_provide python3-ipython-gui}
Obsoletes:	python3-ipython-gui < 4
 
Requires:	python3-qt5
Requires:	python3-traitlets
Requires:	python3-jupyter-core
Requires:	python3-jupyter-client >= 4.1
Requires:	python3-pygments
Requires:	python3-ipykernel >= 4.1
Requires:	python3-setuptools

%description -n python3-%{pypi_name}
Qt-based console for Jupyter with support for rich media output

%package -n python-%{pypi_name}-doc
Summary:	Documentation subpackage for qtconsole

%description -n python-%{pypi_name}-doc
Documentation for qtconsole

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs 
sphinx-build docs/source html

# fix file encoding and utf-8
sed -i 's/\r$//' html/objects.inv


# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications examples/jupyter-qtconsole.desktop

%files -n python3-%{pypi_name} 
%license LICENSE
%doc README.md
%{_bindir}/jupyter-qtconsole
%{_datadir}/applications/jupyter-qtconsole.desktop
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%{python3_sitelib}/%{pypi_name}/*
%dir %{python3_sitelib}/%{pypi_name}/

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
%autochangelog
