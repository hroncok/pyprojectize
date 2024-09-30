%global pypi_name django-pipeline

Name:           python-%{pypi_name}
Version:        1.6.8
Release:        28%{?dist}
Summary:        An asset packaging library for Django

License:        MIT
URL:            https://github.com/jazzband/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Pipeline is an asset packaging library for Django, providing both CSS
and JavaScript concatenation and compression, built-in JavaScript template
support, and optional data-URI image and font embedding

%package -n python3-%{pypi_name}
Summary:        Packaging library for Django - Python 3 version
BuildRequires:  python3-devel

Requires:       python3-django

Obsoletes: python-%{pypi_name} < 1.6.8-5
Obsoletes: python2-%{pypi_name} < 1.6.8-5


%description -n python3-%{pypi_name}
Pipeline is an asset packaging library for Django, providing both CSS
and JavaScript concatenation and compression, built-in JavaScript template
support, and optional data-URI image and font embedding.
This package provides Python 3 build of %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pipeline
# Remove the "tests" subdirectory to avoid it polluting the main python
# namespace:
rm -rf %{buildroot}%{python3_sitelib}/tests
%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6.8-27
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.8-23
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.8-20
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.8-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.8-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.8-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.8-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.8-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Matthias Runge <mrunge@redhat.com> - 1.6.8-5
- drop Python2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.8-2
- Rebuild for Python 3.6

* Fri Jul 29 2016 Jan Beran <jberan@redhat.com> - 1.6.8-1
- update to version 1.6.8
- url and source update
- modernized specfile with Python 3 packaging

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.24-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Stephen Gallagher <sgallagh@redhat.com> 1.3.24-1
- Upgrade to latest upstream release 1.3.24
- Changelog: https://pypi.python.org/pypi/django-pipeline/

* Thu Apr 03 2014 Stephen Gallagher <sgallagh@redhat.com> 1.3.23-1
- Upgrade to latest upstream release 1.3.23
- Changelog: https://pypi.python.org/pypi/django-pipeline/

* Wed Jan 22 2014 Stephen Gallagher <sgallagh@redhat.com> - 1.3.20-2
- Upgrade to latest upstream release 1.3.20
- Changelog: https://pypi.python.org/pypi/django-pipeline/

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.2.24-2
- Bumping release for rebuild

* Mon Jan 28 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.2.24-1
- Upgrade to latest upstream release 1.2.24
- Fix yui/yuglify settings overriding each other
- Separate yuglify compressor from YUI compressor
- Improve HTML compression middleware
- Better compressor error messages
- Improve installation documentation
- Fix packaging metadata
- Add documentation about non-packing storage

* Thu Dec 13 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.2.21-1
- Upgrade to latest upstream release 1.2.21

* Wed Oct 03 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.2.17-1
- Upgrade to latest upstream release
- Support for more compressors:
-   SlimIt
-   Closure
-   CSSTidy
-   cssmin

* Mon Aug 06 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-3
- Initial release
- Add django_pipeline to Fedora to support Review Board 1.7

