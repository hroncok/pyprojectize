Name:           quisk
Version:        4.2.38
Release:        2%{?dist}
Summary:        Software Defined Radio (SDR) software

# Automatically converted from old format: GPLv2 and BSD - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-BSD
URL:            http://james.ahlstrom.name/quisk/
Source0:        https://files.pythonhosted.org/packages/source/q/%{name}/%{name}-%{version}.tar.gz
Source1:        quisk.desktop
Source2:        quisk.png
Source3:        name.ahlstrom.james.Quisk.metainfo.xml

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-wxpython4
BuildRequires:  fftw-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  dos2unix
BuildRequires:  libsoundio-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
Requires:       hicolor-icon-theme
Requires:       python3-wxpython4
Suggests:       codec2-devel

%description
QUISK is a Software Defined Radio (SDR) which can control various
radio hardware. QUISK supports CW, SSB, and AM.

%prep
%autosetup -p1

dos2unix afedrinet/sdr_control.py

# remove binaries, etc
find . -name \*.pyc -exec rm {} \;
find . -name \*.pyd -exec rm {} \;
find . -name \*.so -exec rm {} \;
find . -name \*.o -exec rm {} \;
find . -name \*.dll -exec rm {} \;

# remove execute permissions from everything
find . -type f -exec chmod a-x {} \;

# fix shebangs
sed -i 's|#!\s*/usr/bin/python|#!/usr/bin/python3|;s|#!\s*/usr/bin/env\s\+python3\?|#!/usr/bin/python3|' \
  quisk.py quisk_vna.py portaudio.py n2adr/startup.py \
  afedrinet/sdr_control.py afedrinet/afedri.py

%generate_buildrequires
%pyproject_buildrequires

%build
CFLAGS="%{optflags}" %{__python3} setup.py build_ext --inplace
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}
# make Python scripts with shebangs executable
for f in `find %{buildroot}%{python3_sitearch}/%{name} -name \*.py`
do
    grep -E -q '^#!' $f && chmod a+x $f
done

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

install -Dpm 0644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/quisk.png

install -Dpm 0644 %{SOURCE3} \
  %{buildroot}%{_metainfodir}/name.ahlstrom.james.Quisk.metainfo.xml

%files -f %{pyproject_files}
%license license.txt
%doc docs.html defaults.html
%doc help.html help_vna.html
%{_bindir}/%{name}{,_vna}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_metainfodir}/name.ahlstrom.james.Quisk.metainfo.xml


%changelog
* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2.38-2
- convert license to SPDX

* Mon Sep  2 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.38-1
- New version
  Resolves: rhbz#2309118

* Mon Aug 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.37-1
- New version
  Resolves: rhbz#2307080

* Mon Aug 12 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.36-1
- New version
  Resolves: rhbz#2302645

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.35-1
- New version
  Resolves: rhbz#2295559

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.2.34-2
- Rebuilt for Python 3.13

* Mon May 27 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.34-1
- New version
  Resolves: rhbz#2283079

* Mon Apr 29 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.32-1
- New version
  Resolves: rhbz#2277230

* Mon Apr  8 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.31-1
- New version
  Resolves: rhbz#2273463

* Thu Mar 21 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.30-1
- New version
  Resolves: rhbz#2270511

* Mon Feb 19 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.29-2
- Fixed FTBFS with python-3.13
  Resolves: rhbz#2254186

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.29-1
- New version
  Resolves: rhbz#2257946

* Tue Jan  2 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.28-1
- New version
  Resolves: rhbz#2254908

* Thu Dec 14 2023 Daniel Rusek <mail@asciiwolf.com> - 4.2.27-2
- Added desktop files and AppStream metadata

* Mon Dec 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.27-1
- New version
  Resolves: rhbz#2253680

* Thu Dec  7 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.26-1
- New version
  Resolves: rhbz#2253316

* Mon Dec  4 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.25-1
- New version
  Resolves: rhbz#2252153

* Mon Nov 20 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.24-1
- New version
  Resolves: rhbz#2250472

