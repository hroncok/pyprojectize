%global srcname textile

Name:           python-%{srcname}
Version:        4.0.2
Release:        12%{?dist}
Summary:        A Humane Web Text Generator
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.io/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  sed
BuildRequires:  findutils


%description
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.


%package -n python3-%{srcname}
Summary:        A Humane Web Text Generator
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-regex
BuildRequires:  python3-six
BuildRequires:  python3-pillow
BuildRequires:  python3-html5lib >= 0.999999999
Requires:       python3-regex
Requires:       python3-six
Requires:       python3-pillow
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install

for f in README CHANGELOG ; do
  PYTHONPATH=%{buildroot}%{python3_sitelib} \
  PATH=%{buildroot}%{_bindir}:${PATH} \
    pytextile < ${f}.textile > ${f}.html
done

# remove shebangs
find %{buildroot}%{python3_sitelib} -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;


%check
# run the testsuite and log results, but do not fail the build
%{__python3} ./setup.py test || :


%files -n python3-%{srcname}
%doc README.* CONTRIBUTORS.txt CHANGELOG.*
%license LICENSE.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info
%{_bindir}/pytextile


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0.2-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.0.2-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 4.0.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec  5 2021 Thomas Moschny <thomas.moschny@gmx.de> - 4.0.2-1
- Update to 4.0.2.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.0.1-1
- Update to 4.0.1.

* Sat Jan 25 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.0.0-1
- Update to 4.0.0.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-4
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.4-3
- Drop Python2 subpackage.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.4-1
- Update to 3.0.4.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.3-2
- Rebuilt for Python 3.7

* Sun Apr 22 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.3-1
- Update to 3.0.3.

* Tue Apr 17 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.2-1
- Update to 3.0.2.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.0-1
- Update to 3.0.0.

* Wed Aug 16 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.16-1
- Update to 2.3.16.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.15-1
- Update to 2.3.15.

* Thu Jul 20 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.14-1
- Update to 2.3.14.

* Sun Jun  4 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.12-1
- Update to 2.3.12.

* Mon May  1 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.11-1
- Update to 2.3.11.

* Sat Apr 22 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.10-1
- Update to 2.3.10.

* Mon Apr 10 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.9-1
- Update to 2.3.9.

* Sun Apr  9 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.8-1
- Update to 2.3.8.

* Sun Mar 19 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.7-1
- Update to 2.3.7.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3.6-2
- Rebuild for Python 3.6

* Wed Nov  9 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.6-1
- Update to 2.3.6.

* Tue Nov  1 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.4-1
- Update to 2.3.4.

* Sun Sep 25 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.3-1
- Update to 2.3.3.
- Follow updated Python packaging guidelines.
- Update Requires and BuildRequires.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.2-1
- Update to 2.2.2.
- Apply updated Python packaging guidelines.
- Mark LICENSE with %%license.

* Thu Jan  8 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.1-1
- Update to 2.2.1.

* Fri Jun 13 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.8-1
- Update to 2.1.8.
- Update upstream URLs.
- Provide a Python3 subpackage.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jan 30 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.5-2
- Add patch to support pillow (bz 896295).

* Fri Nov 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.5-1
- Update to 2.1.5.
- Include LICENSE.txt.
- Spec file cleanups.
- Disable tests for now.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Apr 16 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.4-3
- Simplify %%check.

* Fri Apr 16 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.4-2
- Add missing BR python-nose for the tests.
- Actually run the tests in %%check.
- Remove obsolete comment about tidy.

* Fri Apr 16 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.4-1
- Update to 2.1.4.
- Use %%global instead of %%define.
- README is missing in the tarfile.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 11 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.3-1
- Upstream and upstream URLs changed.
- Update to 2.1.3.
- Remove now obsolete tweak for enabling import of htmlizer.
- Process README.textile provided in the package.
- Run test.py in %%check section.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0.11-5
- Rebuild for Python 2.6

* Sat Apr  5 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.11-4
- Simplify BR.

* Mon Jan 28 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.11-3
- As the license text in the main source file is unchanged, revert the
  license tag back to BSD.

* Fri Jan 18 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.11-2
- Updated main and source urls. The website states that the package is
  now under the MIT License.

* Sat Sep  8 2007 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.11-1
- Initial version.
