Summary:       The gerrit client tools
Name:          gerrymander
Version:       1.5
Release:       33%{?dist}
Source0:       https://pypi.python.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
URL:           https://pypi.python.org/pypi/gerrymander
License:       Apache-2.0

BuildArch:     noarch

BuildRequires: python3-pytest
BuildRequires: python3-devel
Requires:      python3-gerrymander

%package -n python3-gerrymander
Summary: The gerrit python3 client
License: GPLv2+


%description
The gerrymander package provides a set of command line tools
for interacting with Gerrit

%description -n python3-gerrymander
The python3-gerrymander package provides a set of python3
modules for interacting with Gerrit.

%prep
%setup -q
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

# Remove any egg info (as of submitting this review, there's no bundled
# egg info)
rm -rf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gerrymander

%check
%pytest

%files
%doc conf/gerrymander.conf-example
%{_bindir}/gerrymander

%files -n python3-gerrymander -f %{pyproject_files}
%doc README LICENSE

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5-32
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5-28
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5-25
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5-22
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5-19
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-16
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-13
- Remove python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5-8
- Python 2 binary package renamed to python2-gerrymander
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.5-6
- Fix Python 2 dependency in gerrymander (RHBZ#1422897)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Adam Williamson <awilliam@redhat.com> - 1.5.4
- fix test invocation for Python 3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 29 2016 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.5.2
- Add the Python PrettyTable dependency to relevant sub-packages
  (Thanks, Daniel Berrange, Matthew Booth)

* Mon Feb 22 2016 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.5.1
- New upstream release 1.5

* Tue Feb 16 2016 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.4.5
- Add 'python-prettytable' to 'Requires'; fixes rhbz# 1307167

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.4.1
- Update to new upstream release 1.4
- Change the official source to pypi (from github generated tarballs)
- Change the URL to pypi

* Wed Aug 20 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3.4
- Remove with_python3 conditional, as current Fedora releases have it

* Tue Aug 19 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3.3
- Update %%files section correctly

* Mon Aug 18 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3.2
- Address review comments from rhbz# 1128253

* Tue Aug 05 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3-1
- Initial package