* Mon Sep 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.23-1
- New version
  Resolves: rhbz#2238411

* Thu Aug 24 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.22-1
- New version
  Resolves: rhbz#2232950

* Tue Aug  1 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.21-1
- New version
  Resolves: rhbz#2227572

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.20-1
- New version
  Resolves: rhbz#2223730

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 4.2.19-2
- Rebuilt for Python 3.12

* Fri May 19 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.19-1
- New version
  Resolves: rhbz#2208354

* Wed Apr 26 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.18-1
- New version
  Resolves: rhbz#2189584

* Fri Feb 17 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.17-1
- New version
  Resolves: rhbz#2169853

* Tue Jan 24 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.16-1
- New version
  Resolves: rhbz#2163011

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan  5 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.15-1
- New version
  Resolves: rhbz#2158291

* Mon Jan  2 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.14-1
- New version
  Resolves: rhbz#2154117

* Thu Dec  8 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.13-1
- New version
  Resolves: rhbz#2150654

* Mon Nov 21 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.12-1
- New version
  Resolves: rhbz#2144213

* Sun Nov 13 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.11-1
- New version
  Resolves: rhbz#2141831

* Wed Oct  5 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.9-1
- New version
  Resolves: rhbz#2132434

* Tue Oct  4 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.8-1
- New version
  Resolves: rhbz#2131307

* Sat Sep 24 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.7-1
- New version
  Resolves: rhbz#2125924

* Mon Sep  5 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.5-1
- New version

* Wed Aug 31 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.4-1
- New version

* Tue Aug 30 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.3-1
- New version
  Resolves: rhbz#2122301

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.2-2
- Fixed wrong shebang replacement script
  Resolves: rhbz#2106412

* Mon Jul 11 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.2-1
- New version
  Resolves: rhbz#2105083

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 4.2.1-4
- Rebuilt for Python 3.11

* Fri Jun 17 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.1-3
- Fixed quisk with hamlib-4.4

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 4.2.1-2
- Rebuilt for Python 3.11

* Wed Jun  8 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.1-1
- New version
  Resolves: rhbz#2094964

* Mon May 23 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.0-1
- New version
  Resolves: rhbz#2088918

* Sun May 15 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.96-1
- New version
  Resolves: rhbz#2084956

* Tue May 10 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.95-1
- New version
  Resolves: rhbz#2082969

* Tue Apr 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.94-1
- New version
  Resolves: rhbz#2074177

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.93-1
- New version
  Resolves: rhbz#2034435

* Mon Nov  1 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.92-1
- New version
  Resolves: rhbz#2018715

* Tue Oct 26 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.91-1
- New version
  Resolves: rhbz#2017127

* Fri Oct 15 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.90-1
- New version
  Resolves: rhbz#2014612

* Thu Oct  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.89-1
- New version
  Resolves: rhbz#2011068

* Tue Oct  5 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.88-1
- New version
  Resolves: rhbz#2004163

* Mon Sep  6 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.86-1
- New version
  Resolves: rhbz#2000733

* Thu Sep  2 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.85-1
- New version

* Mon Aug 16 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.84-1
- New version
  Resolves: rhbz#1993704

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.83-1
- New version
  Resolves: rhbz#1976624

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.1.82-2
- Rebuilt for Python 3.10

* Thu May 20 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.82-1
- New version
  Resolves: rhbz#1962373

* Fri Apr 30 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.81-1
- New version
  Resolves: rhbz#1955799

* Mon Feb 22 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.80-1
- New version
  Resolves: rhbz#1931081

* Thu Feb 18 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.79-1
- New version
  Resolves: rhbz#1930349

* Tue Feb 16 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.78-1
- New version
  Resolves: rhbz#1928278

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.77-1
- New version
  Resolves: rhbz#1918484

* Thu Jan 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.76-1
- New version
  Resolves: rhbz#1916497

* Tue Dec 22 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.75-1
- New version
  Resolves: rhbz#1909830

* Wed Dec  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.74-1
- New version
  Resolves: rhbz#1906161

