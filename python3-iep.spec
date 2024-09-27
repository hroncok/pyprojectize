Name:           python3-iep
Version:        3.7
Release:        32%{?dist}
Summary:        The interactive editor for Python

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.iep-project.org/
Source0:        https://pypi.python.org/packages/source/i/iep/iep-%{version}.tar.gz
Source1:        iep.desktop
Source2:        iep.appdata.xml

Patch0:         iep-3.7-python3.7.patch

BuildArch:      noarch

Requires:       adobe-source-code-pro-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       python3-PyQt4
Requires:       python3-pyzolib
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel

%description
IEP (pronounced as eep) is a cross-platform Python IDE focused on interactivity
and introspection, which makes it very suitable for scientific computing. Its
practical design is aimed at simplicity and efficiency.

%prep
%setup -qn iep-%{version}
%patch -P0 -p1

# Remove bundled fonts
rm -rf iep/resources/fonts

# Remove the unused style files (not yet implemented in IEP 3)
rm -f iep/resources/style_*.ssdf

# To fix non-executable-scripts in rpmlint
for lib in `find iep -name '*.py'`; do
    sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
install -D -m0644 iep/resources/appicons/ieplogo16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/iep.png
install -D -m0644 iep/resources/appicons/ieplogo32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/iep.png
install -D -m0644 iep/resources/appicons/ieplogo48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/iep.png
install -D -m0644 iep/resources/appicons/ieplogo64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/iep.png
install -D -m0644 iep/resources/appicons/ieplogo128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/iep.png
install -D -m0644 iep/resources/appicons/ieplogo256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/iep.png

desktop-file-install                            \
--dir=%{buildroot}%{_datadir}/applications      \
%{SOURCE1}

install -D -m0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/iep.appdata.xml

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/iep.desktop

%files
%doc iep/contributors.txt
%license iep/license.txt
%{_bindir}/iep
%{python3_sitelib}/iep
%{python3_sitelib}/iep-%{version}.dist-info
%{_datadir}/icons/hicolor/*/apps/iep.png
%{_datadir}/appdata/iep.appdata.xml
%{_datadir}/applications/iep.desktop

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.7-32
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.7-30
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.7-26
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.7-23
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.7-20
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.7-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 3.7-12
- Remove obsolete requirements for post/postun scriptlets

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Scott K Logan <logans@cottsay.net> - 3.7-10
- Add patch for Python compatibility

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.7-6
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.7-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 03 2016 Scott K Logan <logans@cottsay.net> - 3.7-1
- Update to 3.7
- Update to align with packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.5-3
- Add an AppData file for the software center

* Sat Jan 17 2015 Scott K Logan <logans@cottsay.net> - 3.5-2
- Add upstream patch to fix previous tab selection RHBZ#1161856
- Add upstream patch to fix the import wizard RHBZ#1181827

* Tue Jul 15 2014 Scott K Logan <logans@cottsay.net> - 3.5-1
- Update to 3.5
- Remove console script until it is fixed upstream
- Add BuildRequires python3-setuptools

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Apr 21 2014 Scott K Logan <logans@cottsay.net> - 3.4-2
- Un-bundle fonts and add them as requirements
- Remove unused style definition files (unimplemented in IEP 3)

* Fri Apr 04 2014 Scott K Logan <logans@cottsay.net> - 3.4-1
- Initial package
