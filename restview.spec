%global pypi_name restview

Name:           %{pypi_name}
Version:        3.0.0
Release:        9%{?dist}
Summary:        ReStructuredText viewer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://mg.pov.lt/restview/
Source0:        %{pypi_source}

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  python3-readme-renderer
BuildRequires:  python3-pytest

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
A viewer for ReStructuredText documents that renders them on the fly. Pass
the name of a ReStructuredText document to restview, and it will launch a
web server on localhost:random-port and open a web browser. Every time you
reload the page, restview will reload the document from disk and render it.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A library for ReStructuredText documents that renders them.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%pytest -v src/restview/tests.py -k "not restview.tests.doctest_RestViewer_rest_to_html"

%files
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.0-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Update to latest upstream release 3.0.0 (closes rhbz#2114560)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.9.2-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Miro Hrončok <mhroncok@redhat.com> - 2.9.2-8
- Use unittest.mock instead of deprecated mock

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.9.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9.2-2
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.2-1
- Initial package for Fedora
