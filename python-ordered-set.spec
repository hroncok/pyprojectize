%global srcname ordered-set
%global dir_name ordered_set

Name:           python-%{srcname}
Version:        4.1.0
Release:        %autorelease
Summary:        Custom MutableSet that remembers its order

License:        MIT
URL:            https://github.com/rspeer/ordered-set
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
#tests
BuildRequires:  python3-nose
BuildRequires:  python3-pytest

%global _description\
An OrderedSet is a custom MutableSet that remembers its order, so that every\
entry has an index that can be looked up.

%description %_description

%package     -n python3-%{srcname}
Summary:        %{summary}
%py_provides    python2-%{srcname}

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{dir_name}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license MIT-LICENSE
%doc README.md

%changelog
%autochangelog
