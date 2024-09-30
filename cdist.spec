# Do not generate requires for scripts that might not be executed locally.
%global __requires_exclude_from ^%{python3_sitelib}/%{name}/conf

# Some scripts are executed on (non-Fedora) remote host. Do not play with shebangs too much!
%undefine __brp_mangle_shebangs

Name:		cdist
Version:	7.0.0
Release:	%autorelease
Summary:	Usable configuration management
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://www.cdi.st/
Source0:	%pypi_source

# Quick fix around argument parsing, which probably (?) blew up with python
# 3.11.
# TODO: investigate/report upstream.
Patch:	fix-argparse-scan.patch

BuildArch:	noarch
BuildRequires:	sed
BuildRequires:	findutils
BuildRequires:	grep
BuildRequires:	python3-devel
Requires:	bash
Requires:	openssh-clients
Recommends:	python3-scapy

%description
cdist is a usable configuration management system. It adheres to the KISS
principle and is being used in small up to enterprise grade environments. cdist
is an alternative to other configuration management systems.

%prep
%autosetup -p 1 -n %{name}-%{version}

# Remove shebang on non-executable python files.
find . -type f -exec sed -i 's/^#!\/usr\/bin\/env python/#!\/usr\/bin\/python/' {} +

# Assume unverisoned python is python3.
find . -type f -exec sed -i 's/^#!\/usr\/bin\/python$/#!\/usr\/bin\/python3/' {} +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

# Restore executable bit on scripts (remove by `python setup.py ...`).
(cd %{buildroot}; grep -l -R -m 1 "^#!\/" . | xargs  chmod +x)

mkdir -p %{buildroot}%{_mandir}/man1/ %{buildroot}%{_mandir}/man7/
cp docs/dist/man/man1/*.1 %{buildroot}%{_mandir}/man1/
cp docs/dist/man/man7/*.7 %{buildroot}%{_mandir}/man7/

%files -f %{pyproject_files}
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-*.1*
%{_mandir}/man7/%{name}-*.7*

%package doc
Summary: Documentation for the cdist configuration management tool

%description doc
HTML documentation for the cdist configuration management tool.

%files doc
%doc docs/dist/html

%changelog
%autochangelog
