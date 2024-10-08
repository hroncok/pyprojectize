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
BuildRequires:  python3-setuptools_scm

%description
This is an artificial spec file created for testing purposes.


%package -n python3-%{srcname}
Summary:        %{summary}
Provides:       python3-%{modname} = %{version}-%{release}
%py_provides    python3-%{modname}

%description -n python3-%{srcname}
...

%pyproject_extras_subpkg -n python3-%{srcname} cool


%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel -C--global-option=--use-the-force-luke


%install
%pyproject_install
%pyproject_save_files -l %{modname} _%{modname}


%check
%{__python3} setup.py test


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{srcname}


%changelog
%autochangelog
