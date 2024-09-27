Name:           wfuzz
Version:        3.1.0
Release:        15%{?dist}
Summary:        Web fuzzer

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://wfuzz.io
Source0:        https://github.com/xmendez/wfuzz/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-netaddr

%description
Wfuzz has been created to facilitate the task in web applications assessments
and it is based on a simple concept: it replaces any reference to the FUZZ
keyword by the value of a given payload.

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-theme-alabaster

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup
rm -rf %{name}.egg-info
# Remove shebang
sed -i -e '/^#!\//, 1d' src/wfuzz/wfuzz.py
# Remove release pinning 
sed -i -e 's/pyparsing>=2.4\*/pyparsing>=2.4/g' setup.py
# We don't need this as we have the whole documentation
sed -i -e '/data_files/d' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wfencode
%{_bindir}/wfpayload
%{_bindir}/wfuzz
%{_bindir}/wxfuzz
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}.dist-info/

%files -n %{name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.0-15
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.1.0-13
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.1.0-10
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.0-7
- Rebuilt for pyparsing-3.0.9

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.0-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Update to new upstream release 3.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.5-4
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.5-3
- Fix changelog entries

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.5-2
- Create docs

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.5-1
- Initial package for Fedora
