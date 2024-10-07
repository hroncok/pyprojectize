%global modname vpoller
%global sum     Distributed vSphere API Proxy

Name:           python-%{modname}
Version:        0.7.3
Release:        25%{?dist}
Summary:        %{sum}

# setup.py mentions BSD license
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/dnaeon/py-%{modname}
# hint: pypi misses several files but github provides
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# TypeError: option values must be strings with Python 3.8 #273 
Patch0:         %{url}/commit/f24774dabd757f2dcdb5f27902de526cc5ff30b9.patch

BuildArch:      noarch

%global _description \
vPoller is a distributed vSphere API Proxy,\
designed for discovering and polling of vSphere objects.\
\
It uses the vSphere API in order to perform discovery\
and polling of vSphere objects.\
\
vPoller uses the ZeroMQ messaging library for distributing\
tasks to workers and load balancing of client requests.\
\
vPoller can be integrated with other systems, which require\
access to vSphere objects, but do not have native support\
for it.\
\
Possible scenarios where vPoller could be used is integration\
with monitoring systems as part of the discovery and polling\
process in order to provide monitoring of your vSphere\
environment.

%description
%{_description}

%package     -n python%{python3_pkgversion}-%{modname}
Summary:        %{sum}
BuildRequires: make
BuildRequires:  python%{python3_pkgversion}-devel
#BuildRequires: %%{py3_dist docopt zmq vconnector pyvmomi sphinx}
BuildRequires:  python%{python3_pkgversion}-docopt
BuildRequires:  python%{python3_pkgversion}-zmq
BuildRequires:  python%{python3_pkgversion}-vconnector
BuildRequires:  python%{python3_pkgversion}-pyvmomi
# no magic dependencies in epel
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-pyvmomi
Requires:       python%{python3_pkgversion}-vconnector
Requires:       python%{python3_pkgversion}-zmq
Requires:       python%{python3_pkgversion}-docopt
%endif

%description -n python%{python3_pkgversion}-%{modname}
%{_description}

%package     -n %{modname}
Summary:        Executable binaries for %{sum}
BuildRequires:  help2man
Requires:       python%{python3_pkgversion}-%{modname}

%description -n %{modname}
%{_description}
This pacakge installs the executable binaries.

%package        doc
Summary:        Documentation files for %{sum}
BuildRequires:  python%{python3_pkgversion}-sphinx

%description    doc
%{_description}
This pacakge installs several documentation files.

%prep
%autosetup -p1 -npy-%{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
export PYTHONPATH=../src
sed -i -r \
 -e 's:(SPHINXBUILD.*=).*:\1 %{_bindir}/sphinx-build-%{python3_version}:' \
 -e 's:SPHINXOPTS.*=:\0 %{_smp_mflags} :' \
 docs/Makefile
%make_build -C docs html
rm -rf docs/_build/html/.{doctrees,buildinfo}
# wrong-script-interpreter
grep -rl "/usr/bin/env" | xargs chmod 0644
grep -rl "/usr/bin/env" | xargs sed -i "s|#!/usr/bin/env |/usr/bin/|"

%install
%pyproject_install
%pyproject_save_files -l %{modname}
# manpages
pushd %{buildroot}
install -d .%{_mandir}/man1
for suffix in client proxy worker ; do
PYTHONPATH=.%{python3_sitelib} help2man --no-discard-stderr \
 -o .%{_mandir}/man1/%{modname}-${suffix}.1 .%{_bindir}/%{modname}-${suffix}
done
popd


%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc README.rst AUTHORS.txt

%files -n %{modname}
%license LICENSE
%{_bindir}/%{modname}-*
%{_mandir}/man1/%{modname}-*.1*

%files doc
%license LICENSE
%doc docs/_build/html/
%doc extra/


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.3-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.7.3-23
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.7.3-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.3-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Raphael Groner <raphgro@fedoraproject.org> - 0.7.3-11
- add patch for python 3.8

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-7
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.3-6
- drop brand

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Raphael Groner <raphgro@fedoraproject.org> - 0.7.3-4
- exclude contrib folder due to not useful in Fedora

* Sun May 19 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.3-3
- use concrete python3 version and path for sphinx-build

* Sun Apr 14 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.3-2
- split subpackages for doc and bin
- move BR into subpackages

* Wed Apr 10 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.3-1
- new version
- drop upstreamed license patch
- generate manpages
- fix rpmlint

* Sat Jan 26 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.1-1
- initial
