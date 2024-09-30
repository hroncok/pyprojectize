## https://github.com/prody/ProDy/issues/266
ExcludeArch: ppc64 s390x

# Tests need internet connection;
# correctly executed in local.
%global with_check 0

##  Filtering of private libraries 
%global _privatelibs  ^%{python3_sitearch}/prody/.*\\.so$
%global __provides_exclude_from ^(%{_privatelibs})$
%global __requires_exclude_from ^(%{_privatelibs})$

Name: ProDy
Summary: Application for protein structure, dynamics and sequence analysis
Version: 2.4.1
Release: %autorelease

# MIT is the main license for ProDy
# prody/utilities/tnt/* code --> 'Public domain' license
# CEalign module is distributed under BSD license
# Automatically converted from old format: MIT and Public domain and BSD - review is highly recommended.
License: Warning: we do not have SPDX identifier for Public domain
URL: http://www.csb.pitt.edu/ProDy
Source0: https://github.com/prody/ProDy/archive/v%{version}/ProDy-%{version}.tar.gz

BuildRequires: gcc, gcc-c++

Patch0: ProDy-change_requires.patch

%description
ProDy is a free and open-source Python package for protein structure, dynamics,
and sequence analysis.  It allows for comparative analysis and modeling of 
protein structural dynamics and sequence co-evolution.  Fast and flexible ProDy
API is for interactive usage as well as application development.  ProDy also  
comes with several analysis applications and a graphical user interface for 
visual analysis. 
- Visit http://www.csb.pitt.edu/ProDy/ -

%package -n python3-%{name}
Summary: Application for protein structure, dynamics and sequence analysis
Provides: ProDy = 0:%{version}-%{release}

BuildRequires: python3-devel
BuildRequires: python3-nose
BuildRequires: python3-urllib3
BuildRequires: python3-scipy
BuildRequires: python3-numpy >= 1:1.10.0
BuildRequires: python3-matplotlib
BuildRequires: python3-biopython

Requires: python3-scipy
Requires: python3-biopython
Requires: python3-ipython
Requires: python3-pyparsing
Requires: python3-numpy

## Explicit library require for using plotting functions
Requires: python3-matplotlib

%description -n python3-%{name}
This is ProDy Python3 package for protein structure, dynamics,
and sequence analysis.  It allows for comparative analysis and modeling of 
protein structural dynamics and sequence co-evolution.  Fast and flexible ProDy
API is for interactive usage as well as application development.  ProDy also  
comes with several analysis applications and a graphical user interface for 
visual analysis. 
- Visit http://www.csb.pitt.edu/ProDy/ -

%prep
%autosetup -p1

# Fix permissions
find prody/proteins/ccealign -name '*.h' -exec chmod 0644 '{}' \;
find prody/proteins/ccealign -name '*.cpp' -exec chmod 0644 '{}' \;

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

mkdir -p $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_bindir}/*

cd scripts
cp -pr ./prody ./python%{python3_version}-prody
cp -pr ./evol  ./python%{python3_version}-evol
# Fix shebangs
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' \
 ./prody \
 ./evol \
 ./python%{python3_version}-prody \
 ./python%{python3_version}-evol

for i in prody-%{python3_version}; do
  touch -r ./python%{python3_version}-prody $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  install -p ./prody $RPM_BUILD_ROOT%{_bindir}
  install -p ./python%{python3_version}-prody $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python3_version}-prody $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in evol-%{python3_version}; do
  touch -r ./python%{python3_version}-evol $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  install -p ./evol $RPM_BUILD_ROOT%{_bindir}
  install -p ./python%{python3_version}-evol $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python3_version}-evol $RPM_BUILD_ROOT%{_bindir}/$i
done
cd ..

%if 0%{?with_check}
%check
pushd scripts
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} nosetests-%{python3_version} --verbosity=2 \
 -w $RPM_BUILD_ROOT%{python3_sitearch}/prody/tests --tests prody -a '!slow'
popd
%endif

%files -n python3-%{name}
%license LICENSE.rst
%doc README.rst
%{_bindir}/prody
%{_bindir}/prody-%{python3_version}
%{_bindir}/python%{python3_version}-prody
%{_bindir}/evol
%{_bindir}/evol-%{python3_version}
%{_bindir}/python%{python3_version}-evol
%{python3_sitearch}/prody/
%{python3_sitearch}/%{name}-*.dist-info

%changelog
%autochangelog
