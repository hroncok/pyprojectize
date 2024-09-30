%global pypi_name aenum

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        12%{?dist}
Summary:        Advanced Enumerations, NamedTuples and NamedConstants for Python

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.org/project/aenum/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
aenum includes a Python stdlib Enum-compatible data type, as well as a
metaclass-based NamedTuple implementation and a NamedConstant class.

An Enum is a set of symbolic names (members) bound to unique, constant values.
Within an enumeration, the members can be compared by identity, and the
enumeration itself can be iterated over. Support exists for unique values,
multiple values, auto-numbering, and suspension of aliasing, plus the ability
to have values automatically bound to attributes.

A NamedTuple is a class-based, fixed-length tuple with a name for each
possible position accessible using attribute-access notation as well as
the standard index notation.

A NamedConstant is a class whose members cannot be rebound; it lacks all other
Enum capabilities, however.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
aenum includes a Python stdlib Enum-compatible data type, as well as a
metaclass-based NamedTuple implementation and a NamedConstant class.

An Enum is a set of symbolic names (members) bound to unique, constant values.
Within an enumeration, the members can be compared by identity, and the
enumeration itself can be iterated over. Support exists for unique values,
multiple values, auto-numbering, and suspension of aliasing, plus the ability
to have values automatically bound to attributes.

A NamedTuple is a class-based, fixed-length tuple with a name for each
possible position accessible using attribute-access notation as well as
the standard index notation.

A NamedConstant is a class whose members cannot be rebound; it lacks all other
Enum capabilities, however.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# https://github.com/ethanfurman/aenum/issues/7
# PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} %{pypi_name}/test.py

%files -n python3-%{pypi_name}
%doc README aenum/doc aenum/CHANGES
%license aenum/LICENSE
%{python3_sitelib}/*.dist-info
%{python3_sitelib}/%{pypi_name}/

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.0-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.1.0-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.1.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 24 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- Disable tests due to issue with py3.10

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.10

* Mon Feb 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Update to latest upstream release 3.0.0 (#1920220)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.6-1
- Update to latest upstream release 2.2.6 (#1911533)

* Wed Dec 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.4-1
- Update to latest upstream release 2.2.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.3-2
- Update to latest upstream release 2.2.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.4-1
- Switch to PyPI for the source to get rid of the BitBucket shortcomings
- Update to latest upstream release 2.1.4

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-1
- Update to latest upstream release 2.1.3
- Add license and docs (rhbz#1714003)

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Initial package for Fedora
