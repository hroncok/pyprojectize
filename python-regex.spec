%global srcname regex

Name:           python-%{srcname}
Version:        2024.4.28
Release:        2%{?dist}
Summary:        Alternative regular expression module, to replace re
# see also https://code.google.com/p/mrab-regex-hg/issues/detail?id=124
# Automatically converted from old format: Python and CNRI - review is highly recommended.
License:        LicenseRef-Callaway-Python AND CNRI-Python
URL:            https://bitbucket.org/mrabarnett/mrab-regex
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  /usr/bin/rst2html
BuildRequires:  python3-pygments
BuildRequires:  gcc

%global _description %{expand:
This new regex implementation is intended eventually to replace
Python's current re module implementation.

For testing and comparison with the current 're' module the new
implementation is in the form of a module called 'regex'.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
# rebuild the HTML doc
rst2html docs/UnicodeProperties.rst > docs/UnicodeProperties.html
rst2html README.rst > README.html


%install
%pyproject_install


%files -n python%{python3_pkgversion}-%{srcname}
%doc README.html
%doc docs/Features.html
%doc docs/UnicodeProperties.html
%{python3_sitearch}/*


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2024.4.28-2
- convert license to SPDX

* Wed Aug 21 2024 Thomas Moschny <thomas.moschny@gmx.de> - 2024.4.28-1
- Update to 2024.4.28.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2024.4.16-2
- Rebuilt for Python 3.13

* Sat Apr 20 2024 Thomas Moschny <thomas.moschny@gmx.de> - 2024.4.16-1
- Update to 2024.4.16.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.12.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.12.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Thomas Moschny <thomas.moschny@gmx.de> - 2023.12.25-1
- Update to 2023.12.25.

* Sun Oct 22 2023 Thomas Moschny <thomas.moschny@gmx.de> - 2023.10.3-1
- Update to 2023.10.3.

* Sun Jul 30 2023 Thomas Moschny <thomas.moschny@gmx.de> - 2022.6.3-1
- Update to 2023.6.3.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.10.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2022.10.31-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.10.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  1 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2022.10.31-1
- Update to 2022.10.31.

* Thu Sep 15 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2022.9.13-1
- Update to 2022.9.13.

* Fri Sep  2 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2022.8.17-1
- Update to 2022.8.17.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.6.2-2
- Rebuilt for Python 3.11

* Fri Jun 10 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2022.6.2-1
- Update to 2022.6.2.

* Wed May 18 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2022.4.24-1
- Update to 2022.4.24.

* Sun Apr 10 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2022.3.15-1
- Update to 2022.3.15.

* Sat Mar  5 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2022.3.2-1
- Update to 2022.3.2.

* Wed Jan 26 2022 Thomas Moschny <thomas.moschny@gmx.de> - 2022.1.18-1
- Update to 2022.1.18.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.11.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2021.11.10-1
- Update to 2021.11.10.

* Sat Oct 30 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2021.10.23-1
- Update to 2021.10.23.

* Tue Sep 28 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2021.9.24-1
- Update to 2021.9.24.

* Fri Sep  3 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2021.8.28-1
- Update to 2021.8.28.

* Thu Aug 26 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2021.8.21-1
- Update to 2021.8.21.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul  6 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2021.7.6-1
- Update to 2021.7.6.

* Mon Jul  5 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2021.7.1-1
- Update to 2021.7.1.

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 2021.4.4-2
- Rebuilt for Python 3.10

* Mon Apr  5 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2021.4.4-1
- Update to 2021.4.4.

* Fri Apr  2 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2021.3.17-1
- Update to 2021.3.17.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.11.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.11.13-1
- Update to 2020.11.13.

* Thu Oct 29 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.10.28-1
- Update to 2020.10.28.

* Wed Oct 28 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.10.23-1
- Update to 2020.10.23.

* Mon Oct 12 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.10.11-1
- Update to 2020.10.11.

* Tue Sep 29 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.9.27-1
- Update to 2020.9.27.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.7.14-1
- Update to 2020.7.14.

* Sat Jun 20 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.6.8-2
- Update to 2020.6.8.

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2020.5.14-2
- Rebuilt for Python 3.9

* Fri May 15 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.5.14-1
- Update to 2020.5.14.

* Tue Apr 14 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.4.4-1
- Update to 2020.4.4.

* Sat Feb 22 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.2.20-1
- Update to 2020.2.20.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.1.8-1
- Update to 2020.1.8.

* Fri Jan  3 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2019.12.20-2
- Add BR on setuptools.

* Wed Jan  1 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2019.12.20-1
- Update to 2019.12.20.
- Update doc generation.

* Sat Dec 14 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.12.9-1
- Update to 2019.12.9.

* Sat Nov  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.11.1-1
- Update to 2019.11.1.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.08.19-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.08.19-2
- Remove Python2 subpackage (bz#1744656).

* Tue Aug 27 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.08.19-1
- Update to 2019.08.19.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.06.08-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.06.08-1
- Update to 2019.06.08.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.05.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.05.25-1
- Update to 2019.05.25.

* Mon Apr 15 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.04.14-1
- Update to 2019.04.14.

* Sat Mar  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.03.09-1
- Update to 2019.03.09.

* Sat Feb  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.02.07-1
- Update to 2019.02.07.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.01.24-1
- Update to 2019.01.24.

* Tue Dec 18 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.11.22-1
- Update to 2018.11.22.

* Sun Nov 11 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.11.07-1
- Update to 2018.11.07.

* Sun Jul 15 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.07.11-1
- Update to 2018.07.11.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.06.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.06.21-2
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.06.21-1
- Update to 2018.06.21.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.06.09-2
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.06.09-1
- Update to 2018.06.09.

* Wed Jun  6 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.06.06-1
- Update to 2018.06.06.

* Sun Mar  4 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.02.21-1
- Update to 2018.02.21.

* Sun Feb 11 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.02.08-1
- Update to 2018.02.08.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb  4 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.02.03-1
- Update to 2018.02.03.

* Sat Jan 13 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.01.10-1
- Update to 2018.01.10.

* Sat Nov 18 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2017.11.09-1
- Update to 2017.11.09.
- Build Python3 subpackage on EPEL7.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2016.09.22-2
- Rebuild for Python 3.6

* Sat Sep 24 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.09.22-1
- Update to 2016.09.22.

* Sun Aug  7 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.07.21-1
- Update to 2016.07.21.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2016.06.24-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul  4 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.06.24-1
- Update to 2016.06.24.

* Mon Jun 13 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.06.05-1
- Update to 2016.06.05.

* Fri Jun  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.06.02-1
- Update to 2016.06.02.
- Update upstream URL.

* Mon May 30 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.05.23-1
- Update to 2016.05.23.

* Fri Apr 29 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.04.25-1
- Update to 2016.04.25.

* Sat Apr  9 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.04.08-1
- Update to 2016.04.08.
- Update upstream URL.

* Tue Apr  5 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.04.02-1
- Update to 2016.04.02.

* Mon Mar  7 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.03.02-2
- Update to 2016.03.02.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2016.01.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.01.10-1
- Update to 2016.01.10.

* Sun Dec 20 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.11.22-1
- Update to 2015.11.22.
- Follow updated Python packaging guidelines.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.07.19-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 27 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.07.19-1
- Update to 2015.07.19.

* Thu Jun 25 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.06.24-1
- Update to 2015.06.24.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.05.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.05.28-1
- Update to 2015.05.28.

* Sat May 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.05.10-1
- Update to 2015.05.10.

* Sat Mar 21 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.03.18-1
- Update to 2015.03.18.
- Apply updated Python packaging guidelines.

* Thu Jan  8 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2014.12.24-1
- Update to 2014.12.24.

* Sun Dec 21 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2014.12.15-1
- Update to 2014.12.15.

* Sat Dec 13 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2014.11.14-1
- Update to 2014.11.14.
- Rebuild the HTML docs.
- Update License tag.
- Update upstream URL.

* Wed Oct 22 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2014.10.09-1
- Initial version.
