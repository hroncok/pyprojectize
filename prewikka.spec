Name:           prewikka
Version:        5.2.0
Release:        19%{?dist}
Summary:        Graphical front-end analysis console for IDMEF
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.prelude-siem.org/
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Patch0:         prewikka-5.2.0-fix_python_3.10.patch

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-configargparse
BuildRequires:  python3-babel
BuildRequires:  python3-lesscpy

Requires:       python3-%{name} >= %{version}

# Since mass rebuild, debugpackage wont works for prewikka
%define debug_package %{nil}

%description
Prewikka is the backend of the web browser interface of Prelude SIEM. Providing
numerous features, Prewikka facilitates the work of users and analysts. It
provides alert aggregation and heartbeat views, and has user customization and
configurable filters. Prewikka also provides access to external tools such as
whois and traceroute.

%package -n python3-%{name}
Summary:        Graphical front-end analysis console for IDMEF
Requires:       %{name} = %{version}-%{release}
Requires:       python3-prelude >= %{version}
Requires:       python3-preludedb >= %{version}
Requires:       python3-babel
Requires:       python3-croniter
Requires:       python3-dateutil
Requires:       python3-gevent
Requires:       python3-lark-parser
Requires:       python3-mako
Requires:       python3-passlib
Requires:       python3-pytz
Requires:       python3-pyyaml
Requires:       python3-requests
Requires:       python3-voluptuous
Requires:       python3-werkzeug
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Prewikka is the backend of the web browser interface of Prelude SIEM. Providing
numerous features, Prewikka facilitates the work of users and analysts. It
provides alert aggregation and heartbeat views, and has user customization and
configurable filters. Prewikka also provides access to external tools such as
whois and traceroute.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
install -d -m 0755 %{buildroot}%{_sbindir}

# We have to use this because py3_install do other things and siteconfig.py
# will be not installed
%{__python3} setup.py install --root=%{buildroot}
mv %{buildroot}%{_bindir}/%{name}-httpd %{buildroot}%{_sbindir}/%{name}-httpd-%{python3_version}
mv %{buildroot}%{_bindir}/%{name}-crontab %{buildroot}%{_sbindir}/%{name}-crontab-%{python3_version}
mv %{buildroot}%{_bindir}/%{name}-cli %{buildroot}%{_sbindir}/%{name}-cli-%{python3_version}

ln -s ./%{name}-httpd-%{python3_version} %{buildroot}%{_sbindir}/%{name}-httpd-3
ln -s ./%{name}-httpd-3 %{buildroot}%{_sbindir}/%{name}-httpd
ln -s ./%{name}-crontab-%{python3_version} %{buildroot}%{_sbindir}/%{name}-crontab-3
ln -s ./%{name}-crontab-3 %{buildroot}%{_sbindir}/%{name}-crontab
ln -s ./%{name}-cli-%{python3_version} %{buildroot}%{_sbindir}/%{name}-cli-3
ln -s ./%{name}-cli-3 %{buildroot}%{_sbindir}/%{name}-cli

rm -f %{buildroot}%{_sysconfdir}/%{name}/*-dist

## Language files; not under /usr/share/locale, need to move them
install -d -m 0755 %{buildroot}%{_datadir}/locale
cp -r %{buildroot}%{python3_sitelib}/%{name}/locale/* %{buildroot}%{_datadir}/locale/
rm -rf %{buildroot}%{python3_sitelib}/%{name}/locale
ln -s %{_datadir}/locale %{buildroot}%{python3_sitelib}/%{name}/locale

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/menu.yml
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/auth.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/external_app.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/logs.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/riskoverview.conf
%{_datadir}/%{name}

%files -n python3-%{name}
%{_sbindir}/%{name}-httpd
%{_sbindir}/%{name}-httpd-3
%{_sbindir}/%{name}-httpd-%{python3_version}
%{_sbindir}/%{name}-crontab
%{_sbindir}/%{name}-crontab-3
%{_sbindir}/%{name}-crontab-%{python3_version}
%{_sbindir}/%{name}-cli
%{_sbindir}/%{name}-cli-3
%{_sbindir}/%{name}-cli-%{python3_version}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.dist-info

%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 5.2.0-19
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.2.0-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.2.0-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.2.0-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 14 2021 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-8
- Add missing fix for Python 3.10

* Fri Aug 13 2021 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-7
- Add support for Python 3.10

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.2.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-3
- Add missing dependency

* Thu Oct 15 2020 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-2
- Add missing dependency

* Thu Sep 17 2020 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-1
- Bump version 5.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.1.1-1
- Bump version 5.1.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.0.2-2
- Add missing dependencie

* Sun Jul 14 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.0.2-1
- Bump version 5.0.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.5-2
- Rebuilt for Python 3.7

* Wed Apr 25 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.1.5-1
- Bump version 4.1.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.0.0-1
- Bump version 4.0.0

* Thu Aug 10 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-4
- Temporary disable debugsource since Mass rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-1
- Bump version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1:1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed May 12 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0-1
- new upstream release

* Fri Feb 12 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0rc3-1
- new upstream release

* Wed Feb 10 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0rc2-1
- new upstream release

* Sat Jan 30 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0rc1-1
- new upstream release

* Tue Sep 29 2009 Steve Grubb <sgrubb@redhat.com> 0.9.17.1-1
- new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Steve Grubb <sgrubb@redhat.com> 0.9.17-1
- new upstream release

* Wed Jun 17 2009 Steve Grubb <sgrubb@redhat.com> 0.9.15-1
- new upstream release

* Fri Apr 17 2009 Steve Grubb <sgrubb@redhat.com> 0.9.14-4
- Change default perms on conf file

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.14-2
- Rebuild for Python 2.6

* Thu Apr 24 2008 Steve Grubb <sgrubb@redhat.com> 0.9.14-1
- new upstream release

* Mon Jan 14 2008 Steve Grubb <sgrubb@redhat.com> 0.9.13-1
- new upstream version 0.9.13

* Sun Apr  8 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.10-1
- moved to upstream version 0.9.10

* Fri Jan 12 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.8-1
- moved to upstream version 0.9.8

* Thu Jan 11 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.7.1-5
- changed docs handling
- fixed python settings

* Mon Jan 01 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.7.1-4
- corrected perms on python files 
- moved prewikka-httpd to /sbin
- added README.fedora

* Mon Nov 20 2006 Thorsten Scherf <tscherf@redhat.com> 0.9.7.1-3
- disabled dependency-generator 

* Mon Nov 20 2006 Thorsten Scherf <tscherf@redhat.com> 0.9.7.1-2
- Some minor fixes in requirements

* Sat Nov 06 2004 Thorsten Scherf <tscherf@redhat.com> 0.9.7.1-1
- test build for fc6
