%global common_summary_en Reader for the RADEX RD1212 and ONE Geiger counters
%global common_summary_fr Lecteur pour les compteurs Geiger RADEX RD1212 et ONE

%global common_description_en %{expand:
The RadexReader is an user-space driver for the RADEX RD1212 and
the RADEX ONE Geiger counters. It allow to read and clear stored
data via USB.

To avoid Access denied (insufficient permissions), don't forget
to unplug the device after installation.}

%global common_description_fr %{expand:
Le RadexReader est un pilote en espace utilisateur pour les compteurs
Geiger RADEX RD1212 et RADEX ONE. Il permet de lire et d'effacer les
données stockées via USB.

Pour éviter un Access denied (insufficient permissions), n'oubliez pas
de débrancher l'appareil après l'installation.}

Name:          python-radexreader
Version:       1.2.4
Release:       4%{?dist}
Summary:       %{common_summary_en}
Summary(fr):   %{common_summary_fr}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://github.com/luigifab/python-radexreader
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: aspell-fr

%description %{common_description_en}
%description -l fr %{common_description_fr}


%package -n python3-radexreader
%py_provides python3-radexreader
Summary:       %{common_summary_en}
Summary(fr):   %{common_summary_fr}

BuildRequires: python3-devel
Requires:      python3
Requires:      %{py3_dist pyserial}
Requires:      %{py3_dist pyusb}

%description -n python3-radexreader %{common_description_en}
%description -n python3-radexreader -l fr %{common_description_fr}


%prep
%setup -q -n python-radexreader-%{version}
sed -i 's/python3-radexreader /python3-radexreader-rpm /g' src/radexreader.py
sed -i 's/\#\!\/usr\/bin\/python3/\#/g' src/radexreader/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
cd src
%pyproject_wheel

%install
cd src
%pyproject_install
%pyproject_save_files -l radexreader
mkdir -p %{buildroot}%{_bindir}/
install -pm 755 radexreader.py %{buildroot}%{_bindir}/radexreader

mkdir -p %{buildroot}%{_mandir}/man1/ %{buildroot}%{_mandir}/fr/man1/
install -pm 644 ../debian/radexreader.1 %{buildroot}%{_mandir}/man1/radexreader.1
install -pm 644 ../debian/radexreader.fr.1 %{buildroot}%{_mandir}/fr/man1/radexreader.1

mkdir -p %{buildroot}/lib/udev/rules.d/
install -pm 644 ../debian/udev %{buildroot}/lib/udev/rules.d/60-%{name}.rules

%files -n python3-radexreader -f %{pyproject_files}
%doc README.md
%{_bindir}/radexreader
%{_mandir}/man1/radexreader.1*
%{_mandir}/*/man1/radexreader.1*
/lib/udev/rules.d/60-%{name}.rules


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.4-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.4-2
- Rebuilt for Python 3.13

* Fri Feb 02 2024 Fabrice Creuzot <code@luigifab.fr> - 1.2.4-1
- New upstream release

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Fabrice Creuzot <code@luigifab.fr> - 1.2.3-1
- New upstream release

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 17 2023 Python Maint <python-maint@redhat.com> - 1.2.2-4
- Rebuilt for Python 3.12

* Fri Jun 16 2023 Fabrice Creuzot <code@luigifab.fr> - 1.2.2-3
- Package spec update

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.12

* Tue Jun 06 2023 Fabrice Creuzot <code@luigifab.fr> - 1.2.2-1
- New upstream release

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Fabrice Creuzot <code@luigifab.fr> - 1.2.1-1
- New upstream release

* Wed May 05 2021 Fabrice Creuzot <code@luigifab.fr> - 1.2.0-1
- Initial Fedora package release (Closes: rhbz#1896742)
