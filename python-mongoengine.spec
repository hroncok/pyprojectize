%global pkgname mongoengine
%global sum A Python Document-Object Mapper for working with MongoDB
%global desc MongoEngine is a Document-Object Mapper (think ORM, \
but for document databases) for working with MongoDB \
from Python. It uses a simple declarative API, similar \
to the Django ORM.
 
 
Name: python-mongoengine
Version: 0.29.1
Release: 1%{?dist}
BuildArch: noarch
 
License: MIT
Summary: %{sum}
URL:     http://mongoengine.org/
Source0: %{pypi_source %pkgname}
# pymongo and pymongo-gridfs is needed for the docs
BuildRequires: python3-pymongo
BuildRequires: python3-pymongo-gridfs
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-devel
BuildRequires: make
 
 
%description
%{desc}
 
 
%package -n python3-%{pkgname}
Summary: %{sum}
Recommends: python3-blinker
Recommends: python3-pillow
Requires: python3-pymongo
Requires: python3-pymongo-gridfs
 
 
%description -n python3-%{pkgname}
%{desc}
 
 
%package doc
Summary: Documentation for %{name}
BuildArch: noarch
 
 
%description doc
Documentation for %{name}.
 
 
%prep
%setup -q -n %{pkgname}-%{version}
find . -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'
# Avoid build dependency on readthedocs-sphinx-ext
sed -Ei 's/(, )?"readthedocs_ext\.readthedocs"//' docs/conf.py
 
 
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
PYTHONPATH=$(pwd) make -C docs SPHINXBUILD=sphinx-build-3 html
rm -f docs/_build/html/.buildinfo
# Don't ship fonts
rm -rf docs/_build/html/_static/font
 
 
%install
%pyproject_install
%pyproject_save_files -l %{pkgname}
 
%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.rst
 
 
%files doc
%license LICENSE
%doc docs/_build/html
 
 
%changelog
* Thu Sep 19 2024 Sandro Mani <manisandro@gmail.com> - 0.29.1-1
- Update to 0.29.1

* Tue Aug 27 2024 Sandro Mani <manisandro@gmail.com> - 0.29.0-1
- Update to 0.29.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.28.2-2
- Rebuilt for Python 3.13

* Fri Mar 08 2024 Sandro Mani <manisandro@gmail.com> - 0.28.2-1
- Update to 0.28.2

* Tue Mar 05 2024 Sandro Mani <manisandro@gmail.com> - 0.28.1-1
- Update to 0.28.1

* Mon Mar 04 2024 Sandro Mani <manisandro@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.27.0-2
- Rebuilt for Python 3.12

* Tue Mar 07 2023 Sandro Mani <manisandro@gmail.com> - 0.27.0-1
- Update to 0.27.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.24.0-3
- Rebuilt for Python 3.11

* Wed Apr 13 2022 Miro Hrončok <mhroncok@redhat.com> - 0.24.0-2
- Avoid build dependency on readthedocs-sphinx-ext

* Mon Feb 21 2022 Eduardo Echeverria <echevemaster@gmail.com> - 0.24.0-1
- Bunped to the latest upstream version 

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.23.0-2
- Rebuilt for Python 3.10

* Sat Apr 3 2021 Eduardo Echeverria <echevemaster@gmail.com> - 0.23.0-1
- Initial packaging

