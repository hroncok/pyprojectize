%global pypi_name spectrographic

Name: %{pypi_name}
Summary: Turn an image into sound whose spectrogram looks like the image
License: MIT

Version: 0.9.3
Release: 17%{?dist}

URL: https://github.com/LeviBorodenko/%{pypi_name}
Source0: %{pypi_source}

Patch0: 0000-remove-pyscaffold-max-version-constraint.patch
Patch1: 0001-add-version-metadata.patch

BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-pyscaffold
BuildRequires: python3-sphinx

# These aren't strictly required, but sphinx complains
# and yells warnings about failed imports when they're not installed
BuildRequires: python3-pillow
BuildRequires: python3-simpleaudio
BuildRequires: python3-wavio

BuildArch: noarch


%description
Turn any image into a sound whose spectrogram looks like the image!

Most sounds are intricate combinations of many acoustic waves, each having
different frequencies and intensities. A spectrogram is a way to represent
sound by plotting time on the horizontal axis and the frequency spectrum
on the vertical axis. Sort of like sheet music on steroids.

What this tool does is, taking an image and simply interpreting it
as a spectrogram. Therefore, by generating the corresponding sound,
we have embedded our image in a spectrogram.


%package doc
Summary: Documentation for %{pypi_name}
BuildArch: noarch

%description doc
This package contains documentation (in HTML format)
for the %{pypi_name} program.


%prep
%autosetup -p1
sed -e 's/\b__RPM_PACKAGE_VERSION__\b/%{version}/g' -i setup.cfg


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

cd docs/
make man
make html


%install
%pyproject_install
%pyproject_save_files -l %{name}

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 build/sphinx/man/%{name}.1 %{buildroot}%{_mandir}/man1/


%files -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%files doc
%doc build/sphinx/html/*


%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.9.3-16
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 0.9.3-13
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.3-11
- Fix python package metadata containing no version information

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Python Maint <python-maint@redhat.com> - 0.9.3-9
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.3-6
- Add Patch0: remove max version constraint on pyscaffold dependency (fixes rhbz#1981726)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.3-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.3-2
- Build docs with Sphinx and install them

* Tue May 05 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.3-1
- Initial packaging
