Name:           python-pcodedmp
Summary:        VBA p-code disassembler
Version:        1.2.6
Release:        22%{?dist}
License:        GPL-3.0-or-later
URL:            https://github.com/bontchev/pcodedmp
VCS:            https://github.com/bontchev/pcodedmp
BuildArch:      noarch

%global srcname pcodedmp

# Bootstrap may be needed to break circular dependencies between
# python-pcodedmp and python-oletools
%bcond_with     bootstrap

# No python-pypandoc packages in EPEL 8 (yet?)
%if 0%{?fedora} || 0%{?rhel} == 7
%bcond_without  pypandoc
%else
%bcond_with     pypandoc
%endif

Source0:        %{pypi_source}
Patch0:         python-pcodedmp-1.2.6-python27.patch



%global _description %{expand:
Macros written in VBA (Visual Basic for Applications; the macro programming
language used in Microsoft Office) exist in three different executable forms,
each of which can be what is actually executed at run time, depending on the
circumstances: Source code, p-code and execodes.

Since most of the time it is the p-code that determines what exactly a macro
would do (even if neither source code, nor execodes are present), pcodedmp is
a Python library and command line tool to display it.}

%description %_description

%package -n pcodedmp
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-pcodedmp = %{version}-%{release}

%description -n pcodedmp %_description

%if 0%{?rhel} && 0%{?rhel} < 8
%package -n python2-pcodedmp
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with pypandoc}
BuildRequires:  python2-pypandoc
%endif
%if %{without bootstrap}
BuildRequires:  python2-oletools >= 0.54
Requires:       python2-oletools >= 0.54
%endif

%description -n python2-pcodedmp %_description
%endif

%package -n python%{python3_pkgversion}-pcodedmp
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with pypandoc}
BuildRequires:  python%{python3_pkgversion}-pypandoc
%endif
%if %{without bootstrap}
BuildRequires:  python%{python3_pkgversion}-lxml
BuildRequires:  python%{python3_pkgversion}-oletools >= 0.54
Requires:       python%{python3_pkgversion}-oletools >= 0.54
%endif

%description -n python%{python3_pkgversion}-pcodedmp %_description

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-pcodedmp
Summary:        %{summary}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%if %{with pypandoc}
BuildRequires:  python%{python3_other_pkgversion}-pypandoc
%endif
%if %{without bootstrap}
BuildRequires:  python%{python3_other_pkgversion}-lxml
BuildRequires:  python%{python3_other_pkgversion}-oletools >= 0.54
Requires:       python%{python3_other_pkgversion}-oletools >= 0.54
%endif

%description -n python%{python3_other_pkgversion}-pcodedmp %_description
%endif

%prep
%autosetup -n pcodedmp-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?rhel} && 0%{?rhel} < 8
%py2_build
%endif
%pyproject_wheel
%{?with_python3_other:%py3_other_build}

%install
%if 0%{?rhel} && 0%{?rhel} < 8
%py2_install
%endif
%pyproject_install
%{?with_python3_other:%py3_other_install}

# The check requires oletools, which might not be available during bootstrapping
%if %{without bootstrap}
%check
# There are no pytest tests defined at this moment
# %%pytest
# Do at least basic smoke test
%py3_check_import pcodedmp
%endif

%files -n pcodedmp
%{_bindir}/pcodedmp

%if 0%{?rhel} && 0%{?rhel} < 8
%files -n python2-pcodedmp
%license LICENSE
%doc README.md
%{python2_sitelib}/pcodedmp/
%{python2_sitelib}/pcodedmp-*.dist-info
%endif

%files -n python%{python3_pkgversion}-pcodedmp
%license LICENSE
%doc README.md
%{python3_sitelib}/pcodedmp/
%{python3_sitelib}/pcodedmp-*.dist-info/

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-pcodedmp
%license LICENSE
%doc README.md
%{python3_sitelib}/pcodedmp/
%{python3_sitelib}/pcodedmp-*.dist-info/
%endif

%changelog
%autochangelog