%global modname nose

Name:           python-%{modname}
Version:        1.3.7
Release:        %autorelease
BuildArch:      noarch

# Automatically converted from old format: LGPLv2+ and Public Domain - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-Public-Domain
Summary:        Deprecated test runner for Python
URL:            https://nose.readthedocs.org/en/latest/
Source0:        http://pypi.python.org/packages/source/n/nose/nose-%{version}.tar.gz
# Make compatible with coverage 4.1
# https://github.com/nose-devs/nose/pull/1004
Patch0:         python-nose-coverage4.patch
# Fix python 3.5 compat
# https://github.com/nose-devs/nose/pull/983
Patch1:         python-nose-py35.patch
# Fix UnicodeDecodeError with captured output
# https://github.com/nose-devs/nose/pull/988
Patch2:         python-nose-unicode.patch
# Allow docutils to read utf-8 source
Patch3:         python-nose-readunicode.patch
# Fix Python 3.6 compatibility
# Python now returns ModuleNotFoundError instead of the previous ImportError
# https://github.com/nose-devs/nose/pull/1029
Patch4:         python-nose-py36.patch
# Remove a SyntaxWarning (other projects may treat it as error)
Patch5:         python-nose-py38.patch
# Remove use_2to3 from setuptools.setup() call
# We call the command line tool in %%prep instead
# https://fedoraproject.org/wiki/Changes/Setuptools_58+
Patch6:         python-nose-no-use_2to3.patch
# Import unittest.TextTestResult instead of removed unittest._TextTestResult
# Use ConfigParser.read_file() instead of .readfp()
# Adapt test_xunit to tracebacks/exceptions with ^^^^^^^^ lines
# Migrate from removed inspect.getargspec() to inspect.getfullargspec()
Patch7:         python-nose-py311.patch
# Adapt doctest to new tracebacks/exceptions on Python 3.11+
Patch8:         python-nose-py311-doctest.patch
# Python 3.12 support from mdmintz/pynose
# https://github.com/mdmintz/pynose/commit/b5247565df (rebased)
# changes in tests hacked on top
Patch9:         python-nose-py312.patch
# Python 3.13 removes 2to3, so we have a patch instead
Patch10:        python-nose-2to3.patch

BuildRequires:  dos2unix

%global _description %{expand:
A deprecated test runner for Python.

See https://fedoraproject.org/wiki/Changes/DeprecateNose}

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-coverage >= 3.4-1
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-%{modname}}
Conflicts:      python-%{modname} < %{version}-%{release}
Obsoletes:      python-%{modname}-docs < 1.3.7-30

# This package is deprecated, no new packages in Fedora can depend on it
# https://fedoraproject.org/wiki/Changes/DeprecateNose
# Contact the change owners for help migrating to pytest
Provides:       deprecated()

%description -n python3-%{modname} %_description

%prep
%autosetup -p1 -n %{modname}-%{version}

dos2unix examples/attrib_plugin.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
mkdir -p %{buildroot}%{_mandir}/man1
%pyproject_install
mv %{buildroot}%{_bindir}/nosetests{,-%{python3_version}}
ln -sf nosetests-%{python3_version} %{buildroot}%{_bindir}/nosetests-3
mv %{buildroot}%{_prefix}/man/man1/nosetests.1 %{buildroot}%{_mandir}/man1/nosetests-%{python3_version}.1
ln -sf nosetests-%{python3_version}.1 %{buildroot}%{_mandir}/man1/nosetests-3.1
ln -sf nosetests-3 %{buildroot}%{_bindir}/nosetests
ln -sf nosetests-3.1 %{buildroot}%{_mandir}/man1/nosetests.1

%check
%{__python3} setup.py build_tests
%{__python3} selftest.py

%files -n python3-%{modname}
%license lgpl.txt
%doc AUTHORS CHANGELOG NEWS README.txt
%{_bindir}/nosetests
%{_bindir}/nosetests-3
%{_bindir}/nosetests-%{python3_version}
%{_mandir}/man1/nosetests.1*
%{_mandir}/man1/nosetests-3.1*
%{_mandir}/man1/nosetests-%{python3_version}.1*
%{python3_sitelib}/nose-*.dist-info/
%{python3_sitelib}/nose/

%changelog
%autochangelog
