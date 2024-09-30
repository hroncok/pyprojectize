%global upstream_name openslide-python

Name:           python-openslide
Version:        1.3.1
Release:        %autorelease
Summary:        Python bindings for the OpenSlide library

License:        LGPL-2.1-only
URL:            https://openslide.org/
Source0:        https://github.com/openslide/%{upstream_name}/releases/download/v%{version}/%{upstream_name}-%{version}.tar.xz

# Disable Intersphinx so it won't download inventories at build time
Patch0:         openslide-python-1.0.1-disable-intersphinx.patch

BuildRequires:  gcc
BuildRequires:  openslide
BuildRequires:  python3-devel
BuildRequires:  python3-pillow
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx

%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.  This package allows Python
programs to use OpenSlide.


%package -n python3-openslide
Summary:        Python 3 bindings for the OpenSlide library
Requires:       openslide
Requires:       python3-pillow


%description -n python3-openslide
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.  This package allows Python 3
programs to use OpenSlide.


%prep
%autosetup -n %{upstream_name}-%{version} -p1

# Examples include bundled jQuery and OpenSeadragon
rm -rf examples


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
sphinx-build doc build/html
rm -r build/html/.buildinfo build/html/.doctrees


%install
%pyproject_install


%check
%if 0%{?rhel} == 9
# pytest 6; no support for pythonpath setting
sed -i -e '/^minversion/ d' pytest.ini
%pytest --import-mode append
%elif 0%{?rhel} != 8
%pytest
%endif


%files -n python3-openslide
%doc CHANGELOG.md build/html
%license COPYING.LESSER
%{python3_sitearch}/openslide/
%{python3_sitearch}/*.dist-info/


%changelog
%autochangelog
