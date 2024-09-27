%global commit 5acbe50717a4f53a411310f03eb5f6ad13b3d1ea

Name:           python-sphinxcontrib-globalsubs
Version:        0.1.1
Release:        %autorelease
Summary:        Global substitutions defined in conf.py
License:        BSD-2-Clause
URL:            https://github.com/missinglinkelectronics/sphinxcontrib-globalsubs
%global forgeurl %{url}
%forgemeta
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This extension adds support for global substitutions to conf.py.
One of the main use cases are central abbreviation lists, but any valid
reST markup can be substituted.
}
%description %_description

%package -n python3-sphinxcontrib-globalsubs
Summary:        %{summary}

%description -n python3-sphinxcontrib-globalsubs %_description

%prep
%autosetup -p1 -n sphinxcontrib-globalsubs-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# %%check
# upstream has no testsuite

%files -n python3-sphinxcontrib-globalsubs
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/sphinxcontrib/*
%{python3_sitelib}/sphinxcontrib_globalsubs-%{version}.dist-info/
%exclude %{python3_sitelib}/sphinxcontrib_globalsubs-*.pth

%changelog
%autochangelog
