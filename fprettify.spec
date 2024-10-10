Name:           fprettify
Version:        0.3.7
Release:        12%{?dist}
Summary:        Auto-formatter for modern Fortran source code
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/pseewald/fprettify
Source0:        https://github.com/pseewald/fprettify/archive/refs/tags/v%{version}/fprettify-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(configargparse)

Requires:       python3-fprettify = %{version}-%{release}

# Patch out use of /usr/bin/env python
Patch0:         fprettify-0.3.7-pyenv.patch

%description
fprettify is an auto-formatter written in Python to impose strict
whitespace formatting for modern Fortran code.

%package -n     python3-fprettify
Summary:        Python library for fprettify

Requires:       python3dist(configargparse)
Requires:       python3dist(setuptools)

%description -n python3-fprettify
fprettify is an auto-formatter written in Python to impose strict
whitespace formatting for modern Fortran code.

This package contains the Python library.

%prep
%setup -q -n fprettify-%{version}
%patch -P0 -p1 -b .pyenv

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fprettify

%check
%{__python3} setup.py test

%files
%{_bindir}/fprettify

%files -n python3-fprettify -f %{pyproject_files}
%doc README.md

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.7-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.7-10
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.7-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.7-3
- Rebuilt for Python 3.11

* Wed May 25 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.7-2
- Patch out use of /usr/bin/env python.

* Fri Feb 04 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.7-1
- Initial package.
