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

Requires:       python3dist(setuptools)

%description -n python3-%{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.


%prep
%autosetup -n %{srcname}-%{version}


# Fix shebang
sed -i -e '/^#!\//, 1d' %{srcname}/__main__.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import


%files -n %{srcname}
%{_bindir}/glad

%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
%autochangelog
