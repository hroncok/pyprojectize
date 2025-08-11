%global summary Parsing and querying distribution metadata stored in text/YAML files
%global desc\
distroinfo is a python module for parsing, validating and querying\
distribution/packaging metadata stored in human readable and review-able\
text/YAML files.\
\
distroinfo is a generic (re)implementation of rdoinfo parser which proved\
well suited for the task of interfacing with distribution metadata in a human\
friendly way. If you consider code reviews human friendly, that is.\

Name:             python-distroinfo
Version:          0.6.2
Release:          8%{?dist}
Summary:          %{summary}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              https://github.com/softwarefactory-project/distroinfo
Source0:          https://pypi.io/packages/source/d/distroinfo/distroinfo-%{version}.tar.gz
BuildArch:        noarch

%description %desc


%package -n python3-distroinfo
Summary:          %{summary}
Requires:         git-core
Requires:         python3-pbr
Requires:         python3-PyYAML
Requires:         python3-requests
Requires:         python3-six
BuildRequires:    python3-devel
BuildRequires:    python3-pbr
# for %%check tests
BuildRequires:    git-core
BuildRequires:    python3-pytest-runner
BuildRequires:    python3-requests
BuildRequires:    python3-PyYAML
BuildRequires:    python3-six

%description -n python3-distroinfo %{desc}

%prep
%setup -q -n distroinfo-%{version}

# let RPM handle the requirements
rm -f {test-,}requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
%pyproject_check_import
%{__python3} setup.py test

%install
%pyproject_install
%pyproject_save_files -l distroinfo

%files -n python3-distroinfo -f %{pyproject_files}
%doc README.rst AUTHORS


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.2-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.2-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.2-2
- Rebuilt for Python 3.12

* Thu Mar 09 2023 Karolina Kula <kkula@redhat.com> - 0.6.2-1
* Update to version 0.6.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Javier Peña <jpena@redhat.com> - 0.5.0-1
- Updated to version 0.5.0.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.10

* Wed Mar 03 2021 Javier Peña <jpena@redhat.com> - 0.4.0-1
- Updated to version 0.4.0.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Javier Peña <jpena@redhat.com> - 0.3.2-2
- The README file changed format to rst

* Thu Apr 16 2020 Javier Peña <jpena@redhat.com> - 0.3.2-1
- Updated to version 0.3.2.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Jakub Ružička <jruzicka@redhat.com> 0.3.0-2
- Remove python2-distroinfo subpackage.
- Clean up.

* Mon Feb 25 2019 Jakub Ružička <jruzicka@redhat.com> 0.3.0-1
- Update to 0.3.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jakub Ružička <jruzicka@redhat.com> 0.2.0-1
- Update to 0.2.0

* Wed Aug 15 2018 Jakub Ružička <jruzicka@redhat.com> 0.1.1-1
- Enable import of remote info files.
- Enable packages and releases inheritance.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-4
- Rebuilt for Python 3.7

* Wed May 30 2018 Jakub Ružička <jruzicka@redhat.com> 0.0.1-3
- Add missing Requires: git-core
- Make sure online tests are never run during build.

* Wed May 30 2018 Jakub Ruzicka <jruzicka@redhat.com> 0.0.1-2
- Use python2-six to comply with python packaging guidelines.
- Use macros for summary and description to prevent redundancy.

* Thu May 24 2018 Jakub Ruzicka <jruzicka@redhat.com> 0.0.1-1
- Initial version
