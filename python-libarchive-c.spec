Name:          python-libarchive-c
Version:       5.1
Release:       %autorelease
Summary:       Python interface to libarchive
License:       CC0
URL:           https://github.com/Changaco/python-libarchive-c

%global forgeurl %{url}
%global tag %{version}
%forgemeta

Source0:       https://github.com/Changaco/python-libarchive-c/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: libarchive-devel
BuildArch:     noarch

%global _description %{expand:
The libarchive library provides a flexible interface for reading and
writing archives in various formats such as tar and cpio. libarchive
also supports reading and writing archives compressed using various
compression filters such as gzip and bzip2.

A Python interface to libarchive. It uses the standard ctypes module
to dynamically load and access the C library.}

%description %_description

%package -n python%{python3_pkgversion}-libarchive-c
Summary:       %{summary}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-pytest
Requires:      libarchive

%description -n python%{python3_pkgversion}-libarchive-c %_description

%prep
%autosetup -n %{name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'libarchive*'
%{_fixperms} %{buildroot}

%check
%{?el7:export LANG=en_US.UTF-8}
pytest-%{python3_version} -s -vv tests %{?el7:-k "not test_check_archiveentry_using_python_testtar"}

%global _docdir_fmt %{name}

%files -n python%{python3_pkgversion}-libarchive-c -f %{pyproject_files}
%doc README.rst
%license LICENSE.md

%changelog
%autochangelog
