Name:		nanovna-saver
Version:	0.6.4
Release:	3%{?dist}
Summary:	Tool for reading, displaying and saving data from the NanoVNA
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/NanoVNA-Saver/%{name}

Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	coreutils
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	python3-pyserial
BuildRequires:	python3-numpy
BuildRequires:	python3-scipy
BuildRequires:	python3-qt5
BuildRequires:	python3-Cython
BuildRequires:	desktop-file-utils
# for fixing the version
BuildRequires:	sed
Requires:	hicolor-icon-theme
# OS/distro specific
Patch0:		nanovna-saver-0.6.2-fedora-icon.patch
Patch1:		nanovna-saver-0.6.2-relax-deps.patch

%description
A multiplatform tool to save Touchstone files from the NanoVNA, sweep
frequency spans in segments to gain more than 101 data points, and
generally display and analyze the resulting data.

%prep
%autosetup -p1

# fix version
sed -i '/^\s*version\s=/ s/attr: NanoVNASaver.About.version/%{version}/' setup.cfg

%build
%py3_build

%install
%py3_install

# Drop tests
rm -rf %{buildroot}%{python3_sitelib}/test

# manual page
install -Dpm 0644 docs/man/NanoVNASaver.1 %{buildroot}%{_mandir}/man1/NanoVNASaver.1

# desktop file
desktop-file-install NanoVNASaver.desktop

# icon
install -Dpm 0644 icon_48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/NanoVNASaver_48x48.png


# https://github.com/NanoVNA-Saver/nanovna-saver/issues/443
#%%check
#%%{python3} setup.py test

%files
%license LICENSE.txt
%doc README.rst docs/CODE_OF_CONDUCT.md docs/CONTRIBUTING.md AUTHORS.rst
%{_bindir}/NanoVNASaver
%{python3_sitelib}/NanoVNASaver
%{python3_sitelib}/NanoVNASaver-%{version}-py*.egg-info
%{_mandir}/man1/NanoVNASaver.1*
%{_datadir}/icons/hicolor/48x48/apps/NanoVNASaver_48x48.png
%{_datadir}/applications/NanoVNASaver.desktop

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.4-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.6.4-1
- New version
  Resolves: rhbz#2294350

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.6.3-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.6.3-1
- New version
  Resolves: rhbz#2250502

* Fri Aug 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.6.2-1
- New version
  Resolves: rhbz#2228299

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.5.5-2
- Rebuilt for Python 3.12

* Tue Mar  7 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.5.5-1
- New version
  Resolves: rhbz#2175630

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan  3 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.5.4-1
- New version
  Resolves: rhbz#2157654

* Thu Sep 22 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.5.3-1
- New version
  Resolves: rhbz#2125428

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.4.0-4
- Rebuilt for Python 3.11

* Thu Apr 21 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0-3
- More relaxed dependencies
  Resolves: rhbz#2075865

* Wed Apr  6 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0-2
- Relaxed dependencies
  Resolves: rhbz#2071947

* Mon Apr  4 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0-1
- New version
  Resolves: rhbz#2071189

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.10-3
- Relaxed dependencies
  Resolves: rhbz#2038547

* Fri Jan  7 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.10-2
- Rebuilt for new versions of python deps
  Resolves: rhbz#2037947

* Thu Jan  6 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.10-1
- New version
  Resolves: rhbz#2030250

* Tue Dec  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.9-1
- New version

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.2-7
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-4
- Rebuilt for Python 3.9

* Tue Feb 25 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-3
- Fixed according to the review

* Fri Feb 21 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-2
- Fixed according to the review

* Wed Feb  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-1
- Initial version
