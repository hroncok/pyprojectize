Name:           uflash
Version:        2.0.0
Release:        %autorelease
Summary:        A module and utility to flash Python onto the BBC micro:bit
License:        MIT
URL:            https://github.com/ntoll/uflash
Source0:        %pypi_source

# For tests, they don't have tags
%define hash    147ea945fbe841b0ae17888ab60a60c6080b1225
Source1:        https://github.com/ntoll/uflash/archive/%{hash}.tar.gz
BuildRequires:  python3-pytest

BuildRequires:  python3-devel
BuildRequires:  python3-nudatus

Requires:       python3-setuptools
Recommends:     python3-nudatus

BuildArch:      noarch

# Other tools are using this as a module, so provide also the python3- name
Provides:       python3-%{name} == %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description
A utility for flashing the BBC micro:bit with Python scripts and the
MicroPython runtime. You pronounce the name of this utility "micro-flash". ;-)
It provides two services. A library of functions to programatically create a
hex file and flash it onto a BBC micro:bit.  A command line utility called
uflash that will flash Python scripts onto a BBC micro:bit.


%prep
%setup -q


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install

%check
tar -xf %{SOURCE1}
mv %{name}-%{hash}/tests .
rm -rf %{name}-%{hash}

py.test-3 -vv

%files
%doc README.rst CHANGES.rst
%license LICENSE
%{_bindir}/uflash
%{_bindir}/py2hex
%{python3_sitelib}/uflash*
%{python3_sitelib}/__pycache__/uflash*



%changelog
%autochangelog
