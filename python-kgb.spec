Name:           python-kgb
Version:        7.1.1
Release:        8%{?dist}
Summary:        Intercept and record calls to functions
License:        MIT
URL:            https://github.com/beanbaginc/kgb
Source0:        %{pypi_source kgb}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# required for tests
BuildRequires:  python3-pytest


%global _description %{expand:
Ever deal with a large test suite before, monkey patching functions to figure
out whether it was called as expected? It’s a dirty job. If you’re not careful,
you can make a mess of things. Leave behind evidence.

kgb’s spies will take care of that little problem for you.

What are spies? Spies intercept and record calls to functions. They can report
on how many times a function was called and with what arguments. They can allow
the function call to go through as normal, to block it, or to reroute it to
another function.

Spies are awesome.

(If you’ve used Jasmine, you know this.)

Spies are like mocks, but better. You’re not mocking the world. You’re
replacing very specific function logic, or listening to functions without
altering them.}

%description %_description

%package -n python3-kgb
Summary:        %{summary}


%description -n python3-kgb %_description


%package -n python3-kgb-tests
Summary:        Unit tests for python3-kgb
Requires:       python3-kgb = %{version}-%{release}


%description -n python3-kgb-tests
Unit tests for python3-kgb


%prep
%autosetup -p1 -n kgb-%{version}

%if !0%{?el8}
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?el8}
%py3_build
%else
%pyproject_wheel
%endif


%install
%if 0%{?el8}
%py3_install
%else
%pyproject_install
%endif

%check
%pytest --pyargs kgb

%files -n  python3-kgb
%license LICENSE
%doc README.rst NEWS.rst AUTHORS
%{python3_sitelib}/kgb/
%exclude %{python3_sitelib}/kgb/tests/
%if 0%{?el8}
%{python3_sitelib}/kgb-%{version}-py*.egg-info/
%else
%{python3_sitelib}/kgb-%{version}.dist-info/
%endif

%files -n python3-kgb-tests
%{python3_sitelib}/kgb/tests/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 7.1.1-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 7.1.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 06 2022 Jonathan Wright <jonathan@almalinux.org> - 7.1.1-1
- Initial package build
- rhbz#2114603
