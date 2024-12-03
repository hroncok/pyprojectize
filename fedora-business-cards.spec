%global forgeurl    https://pagure.io/fedora-business-cards/
Version:            2.3.0

%forgemeta

Name:               fedora-business-cards
Release:            %autorelease
Summary:            The Fedora business card generator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:            GPL-2.0-or-later
URL:                https://fedoraproject.org/wiki/Business_cards
Source:             %{forgesource}

BuildArch:          noarch
BuildRequires:      python3-devel
Requires:           python3-fedora fedora-logos
Requires:           inkscape ghostscript
Requires:           aajohan-comfortaa-fonts abattis-cantarell-fonts

%description
fedora-business-cards is a tool written in Python to generate business cards
for Fedora Project contributors.

%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fedora_business_cards

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README
%{_bindir}/%{name}


%changelog
%autochangelog
