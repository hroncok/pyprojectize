Name:		sentencepiece
Version:	0.1.99
Release:	%autorelease
Summary:	An unsupervised text tokenizer for Neural Network-based text generation

License:	Apache-2.0
URL:		https://github.com/google/sentencepiece
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/google/sentencepiece/issues/860
ExcludeArch:    s390x

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	gperftools-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%description
The SentencePiece is an unsupervised text tokenizer for Neural Network-based
text generation.
It is an unsupervised text tokenizer and detokenizer mainly for
Neural Network-based text generation systems where the vocabulary size is
predetermined prior to the neural model training.
SentencePiece implements subword units and unigram language model with the
extension of direct training from raw sentences.
SentencePiece allows us to make a purely end-to-end system that does not
depend on language-specific pre/post-processing.

%package libs
Summary:	Runtime libraries for SentencePiece

%description libs
This package contains the libraries for SentencePiece.

%package tools
Summary:	Tools for SentencePiece
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tools
This package contains tools for manipulate models for SentencePiece.

%package devel
Summary:	Libraries and header files for SentencePiece
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains header files to develop a software using SentencePiece.

%package        -n python3-%{name}
Summary:	Python module for SentencePiece
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package contains Python3 module file for SentencePiece.

%prep
%autosetup

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \

%cmake_build

pushd python
CFLAGS="-I../src" LDFLAGS="-L../%{_vpath_builddir}/src -lsentencepiece" PKG_CONFIG_PATH="../%{_vpath_builddir}" %py3_build
popd

%install
%cmake_install

pushd python
%py3_install
popd

rm %{buildroot}%{_libdir}/libsentencepiece*.a

%files libs
%doc README.md
%license LICENSE
%{_libdir}/libsentencepiece*.so.0*

%files devel
%{_includedir}/sentencepiece*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/sentencepiece*.pc

%files tools
%{_bindir}/spm*

%files -n python3-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-*.egg-info/


%changelog
%autochangelog