* Wed Nov 11 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.73-1
- New version
  Resolves: rhbz#1896889

* Wed Sep 23 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.72-1
- New version
  Resolves: rhbz#1880465

* Tue Sep  8 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.71-1
- New version
  Resolves: rhbz#1875953

* Sun Aug 30 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.70-1
- New version
  Resolves: rhbz#1873818

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.69-1
- New version
  Resolves: rhbz#1871976

* Sat Aug 15 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.68-1
- New version
  Resolves: rhbz#1868941

* Fri Jul 31 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.67-1
- New version
  Resolves: rhbz#1862424

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.66-1
- New version
  Resolves: rhbz#1858527

* Thu Jul  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.65-1
- New version
  Resolves: rhbz#1854984

* Wed Jul  8 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.64-2
- Enabled libsoundio support

* Thu Jul  2 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.64-1
- New version
  Resolves: rhbz#1853315

* Sun Jun 28 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.63-1
- New version
  Related: rhbz#1851600

* Sun Jun 28 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.62-1
- New version
  Resolves: rhbz#1851600

* Fri Jun 26 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.61-1
- New version
  Resolves: rhbz#1851441

* Tue Jun 23 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.60-1
- New version
  Resolves: rhbz#1849989

* Mon Jun 22 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.59-1
- New version
  Resolves: rhbz#1849289

* Wed Jun 17 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.58-1
- New version
  Resolves: rhbz#1847630

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.57-2
- Rebuilt for Python 3.9

* Thu May  7 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.57-1
- New version
  Resolves: rhbz#1833089

* Fri Apr 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.56-1
- New version
  Resolves: rhbz#1822719

* Mon Apr  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.55-1
- New version
  Resolves: rhbz#1820661

* Wed Apr  1 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.54-1
- New version
  Resolves: rhbz#1819225

* Fri Mar 27 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.53-1
- New version
  Resolves: rhbz#1818091

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.52-1
- New version
  Resolves: rhbz#1783705

* Sun Nov 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.51-1
- New version
  Resolves: rhbz#1775966

* Thu Nov 21 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.50-1
- New version
  Resolves: rhbz#1774760

* Fri Nov 15 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.49-1
- New version
  Resolves: rhbz#1772608

* Fri Nov  8 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.48-2
- Switched to Python 3
  Resolves: rhbz#1737848

* Wed Nov  6 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.48-1
- New version
  Resolves: rhbz#1769036

* Thu Oct 31 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.47-1
- New version
  Resolves: rhbz#1767463

* Tue Oct 22 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.46-1
- New version
  Resolves: rhbz#1764201

* Mon Sep 30 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.45-2
- Fixed CTCSS tone generation
- Fixed traceback on systems with unicode pulseaudio device names

* Tue Sep 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.45-1
- New version
  Resolves: rhbz#1751364

* Fri Aug 30 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.43-1
- New version
  Resolves: rhbz#1747002

* Fri Aug 23 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.42-1
- New version
  Resolves: rhbz#1744610

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.41-1
- New version
  Resolves: rhbz#1723961

* Mon Jun 10 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.40-1
- New version
  Resolves: rhbz#1718590

* Fri May 10 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.39-1
- New version
  Resolves: rhbz#1708747

* Thu Apr 18 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.38-1
- New version
  Resolves: rhbz#1701354

* Wed Apr 10 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.37-1
- New version
  Resolves: rhbz#1698049

* Fri Mar 22 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.36-1
- Updated to latest upstream
  Resolves: rhbz#1632940
  Resolves: rhbz#1632941
- Added weak dependency on codec2-devel for FreeDV support
  Resolves: rhbz#1633195

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Eric Smith <brouhaha@fedoraproject.org> 4.1.17-1
- Updated to latest upstream.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 Eric Smith <brouhaha@fedoraproject.org> 4.1.10-1
- Updated to latest upstream.
- Spec changes per package review (#1443429).

* Wed Apr 19 2017 Eric Smith <brouhaha@fedoraproject.org> 4.1.3-1
- Initial version.
