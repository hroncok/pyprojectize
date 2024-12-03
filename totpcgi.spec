%global commit 21aa122b5b2f107939f696297d58fe3c16d3ac7b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global selinux_variants mls strict targeted

%global totpcgiuser     totpcgi
%global totpcgiprovuser totpcgiprov

%global fixfiles_dirs %{_localstatedir}/www/totpcgi %{_localstatedir}/www/totpcgi-provisioning %{_localstatedir}/lib/totpcgi %{_sysconfdir}/totpcgi

Name:       totpcgi
Version:    0.6.0
Release:    0.21.20190713git%{?dist}
Summary:    A centralized totp solution based on google-authenticator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://github.com/mricon/totp-cgi
Source0:    https://github.com/mricon/totp-cgi/archive/%{commit}/totp-cgi-%{shortcommit}.tar.gz

# Switch from python-crypto to python-cryptodome. 
# rhbz#2061849
Patch0:     totpcgi-switch-to-cryptodome.patch

BuildArch:  noarch

BuildRequires: checkpolicy, selinux-policy-devel, python3-devel

Requires:   httpd, mod_ssl
Requires:   python3-totpcgi = %{version}-%{release}


%description
A CGI/FCGI application to centralize google-authenticator deployments.


%package -n python3-totpcgi
Summary:    Python libraries required for totpcgi
Requires:   python3-bcrypt, python3-pyotp, python3-pycryptodomex, python3-passlib

%description -n python3-totpcgi
This package includes the Python libraries required for totpcgi and
totpcgi-provisioning.


%package provisioning
Summary:    CGI for Google Authenticator provisioning using totpcgi
Requires:   python3-totpcgi = %{version}-%{release}
Requires:   httpd, mod_ssl, python3-qrcode

%description provisioning
This package provides the CGI for provisioning Google Authenticator tokens
used by totpcgi.


%package selinux
Summary:    SELinux policies for totpcgi
Requires:   python3-%{name} = %{version}-%{release}
Requires:   selinux-policy >= %{_selinux_policy_version}
Requires(post):   /usr/sbin/semodule, /sbin/restorecon, /sbin/fixfiles
Requires(postun): /usr/sbin/semodule, /sbin/restorecon, /sbin/fixfiles

%description selinux
This package includes SELinux policy for totpcgi and totpcgi-provisioning.

%prep
%autosetup -n totp-cgi-%{commit} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
pushd selinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv totpcgi.pp totpcgi.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
popd


%install
%pyproject_install
%pyproject_save_files '*'

# Install config files
mkdir -p -m 0750  %{buildroot}%{_sysconfdir}/totpcgi
mkdir -p -m 0750 \
    %{buildroot}%{_sysconfdir}/totpcgi/totp \
    %{buildroot}%{_sysconfdir}/totpcgi/templates
