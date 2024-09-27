%global srcname pylibmc
%global sum Memcached client for Python

Name:           python-%{srcname}
Version:        1.6.3
Release:        %autorelease
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://sendapatch.se/projects/pylibmc/
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

# https://github.com/lericson/pylibmc/pull/292
# Python 3.13 compat
Patch01:        292.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  libmemcached-devel
BuildRequires:  zlib-devel

%description
pylibmc is a client in Python for memcached. It is a wrapper
around TangentOrg‘s libmemcached library. The interface is
intentionally made as close to python-memcached as possible,
so that applications can drop-in replace it.


%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
pylibmc is a client in Python 3 for memcached. It is a wrapper
around TangentOrg‘s libmemcached library. The interface is
intentionally made as close to python-memcached as possible,
so that applications can drop-in replace it.


%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

# there is an asterisk in the name of the file,
# because sometimes the suffix of the architecture is added
chmod 755 $RPM_BUILD_ROOT%{python3_sitearch}/_pylibmc.cpython-%{python3_version_nodots}*.so

%files -n python3-%{srcname}
%doc docs/ LICENSE README.rst
%{python3_sitearch}/%{srcname}-%{version}*.egg-info
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/*.so


%changelog
%autochangelog
