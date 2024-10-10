Name:           python-txredisapi
Version:        1.4.9
Release:        %autorelease
Summary:        Non-blocking Redis client for Python

License:        Apache-2.0
URL:            http://github.com/fiorix/txredisapi
Source0:        https://files.pythonhosted.org/packages/source/t/txredisapi/txredisapi-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
txredisapi is a non-blocking client driver for the Redis database,
written in Python. It uses Twisted for the asynchronous communication
with Redis.

It started as a fork of the original Redis protocol for Twisted, and
evolved into a more robust, reliable, and complete solution for
applications like web servers. These types of applications often need a
fault-tolerant pool of connections with multiple Redis servers, making it
possible to easily develop and maintain distributed systems.

Most of the Redis commands are supported, as well as other features such as
silent reconnection, connection pools, and automatic sharding.

This driver is distributed as part of the cyclone web framework.}

%description %{_description}

%package -n     python3-txredisapi
Summary:        %{summary}
Requires:       python3-six
Requires:       python3-twisted
%description -n python3-txredisapi %{_description}


%prep
%autosetup -n txredisapi-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files txredisapi


%files -n python3-txredisapi -f %{pyproject_files}


%changelog
%autochangelog
