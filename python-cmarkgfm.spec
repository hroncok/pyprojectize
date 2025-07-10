%global pypi_name cmarkgfm

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        %autorelease
Summary:        Minimal bindings to GitHub's fork of cmark

License:        MIT
URL:            https://github.com/jonparrott/cmarkgfm
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-cffi
BuildRequires:  python3-pytest

%description -n python3-%{pypi_name}
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%prep
%autosetup -n %{pypi_name}-%{version}
chmod -x README.rst LICENSE.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

