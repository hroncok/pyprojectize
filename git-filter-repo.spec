%global gitexecdir %{_libexecdir}/git-core

Name:           git-filter-repo
Version:        2.38.0
Release:        8%{?dist}
Summary:        Quickly rewrite git repository history (git-filter-branch replacement)
License:        GPL-2.0-only OR MIT
Group:          Development/Tools/Version Control
Url:            https://github.com/newren/git-filter-repo
#
Source0:        https://github.com/newren/git-filter-repo/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         https://github.com/newren/git-filter-repo/pull/526.patch#/%{name}-support-git-2_43.diff
# Some expected packed sizes in this test are off by two
Patch1:         %{name}-fix-t9390-t41.diff
#
BuildArch:      noarch
#
BuildRequires:  git-core >= 2.26.0
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
# test deps
BuildRequires:  perl-interpreter
BuildRequires:  rsync
#
Requires:       git-core >= 2.26.0

%description
git filter-repo is a versatile tool for rewriting history, which includes
capabilities not found anywhere else. It roughly falls into the same space of
tool as git filter-branch but without the capitulation-inducing poor
performance, with far more capabilities, and with a design that scales
usability-wise beyond trivial rewriting cases.

%prep
%autosetup -p1

# Remove shebang from the python module to avoid rpmlint warnings
# (this is a symlink, but sed -i will break it, conveniently for us)
sed -i '1,2d' git_filter_repo.py

# Change shebang in all relevant files in this directory and all subdirectories
find -type f -exec sed -i '1s=^#!%{_bindir}/\(python\|env python\)[23]\?=#!%{_bindir}/python3=' {} +

# Fix shebang print_my_version(); it affects the --version output
sed -Ei "s=#!/usr/bin/env python3=#!%{_bindir}/python3=" %{name} git_filter_repo.py

# Create setup.{cfg,py} to ensure we have egg-info for generating dependencies
sed -e '/^setup_requires = setuptools_scm$/d' release/setup.cfg >setup.cfg

cat <<'EOF' >setup.py
from setuptools import setup
setup(name="%{name}", version="%{version}",
      entry_points={'console_scripts': ['%{name} = git_filter_repo:main']})
EOF

# Fix links to git docs since we don't install git-filter-repo.html into the
# git htmldir
sed -Ei 's,(a href=")(git),\1%{_docdir}/git/\2,g' Documentation/html/git-filter-repo.html

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install}
%pyproject_save_files -l git_filter_repo

install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 Documentation/man1/git-filter-repo.1 %{buildroot}%{_mandir}/man1/git-filter-repo.1

%check
%pyproject_check_import
t/run_tests

%files -f %{pyproject_files}
%doc README.md Documentation/*.md Documentation/html/*.html contrib/filter-repo-demos
%{gitexecdir}/git-filter-repo
%{_mandir}/man1/git-filter-repo.1*

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.38.0-7
- Rebuilt for Python 3.13

* Wed Mar 13 2024 Michel Lind <salimma@fedoraproject.org> - 2.38.0-6
- Apply PR#526 to support Git 2.43.0
- Fix one test where some expected packed sizes are off by two bytes
- Resolves: rhbz#2261155

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.38.0-2
- Rebuilt for Python 3.12

* Sun Mar 05 2023 Andreas Schneider <asn@redhat.com> - 2.38.0-1
- Update to version 2.38.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.34.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 23 2022 Todd Zullinger <tmz@pobox.com> - 2.34.0-5
- improve python provides
- require git-core rather than git
- include additional documentation
- run the test suite

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.34.0-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Andreas Schneider <asn@redhat.com> - 2.34.0-1
- Update to version 2.34.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.29.0-3
- Rebuilt for Python 3.10

* Mon Mar 15 2021 Andreas Schneider <asn@redhat.com> - 0.29.0-1
- Update to version 2.29.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Andreas Schneider <asn@redhat.com> - 2.28.0-1
- Update to version 2.28.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Andreas Schneider <asn@redhat.com> - 2.27.0-1
- Update to version 2.27.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.25.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Andreas Schneider <asn@redhat.com> - 2.25.0-4
- Add missing BR for python3-rpm-macros

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Andreas Schneider <asn@redhat.com> - 2.25.0-1
- Update to version 2.25.0
- Fix installation to python3 sitelib

* Fri Dec 20 2019 Andreas Schneider <asn@redhat.com> - 2.24.0-2
- Fixed source tarball permissions
- Fixed souperfluous space in Summary

* Thu Dec 19 2019 Andreas Schneider <asn@redhat.com> - 2.24.0-1
- Initial version 2.24.0