install -m 0640 conf/*.conf %{buildroot}%{_sysconfdir}/totpcgi/
install -m 0640 conf/templates/*.html %{buildroot}%{_sysconfdir}/totpcgi/templates/

# Create the state directory
mkdir -p -m 0770 %{buildroot}%{_localstatedir}/lib/totpcgi

# Create the CGI dirs
mkdir -p -m 0751 \
    %{buildroot}%{_localstatedir}/www/totpcgi \
    %{buildroot}%{_localstatedir}/www/totpcgi-provisioning

# Install the web files
install -m 0550 cgi/totp.cgi \
    %{buildroot}%{_localstatedir}/www/totpcgi/index.cgi
install -m 0550 cgi/provisioning.cgi \
    %{buildroot}%{_localstatedir}/www/totpcgi-provisioning/index.cgi
install -m 0644 cgi/*.css \
    %{buildroot}%{_localstatedir}/www/totpcgi-provisioning/

# Install the httpd config files
mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
install -m 0644 contrib/vhost-totpcgi.conf \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/totpcgi.conf
install -m 0644 contrib/vhost-totpcgi-provisioning.conf \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/totpcgi-provisioning.conf

# Install totpprov script and manpage
mkdir -p -m 0755 %{buildroot}%{_bindir}
install -m 0755 contrib/totpprov.py %{buildroot}%{_bindir}/totpprov
mkdir -p -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 contrib/totpprov.1 %{buildroot}%{_mandir}/man1/

# Install SELinux files
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 selinux/totpcgi.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/totpcgi.pp
done
/usr/bin/hardlink -cv %{buildroot}%{_datadir}/selinux

# fix python shebangs
sed -i -e 's|/usr/bin/env python|/usr/bin/python3|' %{buildroot}/var/www/totpcgi/index.cgi
sed -i -e 's|/usr/bin/env python|/usr/bin/python3|' %{buildroot}/var/www/totpcgi-provisioning/index.cgi
sed -i -e 's|/usr/bin/env python|/usr/bin/python3|' %{buildroot}/usr/bin/totpprov

%check
%pyproject_check_import

%pre -n python3-totpcgi
# We always add both the totpcgi and totpcgi-provisioning user
/usr/sbin/useradd -c "Totpcgi user" \
    -M -s /sbin/nologin -d /var/lib/totpcgi %{totpcgiuser} 2> /dev/null || :
/usr/sbin/useradd -c "Totpcgi provisioning user" \
    -M -s /sbin/nologin -d /etc/totpcgi %{totpcgiprovuser} 2> /dev/null || :

# For some reason the labeling doesn't always happen correctly
# force it if fixfiles exists
%post
if [ -f /sbin/fixfiles ] ; then
  /sbin/fixfiles -R totpcgi restore || :
fi

# For some reason the labeling doesn't always happen correctly
# force it if fixfiles exists
%post provisioning
if [ -f /sbin/fixfiles ] ; then
  /sbin/fixfiles -R totpcgi-provisioning restore || :
fi
# make sure /var/lib/totpcgi is 0770 totpcgiprov:totpcgi
chown -R %{totpcgiprovuser}:%{totpcgiuser} %{_localstatedir}/lib/totpcgi || :
chmod 0770 %{_localstatedir}/lib/totpcgi || :
# make sure state files are accessible to provisioning
chmod 0660 %{_localstatedir}/lib/totpcgi/*.json >/dev/null 2>&1 || :

%post selinux
for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/totpcgi.pp &> /dev/null || :
done
/sbin/fixfiles restore %{fixfiles_dirs} || :

%postun selinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
    /usr/sbin/semodule -s ${selinuxvariant} -r totpcgi &> /dev/null || :
  done
  /sbin/fixfiles restore %{fixfiles_dirs} || :
fi


%files
%doc README.rst INSTALL.rst
%doc contrib
%doc cgi/totp.fcgi
%dir %attr(-, %{totpcgiuser}, %{totpcgiuser}) %{_localstatedir}/www/totpcgi
%attr(-, %{totpcgiuser}, %{totpcgiuser}) %{_localstatedir}/www/totpcgi/*.cgi
%config(noreplace) %attr(-, -, %{totpcgiuser}) %{_sysconfdir}/totpcgi/totpcgi.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/totpcgi.conf
%attr(-, %{totpcgiprovuser}, %{totpcgiuser}) %{_localstatedir}/lib/totpcgi

%files -n python3-totpcgi -f %{pyproject_files}
%doc COPYING
%dir %attr(-, %{totpcgiprovuser}, %{totpcgiuser}) %{_sysconfdir}/totpcgi
%dir %attr(-, %{totpcgiprovuser}, %{totpcgiuser}) %{_sysconfdir}/totpcgi/totp
%config(noreplace) %attr(-, -, %{totpcgiprovuser}) %{_sysconfdir}/totpcgi/provisioning.conf
%{_bindir}/*
%{_mandir}/*/*

%files provisioning
%dir %attr(-, %{totpcgiprovuser}, %{totpcgiprovuser}) %{_localstatedir}/www/totpcgi-provisioning
%attr(-, %{totpcgiprovuser}, %{totpcgiprovuser}) %{_localstatedir}/www/totpcgi-provisioning/*.cgi
%config(noreplace) %{_localstatedir}/www/totpcgi-provisioning/*.css
%config(noreplace) %{_sysconfdir}/httpd/conf.d/totpcgi-provisioning.conf
%dir %attr(-, -, %{totpcgiprovuser}) %{_sysconfdir}/totpcgi/templates
%config(noreplace) %attr(-, -, %{totpcgiprovuser}) %{_sysconfdir}/totpcgi/templates/*.html

%files selinux
%doc selinux/*.{fc,if,sh,te}
%{_datadir}/selinux/*/totpcgi.pp


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.0-0.21.20190713git
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.20.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.0-0.19.20190713git
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.18.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.17.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.6.0-0.16.20190713git
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.15.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.14.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.6.0-0.13.20190713git
- Rebuilt for Python 3.11

