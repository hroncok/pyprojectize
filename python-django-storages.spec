%global srcname django-storages

Name:           python-%{srcname}
Version:        1.11.1
Release:        15%{?dist}
Summary:        Support for many storage backends in Django

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jschneier/django-storages
Source:         %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

%package     -n python3-%{srcname}+azure
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+azure}
Provides:       python3dist(%{srcname}/azure) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/azure) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       (python%{python3_version}dist(azure-storage-blob) >= 1.3.1 with python%{python3_version}dist(azure-storage-blob) < 12.0.0)

%description -n python3-%{srcname}+azure %{_description}

"azure" extras. Python 3 version.

%package     -n python3-%{srcname}+boto3
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+boto3}
Provides:       python3dist(%{srcname}/boto3) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/boto3) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(boto3) >= 1.4.4

%description -n python3-%{srcname}+boto3 %{_description}

"boto3" extras.

%package     -n python3-%{srcname}+dropbox
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+dropbox}
Provides:       python3dist(%{srcname}/dropbox) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/dropbox) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(dropbox) >= 7.2.1

%description -n python3-%{srcname}+dropbox %{_description}

"dropbox" extras.

%package     -n python3-%{srcname}+google
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+google}
Provides:       python3dist(%{srcname}/google) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/google) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(google-cloud-storage) >= 1.15.0

%description -n python3-%{srcname}+google %{_description}

"google" extras.

%package     -n python3-%{srcname}+libcloud
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+libcloud}
Provides:       python3dist(%{srcname}/libcloud) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/libcloud) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(apache-libcloud)

%description -n python3-%{srcname}+libcloud %{_description}

"libcloud" extras.

%package     -n python3-%{srcname}+sftp
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+sftp}
Provides:       python3dist(%{srcname}/sftp) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/sftp) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(paramiko)

%description -n python3-%{srcname}+sftp %{_description}

"sftp" extras.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

# Tests require too many dependencies
#%%check
#export DJANGO_SETTINGS_MODULE=tests.settings
#%%python3 -m pytest -v tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/storages/
%{python3_sitelib}/django_storages-*.egg-info/

# Missing requirement azure-storage-blob
#%%files -n python3-%%{srcname}+azure
#%%{?python_extras_subpkg:%%ghost %%{python3_sitelib}/django_storages-*.egg-info}

%files -n python3-%{srcname}+boto3
%{?python_extras_subpkg:%ghost %{python3_sitelib}/django_storages-*.egg-info}

%files -n python3-%{srcname}+dropbox
%{?python_extras_subpkg:%ghost %{python3_sitelib}/django_storages-*.egg-info}

# Missing requirement google-cloud-storage
#%%files -n python3-%%{srcname}+google
#%%{?python_extras_subpkg:%%ghost %%{python3_sitelib}/django_storages-*.egg-info}

%files -n python3-%{srcname}+libcloud
%{?python_extras_subpkg:%ghost %{python3_sitelib}/django_storages-*.egg-info}

%files -n python3-%{srcname}+sftp
%{?python_extras_subpkg:%ghost %{python3_sitelib}/django_storages-*.egg-info}

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.11.1-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.11.1-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.11.1-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.11.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.11.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.1-1
- Update to latest upstream release 1.10.1

* Thu Aug 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.1-1
- Update to latest upstream release 1.9.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8-3
- Add metadata for Python extras subpackages

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.8-1
- Initial package
