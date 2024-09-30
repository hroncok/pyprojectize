%bcond_without tests

%global pretty_name snaptime
%global commit          cc8b7d4489ee8104b717ed461dd21aee806ae322
%global snapshotdate    20210420
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global _description %{expand:
The snaptime package is about transforming timestamps simply.}

Name:           python-%{pretty_name}
Version:        0.2.4
Release:        18%{?dist}
Summary:        Transforming timestamps simply

License:        MIT
URL:            https://github.com/zartstrom/snaptime
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%endif

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pretty_name}-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pretty_name}

%check
#skipping three tests
%if %{with tests}
k="${k-}${k+ and }not test_bad_weekday"
k="${k-}${k+ and }not test_parse_error"
k="${k-}${k+ and }not test_unit_error"
%pytest -k "${k-}"
%endif

%files -n python3-%{pretty_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.4-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.2.4-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 1 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-11
- Break long line

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.4-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-6
- Switch to pytest macro

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.4-5
- Rebuilt for Python 3.10

* Tue Apr 20 15:11:26 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.4-4
- Target a specific commit instead of the master git tip

* Wed Mar 17 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-3
- Cosmetic changes

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-1
- Initial package
