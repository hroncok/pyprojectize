Name:           shyaml
Version:        0.6.2
Release:        %autorelease
Summary:        YAML for command line

License:        BSD-2-Clause
URL:            https://github.com/0k/shyaml
Source0:        https://github.com/0k/shyaml/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Avoids the need to run autogen.sh during setup (which requires the complete
# git repository). Recreate by running './autogen.sh' in a local git checkout
Patch0:         %{name}.autogen.patch
# Remove CHANGELOG from the files to install, as it does not exist.
Patch1:         %{name}.filelist.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist d2to1}
BuildRequires:  %{py3_dist pyyaml}

%description
Simple scripts that allow read access to YAML files through command line.  This
can be handy, if you want to get access to YAML data in your shell scripts.
This scripts supports only read access and it might not support all the
subtleties of YAML specification. But it should support some handy basic query
of YAML file.


%prep
%autosetup -p1 -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/shyaml


%changelog
%autochangelog
