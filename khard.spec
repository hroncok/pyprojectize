Name:           khard
Version:        0.19.1
Release:        4%{?dist}
Summary:        An address book for the Linux console

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/scheibler/%{name}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools_scm
Requires:       python3-atomicwrites
Requires:       python3-configobj
Requires:       python3-ruamel-yaml
Requires:       python3-unidecode
Requires:       python3-vobject

%description
Khard is an address book for the Linux console. It creates, reads, modifies and
removes carddav address book entries at your local machine.


%prep
%setup -q


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '*'
mkdir -p %{buildroot}%{_datadir}/khard/examples/
mkdir -p %{buildroot}%{_datadir}/khard/examples/davcontroller/
install -p -m 0644 misc/davcontroller/davcontroller.py %{buildroot}%{_datadir}/khard/examples/davcontroller/davcontroller.py
mkdir -p %{buildroot}%{_datadir}/khard/examples/sdiff/
install -p -m 0644 misc/sdiff/sdiff_khard_wrapper.sh %{buildroot}%{_datadir}/khard/examples/sdiff/sdiff_khard_wrapper.sh
install -p -d misc/twinkle %{buildroot}%{_datadir}/khard/examples/twinkle
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -p -m 0644 misc/zsh/_email-khard %{buildroot}%{_datadir}/zsh/site-functions/_khard
install -p -m 0644 misc/zsh/_khard %{buildroot}%{_datadir}/zsh/site-functions/_khard


%files -f %{pyproject_files}
%doc CHANGES README.md todo.txt
%license LICENSE
%{_bindir}/khard
%{_datadir}/khard/
%{_datadir}/zsh/site-functions/


%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.19.1-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.19.1-2
- Rebuilt for Python 3.13

* Thu May 30 2024 Ben Boeckel <fedora@me.benboeckel.net> - 0.19.1-1
- Update to 0.19.1
- Resolves #2152527

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.17.0-10
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.17.0-7
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.17.0-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Ben Boeckel <fedora@me.benboeckel.net> - 0.17.0-2
- use PyPI source tarball

* Sat Dec 19 2020 Ben Boeckel <fedora@me.benboeckel.net> - 0.17.0-1
- update to 0.17.0
- install other example data

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-11
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Sebastian Dyroff <sdyroff@fedoraproject.org> - 0.11.4-1
- update to 0.11.4 fixing #1473961

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11.3-2
- Rebuild for Python 3.6

* Sat Oct 08 2016 Ben Boeckel <mathstuf@gmail.com> - 0.11.3-1
- update to 0.11.3

* Tue Aug 02 2016 Ben Boeckel <mathstuf@gmail.com> - 0.11.1-2
- add BR on python3-pypandoc
- remove utf8-readme patch

* Tue Aug 02 2016 Ben Boeckel <mathstuf@gmail.com> - 0.11.1-1
- update to 0.11.1

* Sat Jul 23 2016 Ben Boeckel <mathstuf@gmail.com> - 0.11.0-1
- update to 0.11.0
- remove davcontroller (masked upstream due to python3 compat issues)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 23 2016 Ben Boeckel <mathstuf@gmail.com> - - 0.9.0-1
- update to 0.9.0

* Mon Apr 04 2016 Ben Boeckel <mathstuf@gmail.com> - 0.8.1-1
- update to 0.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 Ben Boeckel <mathstuf@gmail.com> - 0.6.3-1
- update to 0.6.3

* Tue Oct 13 2015 Ben Boeckel <mathstuf@gmail.com> - 0.6.2-1
- update to 0.6.2
- ship zsh completion file

* Sat Jul 25 2015 Ben Boeckel <mathstuf@gmail.com> - 0.4.1-1
- update to 0.4.1
- remove shebang lines

* Tue Mar 03 2015 Ben Boeckel <mathstuf@gmail.com> - 0.2.1-2
- use python2-devel in BR
- chmod +x davcontroller.py
- remove twinkle plugin (twinkle isn't in Fedora)

* Tue Mar 03 2015 Ben Boeckel <mathstuf@gmail.com> - 0.2.1-1
- initial package
