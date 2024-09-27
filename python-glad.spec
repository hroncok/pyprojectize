%global srcname glad

Name:           python-%{srcname}
Version:        0.1.36
Release:        %autorelease
Summary:        Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator

# Mostly MIT, Apache-2.0 for Khronos and EGL specifications/headers.
License:        MIT and Apache-2.0
URL:            https://github.com/Dav1dde/glad
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.


%package -n     %{srcname}
Summary:        %{summary}

Requires:       python3dist(glad)

%description -n %{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(setuptools)

%description -n python3-%{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Fix shebang
sed -i -e '/^#!\//, 1d' %{srcname}/__main__.py


%build
%py3_build


%install
%py3_install


%files -n %{srcname}
%{_bindir}/glad

%files -n python3-%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
%autochangelog
