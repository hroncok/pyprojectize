%global github_owner    gabrielfalcao
%global github_name     HTTPretty
%global srcname         httpretty

%if 0%{?fedora}
%global run_tests 1
%else
# missing deps in epel9
%global run_tests 0
%endif

Name:           python-httpretty
Version:        1.1.4
Release:        %autorelease
Summary:        HTTP request mock tool for Python

License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        %{pypi_source}
# Avoid unnecessary remote access requirement (note: test only actually
# does a remote connection after PR #313)
Patch1:         python-httpretty-fakesock_getpeercert_noconnect.patch
# Remote access (these tests were skipped upstream in <= 0.9.7)
Patch2:         skip-test_passthrough.patch
# Remove timeout, which causes some tests to fail in Koji
# 
# Fixes RHBZ#2046877
Patch3:         test_response-no-within.patch
# https://github.com/gabrielfalcao/HTTPretty/issues/457
Patch4:         test_handle_slashes.patch
# https://github.com/gabrielfalcao/HTTPretty/pull/479/files
# Fixes RHBZ#2261569
Patch5:         chunked_requests_handled_by_urllib3.patch  

BuildArch:      noarch

%global _description\
Once upon a time a python developer wanted to use a RESTful API, everything was\
fine but until the day he needed to test the code that hits the RESTful API:\
what if the API server is down? What if its content has changed?\
Don't worry, HTTPretty is here for you.

%description %_description

%package -n python3-httpretty
Summary:        HTTP request mock tool for Python 3
Requires:       python3-six

BuildRequires:  python3-devel
%if %{run_tests}
BuildRequires:  python3-httplib2
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-sure
BuildRequires:  python3-urllib3
BuildRequires:  python3-tornado
BuildRequires:  python3-eventlet
BuildRequires:  python3-freezegun
BuildRequires:  python3-redis
%endif

%description -n python3-httpretty
Once upon a time a python developer wanted to use a RESTful API, everything was
fine but until the day he needed to test the code that hits the RESTful API:
what if the API server is down? What if its content has changed?
Don't worry, HTTPretty is here for you.


%prep
%autosetup -n httpretty-%{version} -p1

# Alternative for building from commit tarball
#autosetup -n %%{github_name}-%%{github_commit} -p1

# nose plugins we don't have yet
sed -i 's/^with-randomly = 1$//' setup.cfg
sed -i 's/^rednose = 1$//' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files httpretty

%check
%if %{run_tests}
%{__python3} -m nose -v
%endif

%files -n python3-httpretty -f %{pyproject_files}
%doc README.rst
%license COPYING


%changelog
%autochangelog
