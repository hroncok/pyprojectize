%global modname rpyc

Name:           python-%{modname}
Version:        5.1.0
Release:        %autorelease
Summary:        Transparent, Symmetrical Python Library for Distributed-Computing

License:        MIT
URL:            http://rpyc.wikidot.com/
Source0:        https://github.com/tomerfiliba/rpyc/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

%global _description\
RPyC, or Remote Python Call, is a transparent and symmetrical python library\
for remote procedure calls, clustering and distributed-computing.\
RPyC makes use of object-proxies, a technique that employs python's dynamic\
nature, to overcome the physical boundaries between processes and computers,\
so that remote objects can be manipulated as if they were local.

%description %_description


%package -n python3-%{modname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Obsoletes:      python2-%{modname} < 4.0.1-4
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname} %_description

%prep
%setup -q -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install
# The binaries should not have .py extension
mv %{buildroot}%{_bindir}/rpyc_classic.py %{buildroot}%{_bindir}/rpyc_classic
mv %{buildroot}%{_bindir}/rpyc_registry.py %{buildroot}%{_bindir}/rpyc_registry

%files -n python3-%{modname}
%{_bindir}/rpyc_*
%{python3_sitelib}/rpyc*

%changelog
%autochangelog

