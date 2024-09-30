%undefine __cmake_in_source_build
Name:           tlsh
Version:        4.11.2
Release:        %autorelease
Summary:        Fuzzy text matching library

License:        Apache-2.0
URL:            https://github.com/trendmicro/tlsh
Source0:        https://github.com/trendmicro/tlsh/archive/%{version}/tlsh-%{version}.tar.gz

# https://github.com/trendmicro/tlsh/pull/128
Patch:          0001-python-use-setuptools-instead-of-distutils.patch
Patch:          0002-python-drop-pointless-line-continuations.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

%global _description %{expand:
TLSH is a fuzzy matching library. Given a byte stream with a minimum length of
256 bytes (and a minimum amount of randomness), TLSH generates a hash value
which can be used for similarity comparisons.  Similar objects will have similar
hash values which allows for the detection of similar objects by comparing their
hash values.}

%description %_description

%package doc
Summary: Documentation for TLSH
BuildArch: noarch

%description doc
%{summary}.

%package -n python3-tlsh
Summary:        Python 3 interface for TLSH
Obsoletes: tlsh < 3.17.0
Obsoletes: tlsh-devel < 3.17.0

%description -n python3-tlsh %_description

This package contains the %{summary}.

%prep
%autosetup -p1
# I'm just loving cmake more every day
echo 'set(CMAKE_CXX_FLAGS "%{optflags} -fPIC")' | \
     tee -a src/CMakeLists.txt |\
     tee -a test/CMakeLists.txt |\
     tee -a utils/CMakeLists.txt

sed -r -i '/CMAKE_EXE_LINKER_FLAGS.*-static-libstdc/d' CMakeLists.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%cmake
%cmake_build
pushd py_ext
%pyproject_wheel
popd

%install
pushd py_ext
%pyproject_install
%pyproject_save_files -l '*'
popd

%global _docdir_fmt %{name}

%check
bin/simple_unittest
bin/timing_unittest
# just check if we get 0 for identical files, and non-zero for different files
bin/tlsh_unittest -c bin/tlsh_unittest -f bin/tlsh_unittest | grep -E '\b0\b'
bin/tlsh_unittest -c bin/tlsh_unittest -f bin/simple_unittest | grep -vE '\b0\b'

PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} \
        -c "import tlsh; print(tlsh.hash(open('LICENSE', 'rb').read()))"

%ldconfig_scriptlets

%files doc
%license LICENSE NOTICE.txt
%doc README.md
%doc TLSH_CTC_final.pdf
%doc TLSH_Introduction.pdf
%doc Attacking_LSH_and_Sim_Dig.pdf

%files -n python3-tlsh -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
