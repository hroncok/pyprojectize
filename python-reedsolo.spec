%global srcname reedsolo
%global py_setup_args --cythonize

Name:           python-reedsolo
Version:        1.7.0
Release:        %autorelease
Summary:        Pure-Python Reed Solomon encoder/decoder
License:        Public Domain
URL:            https://github.com/tomerfiliba-org/reedsolomon
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
A pure-python universal errors-and-erasures Reed-Solomon Codec, based on the
wonderful tutorial at wikiversity, written by “Bobmath” and “LRQ3000”.}

%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%py_provides python3-c%{srcname}

%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -p1 -n reedsolomon-%{version}
# Remove shebang in non-script source
# https://github.com/tomerfiliba/reedsolomon/pull/31
sed -r -i '1{/^#!/d}' %{srcname}.py


%build
%py3_build


%install
%py3_install


%check
%pytest


%files -n  python3-%{srcname}
%license LICENSE
%doc changelog.txt README.rst
%pycached %{python3_sitearch}/%{srcname}.py
%{python3_sitearch}/c%{srcname}%{python3_ext_suffix}
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
%autochangelog
