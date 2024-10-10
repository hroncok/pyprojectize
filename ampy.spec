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

Provides:       adafruit-%{name} = %{version}-%{release}
%py_provides    python3-adafruit-%{name}


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


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{name}


%check
%{__python3} -m unittest tests/test_*.py -v


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
