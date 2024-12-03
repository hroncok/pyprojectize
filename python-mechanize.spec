%global srcname mechanize
%global sum Stateful programmatic web browsing

Name:           python-mechanize
Version:        0.4.10
Release:        %autorelease
Summary:        Stateful programmatic web browsing

# Automatically converted from old format: BSD or ZPLv2.1 - review is highly recommended.
License:        LicenseRef-Callaway-BSD OR ZPL-2.1
URL:            https://github.com/python-mechanize/
Source0:        https://github.com/python-mechanize/mechanize/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-html5lib
BuildRequires:  python3-twisted
BuildRequires:  python3-zope-interface

%description
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered: mechanize.Browser (stateful web browser),
mechanize.UserAgent (configurable URL opener), plus urllib2 handlers.

Features include: ftp:, http: and file: URL schemes, browser history,
high-level hyperlink and HTML form support, HTTP cookies, HTTP-EQUIV and
Refresh, Referer [sic] header, robots.txt, redirections, proxies, and
Basic and Digest HTTP authentication.  mechanize's response objects are
(lazily-) .seek()able and still work after .close().

Much of the code originally derived from Perl code by Gisle Aas
(libwww-perl), Johnny Lee (MSIE Cookie support) and last but not least
Andy Lester (WWW::Mechanize).  urllib2 was written by Jeremy Hylton.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered: mechanize.Browser (stateful web browser),
mechanize.UserAgent (configurable URL opener), plus urllib2 handlers.

Features include: ftp:, http: and file: URL schemes, browser history,
high-level hyperlink and HTML form support, HTTP cookies, HTTP-EQUIV and
Refresh, Referer [sic] header, robots.txt, redirections, proxies, and
Basic and Digest HTTP authentication.  mechanize's response objects are
(lazily-) .seek()able and still work after .close().

Much of the code originally derived from Perl code by Gisle Aas
(libwww-perl), Johnny Lee (MSIE Cookie support) and last but not least
Andy Lester (WWW::Mechanize).  urllib2 was written by Jeremy Hylton.

%prep
%autosetup -n %{srcname}-%{version} -p 1
chmod -x examples/forms/{echo.cgi,example.py,simple.py}
# Workaround for https://github.com/rpm-software-management/rpm/issues/2532:
rm -rf SPECPARTS

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mechanize

%check
%pyproject_check_import

chmod +x examples/forms/{echo.cgi,example.py,simple.py}
python3 run_tests.py
chmod -x examples/forms/{echo.cgi,example.py,simple.py}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst ChangeLog COPYRIGHT

%changelog
%autochangelog
