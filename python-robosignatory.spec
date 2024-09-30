%global modname robosignatory
#%%global prerelease b1

Name:               python-robosignatory
Version:            0.8.2
Release:            6%{?prerelease}%{?dist}
Summary:            A Fedora Messaging consumer that automatically signs artifacts

License:            GPL-2.0-or-later
URL:                https://pagure.io/robosignatory/
Source0:            https://pagure.io/releases/robosignatory/robosignatory-%{version}%{?prerelease}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-fedora-messaging
BuildRequires:      python3-psutil
BuildRequires:      python3-boto3
BuildRequires:      python3-click
BuildRequires:      python3-koji
# Tests
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-cov

# https://bodhi.fedoraproject.org/updates/python-robosignatory-0.2.0-1.el7#comment-552652
#Requires:           sigul


%global _description\
A Fedora Messaging consumer that automatically signs artifacts.\
\
RoboSignatory is composed of multiple consumers:\
- TagSigner listens for tags into a specific koji tag, then signs the build and\
  moves it to a different koji tag.\
- AtomicSigner listens for messages about composed rpmostree trees and signs\
  those, optionally updating the tag.\
- CoreOSSigner listens for requests to sign CoreOS artefacts, downloads them\
  from AWS S3, signs them, and uploads the signature back to S3.\


%description %_description

%package -n python3-robosignatory
Summary: %summary
Requires:           python3-fedora-messaging
Requires:           koji
Requires:           rpmdevtools
# This is the default package
Provides:           robosignatory = %{version}-%{release}

%description -n python3-robosignatory %_description

%prep
%autosetup -p1 -n %{modname}-%{version}%{?prerelease}
# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%{__python3} -m pytest -v

%files -n python3-robosignatory -f %{pyproject_files}
%doc README.rst LICENSE
%{_bindir}/robosignatory


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.8.2-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 10 2023 Mattia Verga <mattia.verga@proton.me> - 0.8.2-2
- Migrated to SPDX license

* Thu Aug 24 2023 Aurelien Bompard <abompard@fedoraproject.org> - 0.8.2-1
- Version 0.8.2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 0.8.1-2
- Rebuilt for Python 3.12

* Thu Apr 27 2023 Aurelien Bompard <abompard@fedoraproject.org> - 0.8.1-1
- Version 0.8.1

* Thu Apr 27 2023 Aurelien Bompard <abompard@fedoraproject.org> - 0.8.0-1
- Version 0.8.0
- Drop patch (upstreamed)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 01 2022 Mattia Verga <mattia.verga@proton.me> - 0.7.0-8
- Fix tests with fedora-messaging 3.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.7.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.7.0-2
- Rebase to 0.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Aurelien Bompard <abompard@fedoraproject.org> - 0.6.7-1
- Version 0.6.7

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.6-2
- Rebuilt for Python 3.9

* Thu Apr 09 2020 Mattia Verga <mattia.verga@protonmail.com> - 0.6.6-1
- Version 0.6.6
- Add pytest-cov to BR to fix build failure

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Aurelien Bompard <abompard@fedoraproject.org> - 0.6.3-1
- Version 0.6.3

* Thu Sep 19 2019 Aurelien Bompard <abompard@fedoraproject.org> - 0.6.2-1
- Version 0.6.2

* Mon Sep 09 2019 Aurelien Bompard <abompard@fedoraproject.org> - 0.6.0-1
- Version 0.6.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.5.0-1
- Rebase to 0.5.0 final

* Tue Mar 06 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.5.0-0.0b1
- Rebase to beta 1

* Mon Mar 05 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.5.0-0.0.b0
- Rebase to 0.5.0b0

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.4.2-1
- Rebased to upstream 0.4.2

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.0-2
- Python 2 binary package renamed to python2-robosignatory
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Fri Aug 11 2017 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- new version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Ralph Bean <rbean@redhat.com> - 0.3.6-1
- new version

* Fri May 12 2017 Ralph Bean <rbean@redhat.com> - 0.3.5-1
- new version

* Thu May 11 2017 Ralph Bean <rbean@redhat.com> - 0.3.4-1
- new version

* Wed May 10 2017 Ralph Bean <rbean@redhat.com> - 0.3.3-1
- new version

* Thu May 04 2017 Ralph Bean <rbean@redhat.com> - 0.3.2-1
- new version

* Tue May 02 2017 Ralph Bean <rbean@redhat.com> - 0.3.1-1
- new version

* Mon Apr 24 2017 Ralph Bean <rbean@redhat.com> - 0.3.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Ralph Bean <rbean@redhat.com> - 0.2.0-2
- Remove Requires on sigul, which is only necessary for one helper plugin.

* Fri Jan 20 2017 Ralph Bean <rbean@redhat.com> - 0.2.0-1
- new version

* Sun Dec 11 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.1.1-4
- Testing

* Sun Dec 11 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.1.1-3
- Testing

* Sun Dec 11 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.1.1-2
- Add patch to support krb5

* Mon Oct 31 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.1.1-1
- Release 0.1.1

* Mon Oct 31 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.1.0-1
- Release 0.1.0

* Mon Oct 17 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.0.7-1
- New upstream 0.0.7

* Mon Oct 17 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.0.6-1
- Various fixes to 0.0.5

* Mon Oct 17 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.0.5-1
- New upstream release

* Mon Oct 17 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.0.4-1
- New upstream release

* Mon Oct 17 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.0.3-2
- New 0.0.3 sources

* Mon Oct 17 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.0.3-1
- New upstream release

* Sun Sep 11 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.0.2-1
- New upstream release

* Sat Sep 10 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.0.1-1
- Initial packaging

