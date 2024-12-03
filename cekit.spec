%global modname cekit
%global _description \
CEKit helps to build container images from image definition files

Name:           %{modname}
Version:        4.12.0
Release:        3%{?dist}
Summary:        Container image creation tool
License:        MIT
URL:            https://cekit.io
Source0:        https://github.com/cekit/cekit/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

Requires:       git

%if 0%{?rhel} && 0%{?rhel} < 8
%global click python36-click
%global jinja python36-jinja2
%global pyyaml python36-PyYAML
%else
%global click python3-click
%global jinja python3-jinja2
%global pyyaml python3-pyyaml

BuildRequires:  python3-colorlog

Requires:       python3-colorlog

%endif

BuildRequires:  python3-devel
BuildRequires:  python3-pykwalify
BuildRequires:  %{pyyaml}
BuildRequires:  %{jinja}

Requires:       %{jinja}
Requires:       python3-setuptools
Requires:       python3-pykwalify
Requires:       %{pyyaml}
Requires:       %{click}
Requires:       python3-packaging

%if 0%{?fedora}
Suggests:       python3-docker
Suggests:       python3-docker-squash
Suggests:       docker
%endif

%description %_description

%package -n %{modname}-bash-completion
Summary:        %{summary}
Requires:       bash-completion
%description -n %{modname}-bash-completion %_description

Bash completion.

%package -n %{modname}-zsh-completion
Summary:        %{summary}
Requires:       zsh
%description -n %{modname}-zsh-completion %_description

ZSH completion.

%prep
%setup -q -n cekit-%{version}

%if 0%{?rhel} && 0%{?rhel} < 8
# Remove version requirement for packaging
sed -i 's/^packaging.*$/packaging/' requirements.txt
# Remove requirement for odcs
sed -i 's/^odcs.*$//' requirements.txt
# Remove requirement for colorlog
sed -i 's/^colorlog.*$//' requirements.txt
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
cp support/completion/bash/cekit %{buildroot}/%{_sysconfdir}/bash_completion.d/cekit

mkdir -p %{buildroot}/%{_datadir}/zsh/site-functions
cp support/completion/zsh/_cekit %{buildroot}/%{_datadir}/zsh/site-functions/_cekit

%pyproject_install
%pyproject_save_files -l cekit

%check
%pyproject_check_import

%files -n %{modname}-bash-completion
%doc README.rst
%license LICENSE
%{_sysconfdir}/bash_completion.d/cekit

%files -n %{modname}-zsh-completion
%doc README.rst
%license LICENSE
%{_datadir}/zsh/site-functions/_cekit

%files -n %{modname} -f %{pyproject_files}
%doc README.rst


%{_bindir}/cekit
%{_bindir}/cekit-cache

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.12.0-2
- Rebuilt for Python 3.13

* Thu May 16 2024 Nick Cross <ncross@redhat.com> - 4.12.0-1
- Release 4.12.0

* Fri Mar 08 2024 Nick Cross <ncross@redhat.com> - 4.11.0-1
- Release 4.11.0

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Nick Cross <ncross@redhat.com> - 4.10.0-1
- Release 4.10.0

* Thu Sep 07 2023 Nick Cross <ncross@redhat.com> - 4.9.1-1
- Release 4.9.1

* Thu Sep 07 2023 Nick Cross <ncross@redhat.com> - 4.9.0-1
- Release 4.9.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 4.8.0-2
- Rebuilt for Python 3.12

* Mon Jun 05 2023 Nick Cross <ncross@redhat.com> - 4.8.0-1
- Release 4.8.0

* Fri May 19 2023 Nick Cross <ncross@redhat.com> - 4.7.0-1
- Release 4.7.0

* Fri Mar 17 2023 Nick Cross <ncross@redhat.com> - 4.6.0-1
- Release 4.6.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Nick Cross <ncross@redhat.com> - 4.5.0-1
- Release 4.5.0

* Mon Oct 31 2022 Nick Cross <ncross@redhat.com> - 4.4.0-1
- Release 4.4.0

* Wed Aug 03 2022 Nick Cross <ncross@redhat.com> - 4.3.0-1
- Release 4.3.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Nick Cross <ncross@redhat.com> - 4.2.0-1
- Release 4.2.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.11

* Wed Mar 30 2022 Nick Cross <ncross@redhat.com> - 4.1.0-1
- Release 4.1.0

* Thu Mar 10 2022 Nick Cross <ncross@redhat.com> - 4.0.0-1
- Release 4.0.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 01 2021 Marek Goldmann <mgoldman@redhat.com> - 3.12.0-1
- Release 3.12.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.9.0-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Marek Goldmann <mgoldman@redhat.com> - 3.9.0-1
- Release 3.9.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 12:38:02 CET 2021 Marek Goldmann <mgoldman@redhat.com> - 3.8.0-1
- Release 3.8.0

* Wed Jul 29 2020 Marek Goldmann <mgoldman@redhat.com> - 3.7.0-1
- Release 3.7.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Marek Goldmann <mgoldman@redhat.com> - 3.6.0-1
- Release 3.6.0

* Thu Sep 19 2019 Marek Goldmann <mgoldman@redhat.com> - 3.5.0-1
- Release 3.5.0

* Mon Sep 02 2019 Marek Goldmann <mgoldman@redhat.com> - 3.4.0-2
- Specify proper R/BR for PyYAML

* Thu Aug 22 2019 Marek Goldmann <mgoldman@redhat.com> - 3.4.0-1
- Release 3.4.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Marek Goldmann <mgoldman@redhat.com> - 3.3.1-1
- Release 3.3.1

* Wed Jun 26 2019 Marek Goldmann <mgoldman@redhat.com> - 3.2.0-1
- Release 3.2.0

* Mon Jun 03 2019 Marek Goldmann <mgoldman@redhat.com> - 3.1.0-1
- Release 3.1.0

* Tue Apr 30 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.1-1
- Release 3.0.1

* Wed Apr 17 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-1
- Release 3.0.0

* Mon Apr 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.7.20190408git45cab46
- Updated revision to 45cab46

* Fri Mar 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.6.20190308git6318d73
- Rebuild

* Fri Mar 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.5.20190308git6318d73
- Rebuild

* Fri Mar 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.4.20190308git6318d73
- Updated revision to 6318d73

* Fri Mar 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.3.20190308git4f12391
- Updated revision to 4f12391

* Mon Feb 18 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.2.20190214git91cb6c1
- Update to commit dcb561650f177a800208c89e62d029d5ed9cc912
- Added support for RHEL 8 in coditionals
- Fixed Release
- Updated Source

* Thu Feb 14 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.1.20190214gitec3a0b
- Initial packaging
