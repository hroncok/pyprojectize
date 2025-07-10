# If the package needs to download data for the test which cannot be done in
# koji, these can be disabled in koji by using `bcond_with` instead, but the
# tests must be validated in mock with network enabled like so:
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enable-network --rpmbuild-opts="--with tests"
%bcond_with tests

%global pypi_name pyfim

%global desc %{expand: \
PyFIM is an extension module that makes several frequent item set mining
implementations available as functions in Python 2.7.x & 3.5.x. Currently
apriori, eclat, fpgrowth, sam, relim, carpenter, ista, accretion and apriacc
are available as functions, although the interfaces do not offer all of the
options of the command line program. (Note that lcm is available as an
algorithm mode of eclat.) There is also a "generic" function fim, which is
essentially the same function as fpgrowth, only with a simplified interface
(fewer options). Finally, there is a function arules for generating association
rules (simplified interface compared to apriori, eclat and fpgrowth, which can
also be used to generate association rules.

How to use the functions can be seen in the example scripts testfim.py and
testacc.py in the source package (directory pyfim/ex). From a Python script or
command prompt interface, call help(fim), help(apriori) (or help(fim.apriori)),
help(eclat) (or help(fim.eclat)) etc. or print, for example, apriori.__doc__,
eclat.__doc__ etc. for a description of the functions and their arguments.

This extension module was originally developed for Python 2.7. The shared
objects made available above were compiled particularly for Python 2.7.11 and
Python 3.5.1 on Ubuntu 16.04 LTS and the dynamic modules made available above
were compiled for Python 2.7.10 and Python 3.5.1 on Windows 10.}

Name:           python-%{pypi_name}
Version:        6.28
Release:        18%{?dist}
Summary:        Frequent Item Set Mining and Association Rule Induction

License:        MIT
URL:            http://www.borgelt.net/%{pypi_name}.html
Source0:        http://www.borgelt.net/src/%{pypi_name}.tar.gz

%description
%{desc}


%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Cython}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -c -n %{pypi_name}-%{version}
# Replace use of distutils.core.setup
sed -i -e 's/distutils\.core/setuptools/' setup.py

# Remove date stamp from version
sed -i "s/version=.*/version='6.28',/" setup.py

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fim

%check
%pyproject_check_import

%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
# All sub directories contain this file
%license pyfim/doc/mit-license.txt

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 6.28-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 6.28-14
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.28-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.28-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.28-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.28-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 6.28-1
- Use better file entry

* Mon Jun 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 6.28-1
- Initial build
