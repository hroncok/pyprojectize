%global srcname pynetbox
%global __python3 /usr/bin/python3.8
%global python3_pkgversion 38

Name:           python%{python3_pkgversion}-%{srcname}
Version:        6.6.2
Release:        %autorelease
Summary:        Python API client library for Netbox

License:        ASL 2.0
URL:            https://github.com/digitalocean/pynetbox
Source:         %{pypi_source}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info
sed -i -e "s/six==1\.\*/six>=1.0,<2.0/" setup.py
sed -i -e '/scm/d' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}.dist-info/

%changelog
%autochangelog
