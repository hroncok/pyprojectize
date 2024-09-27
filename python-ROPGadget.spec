%global srcname ROPGadget

Name:           python-%{srcname}
Version:        7.4
Release:        %autorelease
Summary:        A tool to find ROP gadgets in program files

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/R/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/JonathanSalwan/ROPgadget/c29c50773ec7fb3df56396ce27fb71c3898c53ae/LICENSE_BSD.txt
Source2:        https://raw.githubusercontent.com/JonathanSalwan/ROPgadget/c29c50773ec7fb3df56396ce27fb71c3898c53ae/README.md

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist capstone}
BuildRequires:  %{py3_dist setuptools}

%description
ROPGadget lets you search your gadgets on your binaries to facilitate
your ROP exploitation. ROPgadget supports ELF, PE and Mach-O format on
x86, x64, ARM, ARM64, PowerPC, SPARC and MIPS architectures.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       %{py3_dist capstone}

%description -n python3-%{srcname}
ROPGadget lets you search your gadgets on your binaries to facilitate
your ROP exploitation. ROPgadget supports ELF, PE and Mach-O format on
x86, x64, ARM, ARM64, PowerPC, SPARC and MIPS architectures.

%prep
%autosetup -n %{srcname}-%{version}

# Requires capstone that is not yet released. Be less selective.
sed -i 's/>=5.0.0rc2//g' setup.py

cp -p %SOURCE1 .
cp -p %SOURCE2 .

%build
%py3_build

%install
%py3_install
for lib in $(find %{buildroot}%{python3_sitelib}/ropgadget/ -name "*.py"); do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done

%files -n python3-%{srcname}
%doc LICENSE_BSD.txt README.md
%{python3_sitelib}/ropgadget
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{_bindir}/*

%changelog
%autochangelog
