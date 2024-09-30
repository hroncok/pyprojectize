%global srcname tftpy

Name:		python-%{srcname}
Version:	0.8.2
Release:	%autorelease
Summary:	TFTPy is a pure Python implementation of the Trivial FTP protocol
License:	MIT
URL:		https://github.com/msoulier/%{srcname}
Source0:	%{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:	noarch

%global _description\
Tftpy is a TFTP library for the Python programming language. It includes\
client and server classes, with sample implementations. Hooks are included\
for easy inclusion in a UI for populating progress indicators. It supports\
RFCs 1350, 2347, 2348 and the tsize option from RFC 2349.\

%description %_description

%package -n python3-%{srcname}
Summary: %summary

BuildRequires:	python3-devel
Conflicts:	python2-%{srcname} <= 0.8.0-1

%description -n python3-%{srcname} %_description


%prep
%setup -q -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%files -n python3-%{srcname}
%doc README
%{_bindir}/tftpy_client.py
%{_bindir}/tftpy_server.py
%{python3_sitelib}/tftpy/
%{python3_sitelib}/*.dist-info


%changelog
%autochangelog
