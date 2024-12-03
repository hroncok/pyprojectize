%global         github_name linux-cli-community
%global         srcname protonvpn_cli

Name:           protonvpn-cli
Version:        2.2.12
Release:        4%{?dist}
Summary:        Linux command-line client for ProtonVPN written in Python

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/Rafficer/%{github_name}
Source:         %{url}/archive/v%{version}/%{github_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  python3-devel

Requires:       openvpn
%if 0%{?fedora} || 0%{?.el8}
Recommends:     dialog
Recommends:     NetworkManager-openvpn
Suggests:       NetworkManager-openvpn-gnome
%else
Requires:       dialog
%endif

%description
The official Linux CLI for ProtonVPN.

ProtonVPN-CLI is a full rewrite of the bash protonvpn-cli in Python, which adds
more features and functionality with the purpose of improving readability,
speed and reliability.

ProtonVPN-CLI features a DNS Leak Protection feature, which makes sure that
your online traffic uses ProtonVPN's DNS Servers. This prevents third parties
(like your ISP) from being able to see your DNS queries (and, therefore, your
browsing history).


%prep
%autosetup -n %{github_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/protonvpn


%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.12-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.12-2
- Rebuilt for Python 3.13

* Tue Feb 27 2024 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> - 2.2.12-1
- Update to latest upstream

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.11-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.11-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 24 2021 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.11-3
- Updated for new git source URL

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 18 2021 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.11-1
- Update to latest upstream

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.6-2
- Rebuilt for Python 3.10

* Tue Feb 16 2021 Alexandru Cheltuitor <acrandom@pm.me> - 2.2.6-1
- Enhancement: Properly specifies versioning when contacting Proton API

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.4-1
- Enhancement: Option to define API domain via config
- Enhancement: Improve wording on connection failure
- Bug fix: Error during connection when IPv6 is disabled system-wide
- Bug fix: Unable to change DNS in containers
- Bug fix: pgrep not working on some distros
- Bug fix: Failing to connect when choosing a server via dialog menu

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-8
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-7
- Approved package for official Fedora repositories
- Remove Requires handled by Python dependency generator (BZ #1809814)

* Fri Mar 27 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-6
- Remove python3-dialog as dependency (already Required automatically)

* Mon Mar 16 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-5
- Remove tags not used in Fedora packages
- Add missing dependencies tracked in upstream requirements.txt

* Tue Mar 03 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-4
- Adhere to Fedora Packaging Guidelines via fedora-review

* Wed Feb 26 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-1
- Update to latest upstream

* Mon Feb 3 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.1-1
- Update to latest upstream

* Wed Dec 25 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.0-1
- First protonvpn-cli package
