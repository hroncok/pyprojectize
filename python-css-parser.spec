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
# for tests
BuildRequires:  python3-chardet

%global _description %{expand:
A fork of the cssutils project based on version 1.0.2. This fork includes
general bug fixes and extensions specific to editing and working with ebooks.}

%description %_description

%package -n python3-css-parser
Summary:        %{summary}

%description -n python3-css-parser %_description

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
sed -r -i '1{/.usr.bin.env python/d;}' src/css_parser/*py src/css_parser/*/*py

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files css_parser

%check
%python3 run_tests.py

%files -n python3-css-parser -f %{pyproject_files}
%doc README.md
%license COPYING COPYING.LESSER

%changelog
%autochangelog
