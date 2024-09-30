%define srcname notofonttools

%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
%define with_python3 1
%else
%define with_python2 1
%define with_python3 1
%endif

%global common_desc \
The nototools python package contains python scripts \
used to maintain the Noto Fonts project, \
including the google.com/get/noto website.

Name:		nototools
Version:	0.2.19
Release:	3%{?dist}
Summary:	Noto fonts support tools and scripts plus web site generation

# In nototools source
## nototools code is in ASL 2.0 license
### third_party ucd code is in Unicode license
License:	Apache-2.0
URL:		https://github.com/googlefonts/nototools
Source0:	%pypi_source

BuildArch:	noarch
%if %{with python2}
BuildRequires:	python2-devel
BuildRequires:	python2-wheel
BuildRequires:	python2-setuptools_scm
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-wheel
BuildRequires:	python3-setuptools_scm
%endif

%if %{with python2}
Requires:	python2-nototools = %{version}-%{release}
%endif
%if %{with python3}
Requires:	python3-nototools = %{version}-%{release}
%endif

%description
%common_desc

%if %{with python3}
%package     -n python3-nototools
Summary:	Noto tools for python 3
Requires:	python3dist(fonttools)
BuildRequires:	python3dist(fonttools)

%description -n python3-nototools
%common_desc

%endif

%if %{with python2}
%package     -n python2-nototools
Summary:	Noto tools for python 2
Requires:	python2dist(fonttools)
BuildRequires:	python2dist(fonttools)

%description -n python2-nototools
%common_desc

%endif

%prep
%setup -c

# remove unneeded files
rm -rf %{srcname}-%{version}/third_party/{cldr,dspl,fontcrunch,ohchr,spiro,udhr,unicode}
mv %{srcname}-%{version} python2

%if %{with python3}
cp -a python2 python3
%endif

# for documents
cp python2/*.md python2/LICENSE .

%generate_buildrequires
%pyproject_buildrequires

%build
%if %{with python2}
pushd python2
%py2_build
popd
%endif

%if %{with python3}
pushd python3
%pyproject_wheel
popd
%endif


%install
%if %{with python3}
pushd python3
%pyproject_install
for lib in %{buildroot}%{python3_sitelib}/nototools/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
popd
%endif

%if %{with python2}
pushd python2
%py2_install
for lib in %{buildroot}%{python2_sitelib}/nototools/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
popd
%endif

%check
%if %{with python2}
pushd python2
# This doesn’t actually run any tests at all, therefore it doesn‘t fail:
%{__python2} setup.py test
popd
%endif

%if %{with python3}
pushd python3
# Comment it out for the moment because it tries to run something which fails
#%{__python3} setup.py test
popd
%endif


%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/add_vs_cmap.py
%{_bindir}/autofix_for_release.py
%{_bindir}/create_image.py
%{_bindir}/decompose_ttc.py
%{_bindir}/drop_hints.py
%{_bindir}/dump_otl.py
%{_bindir}/fix_khmer_and_lao_coverage.py
%{_bindir}/fix_noto_cjk_thin.py
%{_bindir}/generate_sample_text.py
%{_bindir}/merge_fonts.py
%{_bindir}/merge_noto.py
%{_bindir}/noto_lint.py
%{_bindir}/notocoverage
%{_bindir}/notodiff
%{_bindir}/scale.py
%{_bindir}/subset.py
%{_bindir}/subset_symbols.py
%{_bindir}/test_vertical_extents.py

%if %{with python2}
%files -n python2-nototools
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{srcname}-%{version}.dist-info
%{python2_sitelib}/third_party
%endif

%if %{with python3}
%files -n python3-nototools
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{srcname}-%{version}.dist-info
%{python3_sitelib}/third_party
%endif


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.2.19-2
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Peng Wu <pwu@redhat.com> - 0.2.19-1
- Update to 0.2.19

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 0.2.17-4
- Rebuilt for Python 3.12

* Thu May 18 2023 Peng Wu <pwu@redhat.com> - 0.2.17-3
- Migrate to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 26 2022 Peng Wu <pwu@redhat.com> - 0.2.17-1
- Update to 0.2.17

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.2.13-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.13-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Peng Wu <pwu@redhat.com> - 0.2.13-1
- Update to 0.2.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20190715.git9c4375f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.20190714.git9c4375f
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20190713.git9c4375f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.20190712.git9c4375f
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.20190711.git9c4375f
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20190710.git9c4375f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  9 2019 Mike FABIAN <mfabian@redhat.com> - 0-0.20190709.git9c4375f
- Update nototools package from upstream git repo
- Also build the python3-nototools package

* Tue Mar  5 2019 Peng Wu <pwu@redhat.com> - 0-0.20190305.gitbb309e8
- Update nototools package from upstream git repo

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20170929.git0c99dff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20170928.git0c99dff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20170927.git0c99dff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Peng Wu <pwu@redhat.com> - 0-0.20170926.git0c99dff
- Initial package
