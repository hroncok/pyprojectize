# Created by pyp2rpm-3.2.2
Name:           ampy
Version:        1.0.5
Release:        %autorelease
Summary:        Command line tool to interact with a MicroPython board over a serial connection

License:        MIT
URL:            https://github.com/adafruit/ampy

# Use GitHub archive instead of PyPi sdist to have tests, README, LICENSE
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%?python_enable_dependency_generator

Provides:       adafruit-%{name} = %{version}-%{release}
Provides:       python3-adafruit-%{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-adafruit-%{name}}


%description
Adafruit MicroPython tool is a command line tool to interact with a MicroPython
board over a serial connection.

Ampy is meant to be a simple command line tool to manipulate files and run code
on a MicroPython board over its serial connection. With ampy you can send files
from your computer to a MicroPython board's file system, download files from a
board to your computer, and even send a Python script to a board to be
executed.

Note that ampy by design is meant to be simple and does not support advanced
interaction like a shell or terminal to send input to a board. 


%prep
%autosetup -n %{name}-%{version}

# shebangs
sed -i '1d' $(grep -lr '#!/usr/')


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m unittest tests/test_*.py -v


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/adafruit_ampy-%{version}-py%{python3_version}.egg-info


%changelog
%autochangelog
