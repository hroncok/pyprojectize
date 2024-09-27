Name: jc
Summary: Serialize the output of CLI tools and file-types to structured JSON
License: MIT

Version: 1.25.3
Release: 4%{?dist}

URL: https://github.com/kellyjonbrazil/%{name}
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

# Backport upstream commits that fix test failures under Python 3.13.
# Minor changes made to make the patches apply cleanly to v1.25.3.
#
# Based on:
# - https://github.com/kellyjonbrazil/jc/commit/9eb4df34b190c57d020b70153ef3faa8984c02ca.patch
# - https://github.com/kellyjonbrazil/jc/commit/71af0c55553e17c598c9f43b8271bfb069795af5.patch
Patch0: 0000-python-3.13.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(pygments) >= 2.4.2
BuildRequires: python3dist(ruamel-yaml) >= 0.15
BuildRequires: python3dist(xmltodict) >= 0.12

# Require the python module in the main package
Requires: python3-%{name} = %{version}-%{release}


%description
JSON CLI output utility. JC is used to JSONify the output of many
command-line tools and file types for easier parsing in scripts.


%package -n python3-%{name}
Summary: Module for serializing output of CLI tools into JSON
BuildArch: noarch

%description -n python3-%{name}
Python module providing functions for parsing the output of command-line
tools and file types into structured JSON, for easier further processing.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -p man/jc.1 %{buildroot}%{_mandir}/man1/

COMPDIR="%{buildroot}%{_datadir}/bash-completion/completions"
install -m 755 -d "${COMPDIR}"
install -m 644 -p completions/jc_bash_completion.sh "${COMPDIR}/%{name}"


%check
TZ="America/Los_Angeles" ./runtests.sh


%files
%doc README.md EXAMPLES.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/*


%files -n python3-%{name}
%doc docs/
%license LICENSE.md
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.dist-info


%changelog
* Mon Sep 09 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.25.3-4
- Add patch to fix test failures under Python 3.13

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Python Maint <python-maint@redhat.com> - 1.25.3-2
- Rebuilt for Python 3.13

* Mon Jun 10 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.25.3-1
- Update to v1.25.3

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.25.2-2
- Rebuilt for Python 3.13

* Sat Mar 23 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.25.2-1
- Update to v1.25.2

* Tue Feb 13 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.25.1-1
- Update to v1.25.1

* Tue Feb 06 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.25.0-1
- Update to v1.25.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 17 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.24.0-1
- Update to v1.24.0

* Tue Oct 24 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.23.6-1
- Update to v1.23.6

* Sun Jul 30 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.23.4-1
- Update to v1.23.4

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 1.23.3-2
- Rebuilt for Python 3.12

* Sun Jun 25 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.23.3-1
- Update to v1.23.3

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.23.2-2
- Rebuilt for Python 3.12

* Mon May 01 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.23.2-1
- Update to v1.23.2

* Fri Mar 24 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.23.1-1
- Update to v1.23.1

* Tue Feb 28 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.23.0-1
- Update to v1.23.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.22.5-1
- Update to v1.22.5

* Fri Dec 30 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.22.4-1
- Update to v1.22.4

* Sat Dec 17 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.22.3-1
- Update to v1.22.3

* Wed Nov 09 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.22.2-1
- Update to v1.22.2

* Mon Oct 24 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.22.1-1
- Update to v1.22.1

* Tue Sep 27 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.22.0-1
- Update to v1.22.0

* Mon Aug 29 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.21.2-1
- Update to v1.21.2

* Mon Aug 29 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.21.1-1
- Update to v1.21.1

* Mon Aug 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.21.0-1
- Update to v1.21.0
- Ship the EXAMPLES.md file

* Sat Jul 23 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.20.4-1
- Update to v1.20.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.20.2-1
- Update to v1.20.2

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.20.1-2
- Rebuilt for Python 3.11

* Thu Jun 16 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.20.1-1
- Update to v1.20.1
- Generate & install a bash completion file

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.20.0-2
- Rebuilt for Python 3.11

* Tue May 31 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.20.0-1
- Update to v1.20.0

* Sat May 14 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.19.0-1
- Update to v1.19.0

* Wed Apr 27 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.18.8-1
- Update to v1.18.8

* Tue Apr 26 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.18.7-1
- Update to v1.18.7

* Sat Mar 26 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.18.6-1
- Update to v1.18.6

* Sun Mar 06 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.18.5-1
- Update to v1.18.5

* Mon Feb 14 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.18.3-1
- Update to v1.18.3

* Fri Jan 28 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.18.2-1
- Update to v1.18.2

* Mon Jan 24 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.18.1-1
- Update to v1.18.1
- Separate package into CLI executable and python module

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.17.7-1
- Update to v1.17.7

* Mon Jan 03 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.17.6-1
- Update to v1.17.6

* Tue Dec 21 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.17.5-1
- Update to v1.17.5
- Use PEP-503 names for package dependencies

* Thu Dec 09 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.17.4-1
- Update to v1.17.4

* Fri Dec 03 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.17.3-1
- Update to v1.17.3

* Thu Nov 18 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.17.2-1
- Update to v1.17.2

* Tue Nov 02 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.17.1-1
- Update to v1.17.1

* Mon Sep 27 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.17.0-1
- Update to v1.17.0

* Tue Aug 31 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.16.2-1
- Update to v1.16.2

* Mon Aug 16 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.16.1-1
- Update to v1.16.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.16.0-1
- Update to v1.16.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.15.5-2
- Rebuilt for Python 3.10

* Fri May 28 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.15.5-1
- Update to v1.15.5

* Wed May 19 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.15.4-1
- Update to v1.15.4

* Tue Apr 27 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.15.3-1
- Update to v1.15.3

* Mon Apr 19 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.15.2-1
- Update to v1.15.2

* Wed Apr 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.15.1-1
- Update to v1.15.1

* Thu Apr 08 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.15.0-1
- Update to v1.15.0
- Include man page in the package

* Sat Mar 06 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.14.4-1
- Update to v1.14.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 02 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.14.0-1
- Update to v1.14.0

* Fri Aug 14 2020 Artur Iwicki <fedora@svgames.pl> - 1.13.4-1
- Update to upstream release v1.13.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Artur Iwicki <fedora@svgames.pl> - 1.11.2-3
- Switch to using only the GitHub source
- Formatting changes

* Fri Jun 05 2020 Artur Iwicki <fedora@svgames.pl> - 1.11.2-2
- Fetch the GitHub sources apart from PyPi sources
  (the latter don't contain documentation and tests)
- Run tests during %%check
- Include the docs in the package

* Tue Jun 02 2020 Kelly Brazil <kellyjonbrazil@gmail.com> - 1.11.2-1
- Initial package.
