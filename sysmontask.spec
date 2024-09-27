%global srcname SysMonTask
%global uuid com.github.camelneeraj.%{name}

Name: sysmontask
Version: 1.3.9
Release: %autorelease
Summary: Linux system monitor with the compactness and usefulness of WTM
BuildArch: noarch

# The entire source code is BSD except:
#  * LGPLv2+:   sysmontask/gi_composites.py
# Automatically converted from old format: BSD and LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+

URL: https://github.com/KrispyCamel4u/SysMonTask
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: python3-devel

Requires: gtk3
Requires: hicolor-icon-theme
Requires: libwnck3

# For Log Plot utility
Recommends: python3-matplotlib

%description
Linux system monitor with the compactness and usefulness of Windows Task
Manager to allow higher control and monitoring.


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

sed -i 's|/usr/bin/env python3|%{__python3}|' \
    %{buildroot}%{python3_sitelib}/%{name}/*.py

# E: non-executable-script
chmod +x %{buildroot}%{python3_sitelib}/%{name}/{disk,gpu,mem,%{name}}.py

# Remove duplicate LICENSE file
rm %{buildroot}%{_docdir}/%{name}/LICENSE


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc AUTHORS
%doc README.md
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{srcname}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{python3_sitelib}/%{name}.dist-info/
%{python3_sitelib}/%{name}/


%changelog
%autochangelog
