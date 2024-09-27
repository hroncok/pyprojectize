Name:           python-css-parser
Version:        1.0.10
Release:        %autorelease
Summary:        Parse and build Cascading Style Sheets

%global forgeurl https://github.com/ebook-utils/css-parser
%forgemeta

License:        LGPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# for tests
BuildRequires:  python3-chardet

%global _description %{expand:
A fork of the cssutils project based on version 1.0.2. This fork includes
general bug fixes and extensions specific to editing and working with ebooks.}

%description %_description

%package -n python3-css-parser
Summary:        %{summary}
%{?python_provide:%python_provide python3-css-parser}

%description -n python3-css-parser %_description

%prep
%forgeautosetup -p1

%build
sed -r -i '1{/.usr.bin.env python/d;}' src/css_parser/*py src/css_parser/*/*py

%py3_build

%install
%py3_install

%check
%python3 run_tests.py

%files -n python3-css-parser
%{python3_sitelib}/css_parser/
%{python3_sitelib}/css_parser-%{version}-py%{python3_version}.egg-info/
%doc README.md
%license COPYING COPYING.LESSER

%changelog
%autochangelog
