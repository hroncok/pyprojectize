### Abstract ###
%bcond tests %{undefined rhel}

# global prerelease b4

%global openldap_version 2.4.45-4
%global pypi_name python-ldap

Name: python-ldap
Version: 3.4.4
Release: %autorelease
License: python-ldap
Summary: An object-oriented API to access LDAP directory servers
URL: https://python-ldap.org/
Source0: %{pypi_source}


### Build Dependencies ###
BuildRequires: gcc
BuildRequires: openldap-devel >= %{openldap_version}
BuildRequires: openssl-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: python3-devel
# Test dependencies
%if %{with tests}
BuildRequires: openldap-servers >= %{openldap_version}
BuildRequires: openldap-clients >= %{openldap_version}
%endif
BuildRequires: python3-pyasn1 >= 0.3.7
BuildRequires: python3-pyasn1-modules >= 0.1.5

%global _description\
python-ldap provides an object-oriented API for working with LDAP within\
Python programs.  It allows access to LDAP directory servers by wrapping the\
OpenLDAP 2.x libraries, and contains modules for other LDAP-related tasks\
(including processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%description %_description


%package -n     python3-ldap
Summary:        %{summary}

Requires:  openldap >= %{openldap_version}
Requires:  python3-pyasn1 >= 0.3.7
Requires:  python3-pyasn1-modules >= 0.1.5
Requires:  python3-setuptools
%{?python_provide:%python_provide python3-ldap}
Obsoletes: python3-pyldap < 3
Provides:  python3-pyldap = %{version}-%{release}
Provides:  python3-pyldap%{?_isa} = %{version}-%{release}

%description -n python3-ldap %_description


%prep
%autosetup -p1 -n %{name}-%{version}%{?prerelease}
# Fix interpreter
find . -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%check
%if %{with tests}
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest discover -v -s Tests -p 't_*'
%else
%py3_check_import ldap ldap.controls ldap.extop ldap.schema ldapurl ldif
%endif


%install
%pyproject_install

%files -n python3-ldap
%license LICENCE
%doc CHANGES README TODO Demo
%{python3_sitearch}/_ldap.cpython-*.so
%{python3_sitearch}/ldapurl.py*
%{python3_sitearch}/ldif.py*
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/slapdtest/
%{python3_sitearch}/ldap/
%{python3_sitearch}/python_ldap-%{version}%{?prerelease}.dist-info/

%changelog
%autochangelog
