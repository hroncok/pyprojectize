Name:           legendary
Version:        0.20.34
Release:        %autorelease
Summary:        Free and open-source replacement for the Epic Games Launcher
BuildArch:      noarch

License:        GPL-3.0-or-later
URL:            https://github.com/derrod/legendary
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel >= 3.9
BuildRequires:  python3dist(requests)

Requires:       python3-requests

Recommends:     wine
Recommends:     wine-dxvk

%description
Legendary is an open-source game launcher that can download and install games
from the Epic Games Store on Linux and Windows. It's name as a tongue-in-cheek
play on tiers of item rarity in many MMORPGs.


%prep
%autosetup

# E: non-executable-script
for lib in %{name}/{*.py,downloader/*.py,lfs/*.py,models/*.py}; do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}


%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
