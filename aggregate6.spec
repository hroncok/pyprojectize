Summary:        Tool to compress an unsorted list of IPv4 and IPv6 prefixes
Name:           aggregate6
Version:        1.0.12
Release:        6%{?dist}
License:        BSD-2-Clause
URL:            https://github.com/job/aggregate6
Source0:        https://github.com/job/aggregate6/archive/%{version}/%{name}-%{version}.tar.gz
# Don't require Python nose and mock
Patch0:         https://github.com/job/aggregate6/commit/b9571547316cf3d5b2f440d68f9f3fc99040dc0d.patch#/aggregate6-1.0.12-deprecated.patch
BuildRequires:  python%{python3_pkgversion}-devel
# Tests
BuildRequires:  python%{python3_pkgversion}-pytest
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-%{name} = %{version}-%{release}

%description
The aggregate6 tool takes a list of IPv4/IPv6 prefixes in conventional
format on STDIN, and performs two optimisations to attempt to reduce
the length of the prefix list, which can often be useful in context of
compressing firewall rules or BGP prefix-list filters.

%package -n python%{python3_pkgversion}-%{name}
Summary:        Python module to compress an unsorted list of IPv4 and IPv6 prefixes
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:  python%{python3_pkgversion}-py-radix >= 0.10.0
%endif

%description -n python%{python3_pkgversion}-%{name}
The aggregate6 Python module takes a list of IPv4/IPv6 prefixes in
conventional format as parameter, and performs two optimisations to
attempt to reduce the length of the prefix list, which can often be
useful in context of compressing firewall rules or BGP prefix-list
filters.

%prep
%autosetup -p1

%if 0%{?fedora} || 0%{?rhel} >= 9
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_wheel
%else
%py3_build
%endif

%install
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_install
%pyproject_save_files %{name}
%else
%py3_install
%{?el8:%py3_shebang_fix $RPM_BUILD_ROOT%{_bindir}/%{name}}
%endif

# Correct man page installation path
install -D -p -m 0644 $RPM_BUILD_ROOT{%{_prefix}/man,%{_mandir}}/man7/%{name}.7
rm -rf $RPM_BUILD_ROOT%{_prefix}/man/

# Remove shebang from non-executable script
sed -e '1{\|^#![[:space:]]*/|d}' -i $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/%{name}.py
touch -c -r %{name}/%{name}.py $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/%{name}.py

%check
%pytest

%files
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man7/%{name}.7*

%if 0%{?fedora} || 0%{?rhel} >= 9
%files -n python%{python3_pkgversion}-%{name} -f %{pyproject_files}
%else
%files -n python%{python3_pkgversion}-%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}.dist-info/
%endif
%license LICENSE

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Python Maint <python-maint@redhat.com> - 1.0.12-5
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 08 2023 Robert Scheck <robert@fedoraproject.org> 1.0.12-2
- Changes to match the Fedora Packaging Guidelines

* Tue Oct 11 2022 Robert Scheck <robert@fedoraproject.org> 1.0.12-1
- Upgrade to 1.0.12 (#2133590)
- Initial spec file for Fedora and Red Hat Enterprise Linux
