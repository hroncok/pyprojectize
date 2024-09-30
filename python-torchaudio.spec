%global pypi_name torchaudio

%bcond_with gitcommit
%if %{with gitcommit}
# The release/2.3.0
%global commit0 17a70815259222570feb071034acd7bae2adc019
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240318
%global pypi_version 2.3.0
%else
%global pypi_version 2.4.1
%endif

%global desc %{expand: \
The aim of torchaudio is to apply PyTorch to the audio domain. By supporting
PyTorch, torchaudio follows the same philosophy of providing strong GPU
acceleration, having a focus on trainable features through the autograd
system, and having consistent style (tensor names and dimension names).
Therefore, it is primarily a machine learning library and not a general
signal processing library. The benefits of PyTorch can be seen in torchaudio
through having all the computations be through PyTorch operations which
makes it easy to use and feel like a natural extension. }

%ifarch x86_64
%if 0%{?fedora}
%bcond_without rocm
%else
%bcond_with rocm
%endif
%endif
# Which families gpu build for
%global rocm_gpu_list gfx9
%global rocm_default_gpu default
%bcond_without rocm_loop

# torch toolchain
%global toolchain gcc

Name:           python-%{pypi_name}
%if %{with gitcommit}
Version:        %{pypi_version}^git%{date0}.%{shortcommit0}
%else
Version:        %{pypi_version}
%endif
Release:        %autorelease
Summary:        Audio signal processing, powered by PyTorch

License:        BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 AND MIT
URL:            https://github.com/pytorch/audio
%if %{with gitcommit}
Source0:        %{url}/archive/%{commit0}/audio-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/audio-v%{version}.tar.gz
%endif

# Limit to these because that is what torch is on
ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ffmpeg-free
BuildRequires:  ffmpeg-free-devel
BuildRequires:  ninja-build
BuildRequires:  protobuf-devel
BuildRequires:  sox-devel

%if %{with rocm}
BuildRequires:  hipblas-devel
BuildRequires:  hipblaslt-devel
BuildRequires:  hipcub-devel
BuildRequires:  hipfft-devel
BuildRequires:  hiprand-devel
BuildRequires:  hipsparse-devel
BuildRequires:  hipsolver-devel
BuildRequires:  miopen-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocrand-devel
BuildRequires:  rocfft-devel
BuildRequires:  rocprim-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocthrust-devel
BuildRequires:  roctracer-devel
%endif

BuildRequires:  python3-devel
BuildRequires:  python3dist(torch)

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        Audio signal processing, powered by PyTorch

%description -n python3-%{pypi_name}
%{desc}

%if %{with rocm}
%package -n python3-%{pypi_name}-rocm-gfx9
Summary:        %{name} for ROCm gfx9

%description -n python3-%{pypi_name}-rocm-gfx9
%{summary}

%endif

%prep
%if %{with gitcommit}
%autosetup -p1 -n audio-%{commit0}
%else
%autosetup -p1 -n audio-%{version}
%endif

rm -rf third_party/*

%generate_buildrequires
%pyproject_buildrequires

%build
# Building uses python3_sitearch/torch/utils/cpp_extension.py
# cpp_extension.py does a general linking with all the pytorch libs which
# leads warnings being reported by rpmlint.
#
# pyproject_wheel tries to use pypi's cmake, revert back to py3_build

export BUILD_SOX=OFF
export USE_FFMPEG=OFF
%if %{with rocm}
export USE_ROCM=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode

gpu=%{rocm_default_gpu}
module load rocm/$gpu
export PYTORCH_ROCM_ARCH=$ROCM_GPUS
%py3_build
mv build build-${gpu}
module purge

%if %{with rocm_loop}
for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    export PYTORCH_ROCM_ARCH=$ROCM_GPUS
    %py3_build
    mv build build-${gpu}
    module purge
done
%endif

%else

%py3_build

%endif

%install

%if %{with rocm}

export USE_ROCM=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode

gpu=%{rocm_default_gpu}
module load rocm/$gpu
export PYTORCH_ROCM_ARCH=$ROCM_GPUS
mv build-${gpu} build
%py3_install
mv build build-${gpu}
module purge

%if %{with rocm_loop}
for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    export PYTORCH_ROCM_ARCH=$ROCM_GPUS
    mv build-${gpu} build
    # need to customize the install location, so replace py3_install
    %{__python3} %{py_setup} %{?py_setup_args} install -O1 --skip-build --root %{buildroot} --prefix /usr/lib64/rocm/${gpu} %{?*}
    rm -rfv %{buildroot}/usr/lib/rocm/${gpu}/bin/__pycache__
    mv build build-${gpu}
    module purge
done
%endif

%else
%py3_install

%endif

# exec permission
for f in `find %{buildroot} -name '*.py'`; do
    if [ ! -x $f ]; then
        sed -i '1{\@^#!/usr/bin@d}' $f
    fi
done

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md 
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/torio
%{python3_sitearch}/%{pypi_name}-*.dist-info/

%if %{with rocm}
%files -n python3-%{pypi_name}-rocm-gfx9
%{_libdir}/rocm/gfx9/lib64/*

%endif

%changelog
%autochangelog
