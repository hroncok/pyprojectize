%global pypi_name torchtext
%global pypi_version 0.18.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Data loaders and abstractions for language processing, powered by PyTorch

%bcond_with test

# licensecheck reports
# Apache License 2.0
# ------------------
# text-0.16.0/torchtext/csrc/bert_tokenizer.cpp
#
# BSD 3-Clause License
# --------------------
# text-0.16.0/LICENSE
# This is the main license
#
# MIT License
# -----------
# text-0.16.0/run-clang-format.py
# This file is not distributed
License:        BSD-3-Clause AND Apache-2.0

URL:            https://github.com/pytorch/text
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/text-%{version}.tar.gz
# this is a tarball, not a git repo
Patch0:         0001-Prepare-torchtext-setup-for-fedora.patch
# We have removed the third_party dir
# so needs to be versioned
Patch1:         0001-Prepare-torchtext-cmake-for-Fedora.patch


# Limit to these because that is what torch is on
ExclusiveArch:  x86_64 aarch64
%global toolchain gcc

BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  re2-devel
BuildRequires:  sentencepiece-devel
BuildRequires:  utf8proc-devel

BuildRequires:  python3-devel
%if %{with test}
BuildRequires:  python3dist(expecttest)
BuildRequires:  python3dist(parameterized)
%endif
BuildRequires:  python3dist(nltk)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(tqdm)

%description
torchtext is a complementary python package to torch, providing torch
with text processing functionality needed for AI.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
torchtext is a complementary python package to torch, providing torch
with text processing functionality needed for AI.

%prep
%autosetup -p1 -n text-%{version}

rm -rf third_party/*

%generate_buildrequires
%pyproject_buildrequires

%build
# Building uses python3_sitearch/torch/utils/cpp_extension.py
# cpp_extension.py does a general linking with all the pytorch libs which
# leads warnings being reported by rpmlint.
%pyproject_wheel

%if %{with test}
%check
%pytest -sv
%endif

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}.dist-info/

%changelog
%autochangelog

