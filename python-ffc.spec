Name:           python-ffc
Version:        2019.1.0.post0
%global fenics_version 2019.1
Release:        %autorelease
Summary:        Compiler for finite element variational forms

License:        LGPL-3.0-or-later
URL:            https://fenics-ffc.readthedocs.org/
Source0:        https://bitbucket.org/fenics-project/ffc/downloads/ffc-%{version}.tar.gz
Source1:        https://bitbucket.org/fenics-project/ffc/downloads/ffc-%{version}.tar.gz.asc
Source2:        3083BE4C722232E28AD0828CBED06106DD22BAB3.gpg

Patch0:         https://bitbucket.org/fenics-project/ffc/commits/8d80c72468282e35fd5476b42c5c03595cd38e99/raw#/8d80c72468282e35fd5476b42c5c03595cd38e99.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(fenics-fiat) >= %{fenics_version}
BuildRequires:  python3dist(fenics-ufl) >= %{fenics_version}
BuildRequires:  python3dist(fenics-dijitso) >= %{fenics_version}
BuildRequires:  cmake
BuildRequires:  gnupg2
# Note: a copy of gtest is bundled and used for tests during build. It
# could be unbundled, but I don't think this is worth the trouble in
# this case.

%global _description %{expand:
The FEniCS Form Compiler FFC is a compiler for finite element
variational forms, translating high-level mathematical descriptions of
variational forms into efficient low-level C++ code for finite element
assembly.}

%description %_description

%package -n python3-ffc
Summary: %summary
%{?python_provides python3-ffc}

%description -n python3-ffc %_description

%prep
%{?gpgverify:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}

%autosetup -n ffc-%{version} -p1

sed -r -i '1d' ffc/__main__.py ffc/main.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ffc

%check
OPTIONS=(
  # test_evaluate.py uses libs/ffc-factory, which is currently ignored
  --ignore=test/unit/ufc/finite_element/test_evaluate.py
)
%python3 -m pytest -v test/ "${OPTIONS[@]}"

%files -n python3-ffc -f %{pyproject_files}
%doc README.rst ChangeLog.rst AUTHORS
%doc demo
%{_bindir}/ffc
%{_bindir}/ffc-3
%{_mandir}/man1/ffc.1*

%changelog
%autochangelog
