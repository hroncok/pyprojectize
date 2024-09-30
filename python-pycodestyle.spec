%global module_name pycodestyle

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{module_name}
# WARNING: When updating pycodestyle, check not to break flake8!
Version:        2.11.1
Release:        %autorelease
Summary:        Python style guide checker
License:        MIT
URL:            https://pypi.python.org/pypi/%{module_name}
# pypi source missing docs - https://github.com/PyCQA/pycodestyle/issues/1231
Source0:        https://github.com/PyCQA/pycodestyle/archive/%{version}/%{module_name}-%{version}.tar.gz

BuildArch:      noarch

%description
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8. It has a plugin architecture, making new checks easy, and
its output is parseable, making it easy to jump to an error location in your
editor.

%if %{with python2}
%package -n python2-%{module_name}
Summary:        Python style guide checker

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-setuptools


%description -n python2-%{module_name}
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8. It has a plugin architecture, making new checks easy, and
its output is parseable, making it easy to jump to an error location in your
editor.
%endif


%package -n python%{python3_pkgversion}-pycodestyle
Summary:    Python style guide checker
Conflicts:      python-pycodestyle < %{version}-%{release}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  make

%description -n python%{python3_pkgversion}-pycodestyle
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8. It has a plugin architecture, making new checks easy, and
its output is parseable, making it easy to jump to an error location in your
editor.

This is a version for Python %{python3_pkgversion}.


%prep
%autosetup -n %{module_name}-%{version} -p1

# Remove #! from pycodestyle.py
sed --in-place "s:#!\s*/usr.*::" pycodestyle.py


%generate_buildrequires
%pyproject_buildrequires


%build
%if %{with python2}
%py2_build
%endif
%pyproject_wheel

make -C docs man SPHINXBUILD=sphinx-build-%{python3_version}


%install
%if %{with python2}
%py2_install
mv %{buildroot}%{_bindir}/pycodestyle %{buildroot}%{_bindir}/pycodestyle-%{python2_version}
ln -s ./pycodestyle-%{python2_version} %{buildroot}%{_bindir}/pycodestyle-2
%endif

%pyproject_install
mv %{buildroot}%{_bindir}/pycodestyle %{buildroot}%{_bindir}/pycodestyle-%{python3_version}
ln -s ./pycodestyle-%{python3_version} %{buildroot}%{_bindir}/pycodestyle-3
ln -s ./pycodestyle-3 %{buildroot}%{_bindir}/pycodestyle


install -D docs/_build/man/%{module_name}.1 %{buildroot}%{_mandir}/man1/%{module_name}.1


%check
%if %{with python2}
%{__python2} pycodestyle.py --max-doc-length=72 --testsuite testsuite
%{__python2} pycodestyle.py --max-doc-length=72 --doctest
%endif
%pytest -v


%if %{with python2}
%files -n python2-%{module_name}
%doc CHANGES.txt README.rst
%license LICENSE
%{_bindir}/pycodestyle-2
%{_bindir}/pycodestyle-2.7
%{python2_sitelib}/%{module_name}.py*
%{python2_sitelib}/%{module_name}-%{version}.dist-info
%endif

%files -n python%{python3_pkgversion}-pycodestyle
%doc README.rst CHANGES.txt
%license LICENSE
%{_mandir}/man1/%{module_name}.1.gz
%{_bindir}/pycodestyle
%{_bindir}/pycodestyle-3
%{_bindir}/pycodestyle-%{python3_version}
%pycached %{python3_sitelib}/%{module_name}.py
%{python3_sitelib}/%{module_name}-%{version}.dist-info/

%changelog
%autochangelog
