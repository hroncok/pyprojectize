Name:           python-asttokens
Version:        2.4.1
Release:        %autorelease
Summary:        Module to annotate Python abstract syntax trees with source code positions

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/asttokens
Source:         https://github.com/gristlabs/asttokens/archive/v%{version}/asttokens-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(astroid)
BuildRequires:  python3dist(six)

%global _description %{expand:
The asttokens module annotates Python abstract syntax trees (ASTs) with the
positions of tokens and text in the source code that generated them. This makes
it possible for tools that work with logical AST nodes to find the particular
text that resulted in those nodes, for example for automated refactoring or
highlighting.}

%description %_description

%package     -n python3-asttokens
Summary:        %{summary}
Requires:       %{py3_dist six}

%description -n python3-asttokens %_description

%prep
%autosetup -S git -p1 -n asttokens-%{version}
git tag %{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*'

%check
# test_fixture9 and test_sys_modules tests are currently failing with Python 3.12
%pytest tests/ -v "${TEST_ARGS[@]}"

%files -n python3-asttokens -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