* Mon Mar 14 2022 Kevin Fenzi <kevin@scrye.com> - 0.6.0-0.12.20190713git
- Switch dependency on python3-crypto to python3-pycryptodomex. Fixes rhbz#2061849

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.11.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.10.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-0.9.20190713git
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.8.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.7.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-0.6.20190713git
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.5.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-0.4.20190713git
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-0.3.20190713git
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.2.20190713git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Kevin Fenzi <kevin@scrye.com> - 0.6.0-0.1-20190713git
- Update to git head as of 20190713. 0.6.0 pre release.

* Sat Jun 22 2019 Kevin Fenzi <kevin@scrye.com> - 0.5.5-20
- Fix further FTBFS bugs. Fixes #1676151

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-18
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 21 2018 Kevin Fenzi <kevin@scrye.com> - 0.5.5-17
- Fix FTBFS bug #1606539

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.5-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 24 2017 Kevin Fenzi <kevin@scrye.com> - 0.5.5-13
- Drop dep on policyhelp. Fixes bug #1528774

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.5-12
- Python 2 binary package renamed to python2-totpcgi
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.5.5-11
- Switch to python-bcrypt, BZ 1473018.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Kevin Fenzi <kevin@scrye.com> - 0.5.5-7
- Fix define vs global

* Wed Aug 05 2015 Kevin Fenzi <kevin@scrye.com> 0.5.5-6
- Apply patch for selinux policy changes. 
- Fixes bug #1249121

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 13 2014 Till Maas <opensource@till.name> - 0.5.5-4
- Update selinux policy, adjust types and other call

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May  7 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.5-2
- Use %%_selinux_policy_version macro for totpcgi-selinux dependency
  (as defined in /usr/lib/rpm/macros.d/macros.selinux-policy) to fix
  invalid dependency on file:///usr/share/doc/selinux-policy/html/index.html

* Fri Sep 20 2013 Konstantin Ryabitsev <mricon@kernel.org> - 0.5.5-1
- Upstream 0.5.5 with new features.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.5.4-1
- Upstream 0.5.4 with security fixes.

* Wed Nov 28 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.5.3-2
- Minor fixes for fedora-review (RHBZ #880863)

* Tue Nov 27 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.5.3-1
- Release 0.5.3 with minor fixes.

* Mon Nov 26 2012 Andrew Grimberg <agrimberg@linuxfoundation.org> - 0.5.2-2
- Move the user adds for totpcgi & totpcgiprov to python-totpcgi package

* Mon Nov 19 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.5.2-1
- Release 0.5.2 with a fix for a potential replay attack in case the
  pincode was submitted with a typo (issue #12)

* Fri Jun 29 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.5.1-1
- Release 0.5.1 with trust_http_auth functionality.

* Wed May 30 2012 Andrew Grimberg <agrimberg@linuxfoundation.org> - 0.5.0-2
- Reorder the package dependencies slightly
- Add in post scripts for totpcgi & totpcgi-provisioning for SE labeling

* Wed May 30 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.5.0-2
- Use a manual fixfiles list, as we have more than one package

* Thu May 24 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.5.0-1
- Split into more packages: totpcgi, python-totpcgi, totpcgi-provisioning, totpcgi-selinux

* Tue May 08 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.4.0-1
- Update to 0.4.0, which adds encrypted-secret functionality.
- Require python-crypto and python-passlib

* Fri May 04 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.1-3
- Package SELinux using Fedora's guidelines.
- Add contrib dir in its entirety.
- Use config(noreplace).

* Tue May 01 2012 Andrew Grimberg <agrimberg@linuxfoundation.org> - 0.3.1-2
- Exceptions on bad passwords to LDAP
- Config for CA cert to use for verification
- PostgreSQL pincode & secrets backends

* Thu Apr 12 2012 Andrew Grimberg <agrimberg@linuxfoundation.org> - 0.3.0-1
- Bump version number
- Split backend system

* Wed Apr 11 2012 Andrew Grimberg <agrimberg@linuxfoundation.org> - 0.2.0-4
- Add in pincode.py script

* Mon Mar 26 2012 Andrew Grimberg <agrimberg@linuxfoundation.org> - 0.2.0-3
- Fix path perms for /var/www/totpcgi so that apache can chdir
- Reduce perms on /var/www/totpcgi/totp.cgi to bare minimum

* Fri Mar 23 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.2.0-2
- Update to better match Fedora's spec standards.

* Wed Mar 21 2012 Andrew Grimberg <agrimberg@linuxfoundation.org> - 0.2.0-1
- Initial spec file creation and packaging
