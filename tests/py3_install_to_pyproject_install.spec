# Created by pyp2rpm-3.2.2
%global srcname XwhyZ
%global modname xyz
Name:           python-%{srcname}
Version:        3.2.1.0
Release:        %autorelease
Summary:        Blah blah blah
License:        MIT
URL:            https://github.com/hroncok/pyprojectize
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

%?python_enable_dependency_generator

%description
This is an artificial spec file created for testing purposes.


%package -n python3-%{srcname}
Summary:        %{summary}
Provides:       python3-%{modname} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{srcname}
...

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{srcname} -i %{python3_sitelib}/*.egg-info cool}


%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
CYTHON_COMPILE=1 %py3_build -- --use-the-force-luke


%install
#%%py3_install

%{?with_python3:%pyproject_install}


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{_bindir}/%{srcname}
%{python3_sitelib}/%{modname}/
%pycached %{python3_sitelib}/_%{modname}.py
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
%autochangelog
