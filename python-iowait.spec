%global modname iowait

Name:           python-%{modname}
Version:        0.2
Release:        %autorelease
Summary:        Platform-independent module for I/O completion events

License:        LGPL-3.0-or-later
URL:            https://pypi.python.org/pypi/iowait
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{modname}; echo ${n:0:1})/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Different operating systems provide different ways to wait for I/O completion\
events: there’s select(), poll(), epoll() and kqueue(). For cross-platform\
applications it can be a pain to support all this system functions, especially\
because each one provides a different interface.\
\
IOWait solves this problem by providing a unified interface and using always\
the best and faster function available in the platform. Its only limitation\
is that, on Windows, it only works for sockets.

%description %{_description}

%package -n python3-%{modname}

Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} test.py -v

%files -n python3-%{modname}
%license COPYING.LESSER
%doc README

%{python3_sitelib}/%{modname}-*.egg-info
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
%autochangelog
