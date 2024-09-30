Name:           systemd-coredump-python
Version:        3
Release:        %autorelease
Summary:        systemd-coredump helper to log Python exceptions

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/systemd/systemd-coredump-python
Source0:        https://github.com/systemd/systemd-coredump-python/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

BuildArch:      noarch

%global _description %{expand:
Python module which hooks into sys.excepthook to log backtraces in the journal.}

%description %_description

%package -n python3-systemd-coredump
Summary:        %{summary}
Conflicts:      systemd < 233

%description -n python3-systemd-coredump %_description

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files systemd_coredump_exception_handler

# %%check
# there are no useful checks, the stuff in tests/ is only useful for development so far

%files -n python3-systemd-coredump -f %{pyproject_files}
%license COPYING
%doc README
%{python3_sitelib}/systemd_coredump.pth

%changelog
%autochangelog
