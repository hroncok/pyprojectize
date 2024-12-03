%global srcname openidc-client
%global pkgname openidc_client

%global commit 0e2ed814497fd850a76c875123a0b0cdfd12ee70
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0.6.0
Release:        24.20220119git%{shortcommit}%{?dist}
Summary:        Python OpenID Connect client with token caching and management

License:        MIT
URL:            https://github.com/puiterwijk/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/puiterwijk/python-openidc-client/pull/10
# Fully fix support for server not sending refresh token
Patch0:         0001-feat-really-support-not-receiving-refresh-token.patch

BuildArch:      noarch

%description
%{summary}.

%package     -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-requests
Requires:       python3-requests

%description -n python3-%{srcname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{name}-%{commit} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pkgname}

%check
%pyproject_check_import

%{__python3} setup.py test

%files -n python3-openidc-client -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-24.20220119git0e2ed81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.0-23.20220119git0e2ed81
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-22.20220119git0e2ed81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-21.20220119git0e2ed81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-20.20220119git0e2ed81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.0-19.20220119git0e2ed81
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-18.20220119git0e2ed81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-17.20220119git0e2ed81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Adam Williamson <awilliam@redhat.com> - 0.6.0-16.20220119git0e2ed81
- Update to newer git snapshot with fix for not receiving refresh token
- Backport PR #10 to completely fix not receiving refresh token

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.0-15.20180605gitcd8d91c
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-14.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 0.6.0-12.20180605gitcd8d91c
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-9.20180605gitcd8d91c
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-7.20180605gitcd8d91c
- Subpackage python2-openidc-client has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-6.20180605gitcd8d91c
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2.20180605gitcd8d91c
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.6.0-1.20180605gitcd8d91c
- Rebase to 0.6.0

* Sat Mar 24 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.5.0-1.20180324git188c560
- Fixes python3 compatibility
- Rebase to 0.5.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2.20171113git54dee6e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Mohan Boddu <mboddu@bhujji.com> - 0.4.0-1.20171113git54dee6e
- Add Requests AuthBase wrapper
- Allow specifying to not get new tokens in auther

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20170523git77cb3ee
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Mohan Boddu <mboddu@bhujji.com> - 0-3.20170523git77cb3ee
- Following the upstream release numbers
- Allow providing HTTP method
- Make refresh_token also update the cache

* Mon Mar 27 2017 Mohan Boddu <mboddu@bhujji.com> - 0-3.20170327git5456800
- Changed the version number to use date
- Using package name in URL

* Fri Mar 24 2017 Mohan Boddu <mboddu@bhujji.com> - 0-2.git5456800
- Skip tests on setup.py install
- Adding Requires on python{2,3}-requests
- Adding %py{2,3}_build macros
- Adding %py{2,3}_install macros

* Mon Mar 20 2017 Mohan Boddu <mboddu@bhujji.com> - 0-1
- Initial packaging of python-openidc-client
