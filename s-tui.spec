%global sys_name s_tui

Name:       s-tui
Version:    1.1.6
Release:    %autorelease
Summary:    Terminal-based CPU stress and monitoring utility
BuildArch:  noarch

License:    GPL-2.0-or-later
URL:        https://github.com/amanusk/s-tui
Source0:    %{pypi_source}

BuildRequires: python3-devel

Recommends: stress-ng

%description
Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power and
utilization in a graphical way from the terminal.

What it does

  * Monitoring your CPU temperature/utilization/frequency/power
  * Shows performance dips caused by thermal throttling
  * Requires no X-server
  * Built in options for stressing the CPU (stress/stress-ng/FIRESTARTER)


%prep
%autosetup

# Remove bundled egg-info
rm -rf %{name}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{sys_name}

# Remove shebang from Python libraries
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,sources,sturwid}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,sources,sturwid}/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
