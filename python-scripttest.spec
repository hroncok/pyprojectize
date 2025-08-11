Name:           python-scripttest
Version:        1.3.0
Release:        %autorelease
Summary:        Helper to test command-line scripts

License:        MIT
URL:            http://pypi.python.org/pypi/ScriptTest/
Source0:        https://github.com/pypa/scripttest/archive/1.3.0.tar.gz

BuildArch:      noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-sphinx
BuildRequires: python%{python3_pkgversion}-pytest

%description
ScriptTest is a library to help you test your interactive 
command-line applications.

With it you can easily run the command (in a subprocess) and see 
the output (stdout, stderr) and any file modifications.

%package -n     python%{python3_pkgversion}-scripttest
Summary:        Helper to test command-line scripts

%description -n python%{python3_pkgversion}-scripttest
ScriptTest is a library to help you test your interactive 
command-line applications.

With it you can easily run the command (in a subprocess) and see 
the output (stdout, stderr) and any file modifications.


%prep
%setup -q -n scripttest-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

sphinx-build -b html docs/ docs/html


%install
%pyproject_install
%pyproject_save_files scripttest

%check
%pyproject_check_import
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-scripttest -f %{pyproject_files}
%doc docs/html
%license docs/license.rst


%changelog
%autochangelog
