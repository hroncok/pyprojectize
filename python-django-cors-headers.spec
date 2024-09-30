%global srcname django-cors-headers

Name:           python-%{srcname}
Version:        3.7.0
Release:        13%{?dist}
Summary:        Django application for handling the server headers required for CORS

License:        MIT
URL:            https://github.com/adamchainz/django-cors-headers
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
A Django App that adds Cross-Origin Resource Sharing (CORS) headers
to responses. This allows in-browser requests to your Django application
from other origins.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vrf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files corsheaders

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst HISTORY.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.7.0-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.7.0-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.7.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.7.0-2
- Rebuilt for Python 3.10

* Fri Mar 26 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-7
- Rebuilt for Python 3.7

* Tue Mar 06 2018 Ralph Bean <rbean@redhat.com> - 2.0.2-6
- Make py3 package provide the old py2 name.

* Mon Mar 05 2018 Ralph Bean <rbean@redhat.com> - 2.0.2-5
- Disable python2 for https://fedoraproject.org/wiki/Changes/Django20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Ralph Bean <rbean@redhat.com> - 2.0.2-2
- Add missing doc and license declarations.

* Fri Feb 10 2017 Ralph Bean <rbean@redhat.com> - 2.0.2-1
- Latest upstream.

* Mon Jan 18 2016 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Initial packaging for Fedora.
