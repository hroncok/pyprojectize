%global	module	trml2pdf

Name:		python-%{module}
Version:	0.6
Release:	13%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2
Summary:	Easy creating PDF using ReportLab's RML
URL:		https://github.com/romanlv/trml2pdf
Source0:	https://github.com/romanlv/trml2pdf/archive/%{version}/%{module}-%{version}.tar.gz
# python3-devel
BuildRequires:	pkgconfig(python3)
# python3-six
BuildRequires:	%{py3_dist six} >= 1.9
# python3-reportlab
BuildRequires:	%{py3_dist reportlab} >= 3.2
Requires:	%{py3_dist reportlab} >= 3.2
BuildArch:	noarch

%description
Open source implementation of RML (Report Markup Language) from ReportLab

%package -n	python3-%{module}
Summary:	%{summary}
%py_provides python3-%{module}

%description -n	python3-%{module}
Open source implementation of RML (Report Markup Language) from ReportLab


%prep
%autosetup -n %{module}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{module}
%{__install} -Dp -m0644 doc/trml2pdf.1 %{buildroot}%{_mandir}/man1/trml2pdf.1


%check
%py3_build test


%files -n python3-%{module} -f %{pyproject_files}
%license doc/COPYRIGHT.txt
%doc README.md doc/CREDITS.md
%{_bindir}/%{module}
%{_mandir}/man1/trml2pdf.1.*

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.6-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.6-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon May 03 2021 TI_Eugene <ti.eugene@gmail.com> - 0.6-2
- py_provides typo fixed
- Source URL fixed

* Sun Jan 31 2021 TI_Eugene <ti.eugene@gmail.com> - 0.6-1
- Initial build
