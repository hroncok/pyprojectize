%global _python_bytecompile_errors_terminate_build 0

%global pypi_name readability-lxml

Name:           python-%{pypi_name}
Version:        0.8.1
Release:        %autorelease
Summary:        Fast html to text parser (article readability tool)

License:        Apache-2.0 
URL:            https://github.com/buriy/python-readability
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(cssselect)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(lxml-html-clean)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(timeout-decorator)

%description
Given a html document, it pulls out the main body text and cleans it up.

This is a python port of a ruby port of arc90's readability project.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:  python3dist(lxml-html-clean)

%?python_enable_dependency_generator

%description -n python3-%{pypi_name}
Given a html document, it pulls out the main body text and cleans it up.

This is a python port of a ruby port of arc90's readability project.


%prep
%autosetup -n python-readability-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove shebang from Python libraries
for lib in readability/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


%build
%py3_build


%install
%py3_install


%check
%{python3} -m pytest -v


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/readability_lxml-*-py%{python3_version}.egg-info
%{python3_sitelib}/readability/


%changelog
%autochangelog
