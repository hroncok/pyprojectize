# Polyfill %%bcond() macro for platforms without it
%if 0%{!?bcond:1}
%define bcond() %[ (%2)\
    ? "%{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}"\
    : "%{expand:%%{?_with_%{1}:%%global with_%{1} 1}}"\
]
%endif

# Set this to 1 when bootstrapping
%bcond bootstrap 0

%bcond tests 1

# While bootstrapping, ignore manpages
%bcond manpages %{without bootstrap}

# The pytest-xdist package is not available when bootstrapping or on RHEL
%bcond xdist %[%{without bootstrap} && %{undefined rhel}]

# Package the placeholder rpm-macros (moved to redhat-rpm-config in F40)
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
%bcond rpmmacropkg 1
%else
%bcond rpmmacropkg 0
%endif

%if %{with bootstrap}
%bcond poetry 0
%else
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} || 0%{?epel} >= 9
%bcond poetry 1
# Appease old Poetry versions (<1.2.0a2)
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 38 || 0%{?rhel} >= 10
%bcond old_poetry 0
%else
%bcond old_poetry 1
%endif
%else
%bcond poetry 0
%endif
%endif

%global srcname rpmautospec

Name: python-%{srcname}
Version: 0.7.2

%if %{with bootstrap}
Release: 0%{?dist}
%else
Release: %autorelease
%endif
Summary: Package and CLI tool to generate release fields and changelogs
License: MIT
URL: https://github.com/fedora-infra/%{srcname}
Source0: https://github.com/fedora-infra/%{srcname}/releases/download/%{version}/%{srcname}-%{version}.tar.gz

%if 0%{!?pyproject_files:1}
%global pyproject_files %{_builddir}/%{name}-%{version}-%{release}.%{_arch}-pyproject-files
%endif

BuildArch: noarch
BuildRequires: git
# the langpacks are needed for tests
BuildRequires: glibc-langpack-de
BuildRequires: glibc-langpack-en
BuildRequires: python3-devel >= 3.9.0
# Needed to build man pages
%if %{with manpages}
BuildRequires: python3dist(click-man)
%endif

%if %{with tests}
# The dependencies needed for testing don’t get auto-generated.
BuildRequires: python3dist(pytest)
%if %{with xdist}
BuildRequires: python3dist(pytest-xdist)
%endif
%endif

BuildRequires: python3dist(pyyaml)
BuildRequires: sed

%if %{without poetry}
BuildRequires: python3dist(babel)
BuildRequires: python3dist(click)
BuildRequires: python3dist(click-plugins)
BuildRequires: python3dist(pygit2)
BuildRequires: python3dist(rpm)
BuildRequires: python3dist(rpmautospec-core)
%py_provides   python3-%{srcname}
%endif

%global _description %{expand:
A package and CLI tool to generate RPM release fields and changelogs.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname} %_description

%package -n %{srcname}
Summary:  CLI tool for generating RPM releases and changelogs
Requires: python3-%{srcname} = %{version}-%{release}

%description -n %{srcname}
CLI tool for generating RPM releases and changelogs

%if %{with rpmmacropkg}
%package -n rpmautospec-rpm-macros
Summary: Rpmautospec RPM macros for local rpmbuild
Requires: rpm

%description -n rpmautospec-rpm-macros
This package contains RPM macros with placeholders for building rpmautospec
enabled packages locally.
%endif

%generate_buildrequires
%if %{with poetry}
%pyproject_buildrequires
%endif

%prep
%autosetup -n %{srcname}-%{version}
%if %{without poetry}
sed -i -e 's/\[project\]/#\&/g' pyproject.toml
%endif
%if %{with old_poetry}
sed -i \
    -e 's/\[tool\.poetry\.group\.dev\.dependencies\]/[tool.poetry.dev-dependencies]/g' \
    pyproject.toml
%endif

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i -e '/pytest-cov/d; /addopts.*--cov/d' pyproject.toml

%build
%if %{with poetry}
%pyproject_wheel
%else
%py3_build
%endif

%install
%if %{with poetry}
%pyproject_install
%pyproject_save_files %{srcname}
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}
%else
%py3_install
cat << EOF > %{pyproject_files}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/*.egg-info/
EOF
%endif

%if %{with manpages}
# Man pages
PYTHONPATH=%{buildroot}%{python3_sitelib} click-man rpmautospec
install -m755 -d %{buildroot}%{_mandir}/man1
install -m644 man/*.1 %{buildroot}%{_mandir}/man1
%endif

# RPM macros
%if %{with rpmmacropkg}
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644 rpm/macros.d/macros.rpmautospec %{buildroot}%{rpmmacrodir}/
%endif

# Shell completion
for shell_path in \
        bash:%{bash_completions_dir}/rpmautospec \
        fish:%{fish_completions_dir}/rpmautospec.fish \
        zsh:%{zsh_completions_dir}/_rpmautospec; do
    shell="${shell_path%%:*}"
    path="${shell_path#*:}"
    dir="${path%/*}"

    install -m 755 -d "%{buildroot}${dir}"

    PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _RPMAUTOSPEC_COMPLETE="${shell}_source" \
    %{__python3} -c \
    "import sys; sys.argv[0] = 'rpmautospec'; from rpmautospec.cli import cli; sys.exit(cli())" \
    > "%{buildroot}${path}"
done

%check
# Always run the import checks, even when other tests are disabled
%if %{with poetry}
%pyproject_check_import
%else
%py3_check_import rpmautospec rpmautospec.cli
%endif

%if %{with tests}
%pytest -v \
%if %{with xdist}
--numprocesses=auto
%endif
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files -n %{srcname}
%{_bindir}/rpmautospec
%if %{with manpages}
%{_mandir}/man1/rpmautospec*.1*
%endif
%dir %{bash_completions_dir}
%{bash_completions_dir}/rpmautospec
%dir %{fish_completions_dir}
%{fish_completions_dir}/rpmautospec.fish
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_rpmautospec

%if %{with rpmmacropkg}
%files -n rpmautospec-rpm-macros
%{rpmmacrodir}/macros.rpmautospec
%endif

%changelog
%{?autochangelog}
