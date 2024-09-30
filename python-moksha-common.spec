%global modname moksha.common

Name:           python-moksha-common
Version:        1.2.5
Release:        %autorelease
Summary:        Common components for Moksha

# Automatically converted from old format: ASL 2.0 or MIT - review is highly recommended.
License:        Apache-2.0 OR LicenseRef-Callaway-MIT
URL:            https://pypi.io/project/moksha.common
Source0:        https://pypi.io/packages/source/m/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch


BuildRequires:  python3-devel
BuildRequires:  python3-nose

BuildRequires:  python3-decorator
BuildRequires:  python3-kitchen
BuildRequires:  python3-pytz
BuildRequires:  python3-six

# Its a whole different package now

%global _description\
Common components for Moksha.

%description %_description

%package -n python3-moksha-common
Summary:        Common components for Moksha

Requires:       python3-decorator
Requires:       python3-kitchen
Requires:       python3-pytz
Requires:       python3-six
# /usr/bin/moksha was moved from there:
Conflicts:      python2-moksha-common < 1.2.5-9

%description -n python3-moksha-common
Common components for Moksha.

%prep
%setup -q -n %{modname}-%{version}

# Remove namespace_packages from setup.py
sed -i "/namespace_packages/d" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files moksha

# Add __init__.py files to namespace packages not installed by setuptools
cp moksha/__init__.py %{buildroot}/%{python3_sitelib}/moksha/

%check
%{__python3} -m nose

%files -n python3-moksha-common -f %{pyproject_files}
%doc README COPYING AUTHORS
# The CLI tool.  :)
%{_bindir}/moksha


%changelog
%autochangelog
