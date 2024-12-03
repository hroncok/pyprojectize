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
Obsoletes:      python2-%{modname} < 4.0.1-4

%description -n python3-%{modname} %_description

%prep
%setup -q -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'rpyc*'
# The binaries should not have .py extension
mv %{buildroot}%{_bindir}/rpyc_classic.py %{buildroot}%{_bindir}/rpyc_classic
mv %{buildroot}%{_bindir}/rpyc_registry.py %{buildroot}%{_bindir}/rpyc_registry

%check
%pyproject_check_import

%files -n python3-%{modname} -f %{pyproject_files}
%{_bindir}/rpyc_*

%changelog
%autochangelog

