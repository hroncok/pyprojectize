%global pypi_name pypubsub
%global src_name Pypubsub

Name:           python-%{pypi_name}
Version:        4.0.3
Release:        23%{?dist}
Summary:        Python Publish-Subscribe Package

License:        BSD-2-Clause
URL:            https://github.com/schollii/pypubsub
Source0:        https://github.com/schollii/%{pypi_name}/archive/v%{version}.tar.gz#/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
PyPubSub provides a publish - subscribe API that facilitates the development of
event-based / message-based applications. PyPubSub supports sending and
receiving messages between objects of an application. It is centered on the
notion of a topic; senders publish messages of a given topic, and listeners
subscribe to messages of a given topic. The package also supports a variety of
advanced features that facilitate debugging and maintaining pypubsub topics and
messages in larger applications.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
PyPubSub provides a publish - subscribe API that facilitates the development of
event-based / message-based applications. PyPubSub supports sending and
receiving messages between objects of an application. It is centered on the
notion of a topic; senders publish messages of a given topic, and listeners
subscribe to messages of a given topic. The package also supports a variety of
advanced features that facilitate debugging and maintaining pypubsub topics and
messages in larger applications.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '%{src_name}*' pubsub

%check
%pyproject_check_import

pushd tests/suite
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 py.test-%{python3_version}
popd


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst src/pubsub/RELEASE_NOTES.txt
%license src/pubsub/LICENSE_BSD_Simple.txt

%changelog
* Thu Aug 01 2024 Scott Talbert <swt@techie.net> - 4.0.3-23
- Update License tag to use SPDX identifiers

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.0.3-21
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.0.3-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0.3-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.3-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Scott Talbert <swt@techie.net> - 4.0.3-8
- Add missing BR for setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Scott Talbert <swt@techie.net> - 4.0.3-1
- New upstream release 4.0.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 6 2018 Scott Talbert <swt@techie.net> - 4.0.0-1
- Initial package.
