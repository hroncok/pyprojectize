%global _description\
Nyx is a command-line monitor for Tor. With this you can get detailed\
real-time information about your relay such as bandwidth usage,\
connections, logs, and much more.

Name: nyx
Version: 2.1.0
Release: 22%{?dist}
Summary: Command-line monitor for Tor
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL: https://nyx.torproject.org
Source0: %{pypi_source}
# https://github.com/torproject/nyx/issues/49
Patch0: nyx-2.1.0-replace-inspect.getargspec-usage.patch
BuildArch: noarch
BuildRequires: python3-devel
# Tests
BuildRequires: python3-stem
BuildRequires: python3-pyflakes
Suggests: %{name}-doc = %{version}-%{release}
Provides: tor-arm = %{version}-%{release}
Obsoletes: tor-arm <= 1.4.5.0-17
Obsoletes: tor-arm-gui <= 1.4.5.0-17
Obsoletes: tor-arm-devel <= 1.4.5.0-17

%description %_description

%package doc
Summary: %summary

%description doc %_description

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}
install -D -m 0644 nyx.1 %{buildroot}%{_mandir}/man1/nyx.1

%check
%{__python3} run_tests.py

%files -f %{pyproject_files}
%{_bindir}/%{name}

%files doc
%license LICENSE
%doc web
%{_mandir}/man1/nyx.1*

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.1.0-20
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Python Maint <python-maint@redhat.com> - 2.1.0-16
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.0-13
- Patch usage of inspect.getargspec

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-12
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.0-9
- Add BR python3-setuptools

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-8
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.0-6
- Enable tests

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.0-1
- Version 2.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-4
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.4-2
- Add Obsoletes for all tor-arm subpackages

* Wed Nov 08 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.4-1
- Version 2.0.4

* Wed Jul 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.6-2.20170712git08eec6f
- Use Python3
- Doc subpackage

* Wed Jul 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.6-1.20170712git08eec6f
- First release of nyx
