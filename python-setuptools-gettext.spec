Name:           python-setuptools-gettext
Version:        0.1.8
Release:        6%{?dist}
Summary:        Setuptools gettext extension plugin

License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/setuptools-gettext
Source0:        %{pypi_source setuptools-gettext}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Setuptools helpers for gettext. Compile .po files into .mo files.

%package -n     python3-setuptools-gettext
Summary:        %{summary}

%description -n python3-setuptools-gettext
Setuptools helpers for gettext. Compile .po files into .mo files.

%prep
%autosetup -n setuptools-gettext-%{version}
rm -rf ./setuptools_gettext.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files setuptools_gettext

%check
%py3_check_import setuptools_gettext

%files -n python3-setuptools-gettext -f %{pyproject_files}
%doc README.md
%license COPYING

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.8-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 5 2024 Björn Lindström <bkhl@elektrubadur.se> - 0.1.8-2
- Remove patching of setuptools dependency, no longer needed as setuptools in
  rawhide new enough.

* Fri Jan 5 2024 Björn Lindström <bkhl@elektrubadur.se> - 0.1.8-1
- Updated to 0.1.8.
- Removed patch for clarifying license, as that has now been done upstream.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.3-3
- Rebuilt for Python 3.12

* Thu May 4 2023 Björn Lindström <bkhl@elektrubadur.se> - 0.1.3-2
- Add missing dist tag in release number.

* Sat Apr 29 2023 Björn Lindström <bkhl@elektrubadur.se> - 0.1.3-1
- Initial package.
