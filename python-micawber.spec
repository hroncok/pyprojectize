%global pypi_name micawber

Name:           python-%{pypi_name}
Version:        0.5.5
Release:        5%{?dist}
Summary:        a small library for extracting rich content from urls

License:        MIT
URL:            http://github.com/coleifer/micawber/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)

%description
A small library for extracting rich content from urls. what does it do?
-micawber supplies a few methods for retrieving rich metadata about a variety
of links, such as links to youtube videos. micawber also provides functions for
parsing blocks of text and html and replacing links to videos with rich
embedded --here is a quick example:.. code-block:: python import micawber load
up rules for...

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A small library for extracting rich content from urls. what does it do?
-micawber supplies a few methods for retrieving rich metadata about a variety
of links, such as links to youtube videos. micawber also provides functions for
parsing blocks of text and html and replacing links to videos with rich
embedded --here is a quick example:.. code-block:: python import micawber load
up rules for...


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%{__python3} runtests.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.5-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep  7 2023 José Matos <jamatos@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.5.4-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.4-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 José Matos <jamatos@fedoraproject.org> - 0.5.4-1
- update to 0.5.4

* Thu Jul  8 2021 José Matos <jamatos@fedoraproject.org> - 0.5.3-1
- update to 0.5.3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 José Matos <jamatos@fedoraproject.org> - 0.5.2-1
- update to 0.5.2
- reenable tests since the failure was dealt in this update

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.9

* Sun Mar 22 2020 José Matos <jamatos@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 José Matos <jamatos@fedoraproject.org> - 0.5.0-1
- update to 0.5.0

* Tue Jun 11 2019 José Matos <jamatos@fedoraproject.org> - 0.4.1-2
- Change the source url to standard path name (%%{pypi_source})

* Sun Jun  9 2019 José Matos <jamatos@fedoraproject.org> - 0.4.1-1
- update to 0.4.1

* Sat Sep  1 2018 José Matos <jamatos@fedoraproject.org> - 0.3.5-1
- Initial package.
