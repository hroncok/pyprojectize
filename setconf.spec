Name:           setconf
Version:        0.7.7 
Release:        16%{?dist}
Summary:        Utility for changing settings in configuration text files 

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://setconf.roboticoverlords.org/ 
Source0:        https://github.com/xyproto/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Patch#:       setconf-version-description.patch
Patch0:         setconf-0.7.6-rm_sb.patch
Patch2:         setconf-0.7.7-add_man.patch

BuildRequires:  python3-devel

BuildArch:      noarch

%description
Setconf is small utility that can be used for
changing settings in configuration text files. 

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
%pyproject_check_import

%{__python3} setconf.py --test
awk '/^..\/setconf.py/ { print "%{__python3} " $0; next } { print }' testcases/test.sh >testcases/py3_test.sh
chmod a+x testcases/py3_test.sh
cd testcases/ && ./py3_test.sh

%install
%pyproject_install
%pyproject_save_files -l %{name}

%files -f %{pyproject_files}
%doc README.md
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.7-16
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7.7-14
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7.7-11
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.7-8
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.7-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Jan Macku <jamacku@redhat.com> - 0.7.7-2
- Fix names of patches in spec
- Fix Patch1 to match the source

* Tue Jul 07 2020 Jan Macku <jamacku@redhat.com> - 0.7.7-1
- New release - setconf 0.7.7

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Jan Macku <jamacku@redhat.com> - 0.7.6-1 
- Init setconf package  
