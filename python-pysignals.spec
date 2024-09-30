%global srcname pysignals

Name: python-%{srcname}
Version: 0.1.4
Release: 6%{?dist}
Summary: PySignals is a signal dispatcher for Python

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Url: https://github.com/theojulienne/%{srcname}
Source0: https://github.com/theojulienne/%{srcname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires:  python3-devel

# required for check
BuildRequires: %{py3_dist six}

%global _description %{expand:
PySignals is a signal dispatcher for Python, extracted from “django.dispatch”
in the Django framework so it can be used in applications without requiring
the entire Django framework to be installed.
}

%description %_description

%package -n python3-%{srcname}

Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p 1 -n PySignals-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{python3} setup.py test

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt license.python.txt
%doc README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.4-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.4-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 29 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.4-1
- Release 0.1.4

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.1.3-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.3-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.3-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 05 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.3-1
- Release 0.1.3
- Point source url to most recent release on github, rather than pypi

* Thu Jun 18 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.2-3
- Update pysignals to latest django dispatch 1.9.13

* Wed Jun 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.2-2
- Add LICENSE.txt from upstream

* Wed Jun 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.2-1
- Initial package

