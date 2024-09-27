Summary:        Fast numerical array expression evaluator for Python and NumPy
Name:           python-numexpr
Version:        2.8.5
Release:        %autorelease
URL:            https://github.com/pydata/numexpr
License:        MIT
Source:         https://github.com/pydata/numexpr/archive/v%{version}/numexpr-%{version}.tar.gz
Patch:          0002-Revert-Make-more-difficult-sanitize-of-the-expressio.patch
Patch:          0003-Revert-Add-in-protections-against-call-to-eval-expre.patch
Patch:          0004-Revert-Adding-tests-for-validate-and-noticed-that-re.patch
Patch:          0005-Revert-Add-in-docstring-intro-for-validate.patch
Patch:          0006-Revert-Add-a-validate-.-function-that-can-be-used-to.patch
Patch:          0007-Use-r-to-avoid-warning-about-unknown-escapes.patch
# https://github.com/pydata/numexpr/pull/489
Patch:          0008-Fix-necompiler.getArguments-on-Python-3.13.0b1.patch

BuildRequires:  gcc-c++
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy

%global _description %{expand:
The numexpr package evaluates multiple-operator array expressions many times
faster than NumPy can. It accepts the expression as a string, analyzes it,
rewrites it more efficiently, and compiles it to faster Python code on the
fly. It’s the next best thing to writing the expression in C and compiling it
with a specialized just-in-time (JIT) compiler, i.e. it does not require a
compiler at runtime.}

%description %_description

%package -n python%{python3_pkgversion}-numexpr
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-numpy >= 1.6
%{?python_provide:%python_provide python%{python3_pkgversion}-numexpr}

%description -n python%{python3_pkgversion}-numexpr %_description

%prep
%autosetup -n numexpr-%{version} -p1

# Python 3.13+ has removed unittest.makeSuite()
# Reported upstream: https://github.com/pydata/numexpr/issues/486
sed -i 's/unittest.makeSuite/unittest.defaultTestLoader.loadTestsFromTestCase/g' $(grep -rl makeSuite)

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
chmod 0755 %{buildroot}%{python3_sitearch}/numexpr/cpuinfo.py
sed -i "1s|/usr/bin/env python$|%{python3}|" %{buildroot}%{python3_sitearch}/numexpr/cpuinfo.py

%check
pushd build/lib.linux*
%py3_test_envvars %python3 -c 'import numexpr, sys; sys.exit(not numexpr.test().wasSuccessful())'
popd

%files -n python%{python3_pkgversion}-numexpr
%license LICENSE.txt
%doc ANNOUNCE.rst RELEASE_NOTES.rst README.rst
%{python3_sitearch}/numexpr/
%{python3_sitearch}/numexpr-%{version}.dist-info

%changelog
%autochangelog
