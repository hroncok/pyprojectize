Name:           stratis-cli
Version:        3.6.2
Release:        4%{?dist}
Summary:        Command-line tool for interacting with the Stratis daemon

License:        Apache-2.0
URL:            https://github.com/stratis-storage/stratis-cli
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{_bindir}/a2x
%if 0%{?rhel}
BuildRequires:  python3-dateutil
BuildRequires:  python3-dbus-client-gen
BuildRequires:  python3-dbus-python-client-gen
BuildRequires:  python3-justbytes
BuildRequires:  python3-packaging
BuildRequires:  python3-psutil
BuildRequires:  python3-wcwidth
%endif

# Require the version of stratisd that supports a compatible D-Bus interface
Requires:       (stratisd >= 3.6.0 with stratisd < 4.0.0)

# Exclude the same arches for stratis-cli as are excluded for stratisd
ExclusiveArch:  %{rust_arches} noarch
%if 0%{?rhel}
ExcludeArch:    i686
%endif
BuildArch:      noarch

%description
stratis provides a command-line interface (CLI) for
interacting with the Stratis daemon, stratisd. stratis
interacts with stratisd via D-Bus.

%prep
%autosetup

%build
%py3_build
a2x -f manpage docs/stratis.txt

%install
%py3_install
# Do not install tab-completion files for RHEL
%if !0%{?rhel}
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  shell-completion/bash/stratis
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  shell-completion/zsh/_stratis
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  shell-completion/fish/stratis.fish
%endif
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man8 docs/stratis.8

%files
%license LICENSE
%doc README.rst
%{_bindir}/stratis
%{_mandir}/man8/stratis.8*
%if !0%{?rhel}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/stratis
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_stratis
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/stratis.fish
%endif
%{python3_sitelib}/stratis_cli/
%{python3_sitelib}/stratis_cli-*.egg-info/

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.6.2-3
- Rebuilt for Python 3.13

* Mon May 13 2024 mulhern <amulhern@redhat.com> - 3.6.2-2
- Add a generic gating.yaml file

* Mon Apr 22 2024 Bryan Gurney <bgurney@redhat.com> - 3.6.2-1
- Update to 3.6.2

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 25 2023 Bryan Gurney <bgurney@redhat.com> - 3.6.0-2
- Use testing tag v3.6.0

* Tue Oct 24 2023 Bryan Gurney <bgurney@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.5.3-3
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Bryan Gurney <bgurney@redhat.com> - 3.5.3-2
- Use tmt tests

* Wed Jun 07 2023 Bryan Gurney <bgurney@redhat.com> - 3.5.3-1
- Update to 3.5.3

* Wed May 17 2023 Bryan Gurney <bgurney@redhat.com> - 3.5.2-1
- Update to 3.5.2

* Fri Mar 31 2023 Bryan Gurney <bgurney@redhat.com> - 3.5.1-1
- Update to 3.5.1

* Tue Jan 24 2023 Bryan Gurney <bgurney@redhat.com> - 3.5.0-1
- Update to 3.5.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Bryan Gurney <bgurney@redhat.com> - 3.4.1-1
- Update to 3.4.1

* Tue Nov 29 2022 Bryan Gurney <bgurney@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Tue Oct 18 2022 Bryan Gurney <bgurney@redhat.com> - 3.3.0-1
- Update to 3.3.0

* Sat Jul 30 2022 mulhern <amulhern@redhat.com> - 3.2.0-2
- Fix gating tests

* Sat Jul 30 2022 mulhern <amulhern@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.11

* Tue Jun 07 2022 Bryan Gurney <bgurney@redhat.com> - 3.1.0-2
- Add rpminspect.yaml file

* Wed May 25 2022 mulhern <amulhern@redhat.com> - 3.1.0-1
- Update to 3.1.0

* Wed Mar 30 2022 mulhern <amulhern@redhat.com> - 3.0.1-5
- Tidies for unification of spec file

* Sun Feb 27 2022 mulhern <amulhern@redhat.com> - 3.0.1-4
- Remove all gating files

* Sun Feb 27 2022 mulhern <amulhern@redhat.com> - 3.0.1-3
- Bump revision in order to include dependencies in gating tests

* Sun Feb 27 2022 mulhern <amulhern@redhat.com> - 3.0.1-2
- Add gating tests

* Sun Feb 13 2022 mulhern <amulhern@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 mulhern <amulhern@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Thu Aug 5 2021 mulhern <amulhern@redhat.com> - 2.4.4-1
- Update to 2.4.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 mulhern <amulhern@redhat.com> - 2.4.3-1
- Update to 2.4.3

* Tue Jun 15 2021 mulhern <amulhern@redhat.com> - 2.4.2-1
- Update to 2.4.2

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.1-2
- Rebuilt for Python 3.10

* Wed May 19 2021 mulhern <amulhern@redhat.com> - 2.4.1-1
- Update to 2.4.1

* Tue Apr 27 2021 mulhern <amulhern@redhat.com> - 2.4.0-1
- Update to 2.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 mulhern <amulhern@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Tue Nov 10 2020 mulhern <amulhern@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 mulhern <amulhern@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Thu Jul 9 2020 mulhern <amulhern@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sat Sep 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Sat Nov 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-3
- Make package archful

* Thu Sep 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-2
- Bump stratisd req

* Thu Sep 27 2018 Andy Grover <agrover@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Fri Aug 31 2018 Andy Grover <agrover@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Fri Aug 3 2018 Andy Grover <agrover@redhat.com> - 0.5.5-3
- Remove zsh completions subpackage
- Own completion directories

* Thu Aug 2 2018 Andy Grover <agrover@redhat.com> - 0.5.5-1
- Update to 0.5.5
- Add zsh completions subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-2
- Rebuilt for Python 3.7

* Mon Jun 4 2018 Andy Grover <agrover@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Tue May 1 2018 Andy Grover <agrover@redhat.com> - 0.5.2-1
- Update to 0.5.2

* Wed Apr 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-3
- Fix dependency on stratisd

* Tue Apr 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Relax stratisd dependency

* Thu Mar 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.5-3
- Enable usage of dependency generator

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.5-2
- Include manpage

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.5-1
- Initial package
