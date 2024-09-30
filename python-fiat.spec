Name:           python-fiat
Version:        2019.1.0
Release:        %autorelease
Summary:        Generator of arbitrary order instances of Lagrange elements on lines, triangles, and tetrahedra
%global data_version 83d6c1d8f30d

Source0:        https://bitbucket.org/fenics-project/fiat/downloads/fiat-%{version}.tar.gz
Source1:        https://bitbucket.org/fenics-project/fiat/downloads/fiat-%{version}.tar.gz.asc
Source2:        https://bitbucket.org/fenics-project/fiat-reference-data/get/%{data_version}.zip#/fiat-reference-data-%{data_version}.zip

Patch0001:      https://bitbucket.org/fenics-project/fiat/commits/852a15f1a21e360cde3bc8b53693dc933712806e/raw#/patch0001.patch
Patch0002:      https://bitbucket.org/fenics-project/fiat/commits/b8e9c1e64264bd2a0276db483ab300f7c16bf8e2/raw#/patch0002.patch
Patch0004:      https://bitbucket.org/fenics-project/fiat/commits/3b17d82a5678746234247bad3b9c019f49bc00ad/raw#/patch0004.patch
Patch0005:      https://bitbucket.org/fenics-project/fiat/commits/1d0f416f3b3093ccf72ff8cc65a56a213abbbd43/raw#/patch0005.patch

License:        LGPL-3.0-or-later
URL:            https://bitbucket.org/fenics-project/fiat
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cases)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(sympy)
BuildRequires:  /usr/bin/unzip

%global _description %{expand:
The FInite element Automatic Tabulator FIAT supports generation of
arbitrary order instances of the Lagrange elements on lines,
triangles, and tetrahedra. It is also capable of generating arbitrary
order instances of Jacobi-type quadrature rules on the same element
shapes. Further, H(div) and H(curl) conforming finite element spaces
such as the families of Raviart-Thomas, Brezzi-Douglas-Marini and
Nedelec are supported on triangles and tetrahedra. Upcoming versions
will also support Hermite and nonconforming elements.

FIAT is part of the FEniCS Project.}

%description %_description

%package -n python3-fiat
Summary: %summary
%{?python_provides python3-fiat}

%description -n python3-fiat %_description

%prep
%autosetup -n fiat-%{version} -p1

(
  cd test/regression
  unzip %{SOURCE2}
  ln -s fenics-project-fiat-reference-data-%{data_version} fiat-reference-data
)

sed -r -i 's/np[.]float/float/g' test/unit/test_discontinuous_taylor.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files FIAT

%check
%__python3 -m pytest -v test/ --skip-download

%files -n python3-fiat -f %{pyproject_files}
%license COPYING
%license COPYING.LESSER
%doc README.rst
%doc AUTHORS

%changelog
%autochangelog
