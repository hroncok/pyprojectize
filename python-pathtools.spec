%global upname pathtools

Name:		python-%{upname}
Version:	0.1.2
Release:	37%{?dist}
Summary:	Pattern matching and various utilities for file systems paths

License:	MIT
URL:		https://github.com/gorakhargosh/%{upname}
Source0:	%{pypi_source %{upname}}
# This is hacky, but I don't feel like writing a real fix for this
# silly upstream approach. imp is retired in python 3.12, so we need
# to not use it. This replaces the use of it with a marker string
# we'll sub out with the real version in %prep
# not upstreamable, upstream would need to do the mess recommended at
# https://docs.python.org/3.12/whatsnew/3.12.html#removed , or just
# use a less silly way of getting version numbers into setup.py...
# reported as https://github.com/gorakhargosh/pathtools/issues/13
Patch:		pathtools-0.1.2-version_imp.patch

BuildArch:	noarch
BuildRequires: make
BuildRequires:	python3-devel
BuildRequires:	python3-sphinx

%global _description\
%{name} is a Python API library for common path\
and pattern functionality.\


%description %_description

%package -n python3-%{upname}
Summary: %summary

%description -n python3-%{upname} %_description


%prep
%autosetup -n %{upname}-%{version} -p1

# remove hashbang from lib's files
sed -i -e '/#!\//d' pathtools/*.py

# Use the default sphinx theme
# python-flask-sphinx-themes is orphaned
sed -i "s/html_theme = 'flask'/html_theme = 'default'/" ./docs/source/conf.py

# replace the marker from the imp-removal patch with the real version
sed -i -e "s,||VERSION||,'%{version}',g" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

pushd docs
make SPHINXBUILD=sphinx-build-3 html
rm -rf build/html/.build*
popd


%install
%pyproject_install
%pyproject_save_files -l 'pathtools*'


%files -n python3-%{upname} -f %{pyproject_files}
%doc AUTHORS LICENSE README
%doc docs/build/html


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.2-36
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 25 2023 Adam Williamson <awilliam@redhat.com> - 0.1.2-33
- Use a hacky patch to get rid of imp usage so it'll build with Python 3.12

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.1.2-31
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.2-28
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.2-25
- Rebuilt for Python 3.10

* Fri Feb 19 2021 Lumír Balhar <lbalhar@redhat.com> - 0.1.2-24
- Switch do default sphinx theme

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-21
- Rebuilt for Python 3.9

* Mon Dec 09 2019 Stephen Coady <scoady@redhat.com> - 0.1.2-20
- Rebuilt to adopt package

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-19
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-18
- Drop python2-pathtools

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-16
- Only build the documentation on Python 3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-14
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.2-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.2-11
- Python 2 binary package renamed to python2-pathtools
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Aug 12 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.2-1
- Initial RPM release (#996088)
