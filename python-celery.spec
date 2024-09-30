%bcond_without tests
# Packaging unstable?
#%%global prerel rc1
%global general_version 5.3.6
%global upstream_version %{general_version}%{?prerel}

Name:           python-celery
Version:        %{general_version}%{?prerel:~%{prerel}}
Release:        %autorelease
BuildArch:      noarch

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://docs.celeryq.dev/
Source0:        https://github.com/celery/celery/archive/v%{upstream_version}/%{name}-%{upstream_version}.tar.gz
# Fix custom pytest markers for pytest
Source1:        pytest.ini
Summary:        Distributed Task Queue

%description
An open source asynchronous task queue/job queue based on
distributed message passing. It is focused on real-time
operation, but supports scheduling as well.

The execution units, called tasks, are executed concurrently
on one or more worker nodes using multiprocessing, Eventlet
or gevent. Tasks can execute asynchronously (in the background)
or synchronously (wait until ready).

Celery is used in production systems to process millions of
tasks a day.

Celery is written in Python, but the protocol can be implemented
in any language. It can also operate with other languages using
web hooks.

The recommended message broker is RabbitMQ, but limited support
for Redis, Beanstalk, MongoDB, CouchDB and databases
(using SQLAlchemy or the Django ORM) is also available.

%package doc
Summary: Documentation for python-celery
# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License: LicenseRef-Callaway-CC-BY-SA

%description doc
Documentation for python-celery.

%package -n python3-celery
Summary:        Distributed Task Queue

# Requires are auto-generated from setup.py (and then from requirements/default.txt)

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-amqp
BuildRequires:  python3-billiard
BuildRequires:  python3-cryptography
BuildRequires:  python3-click
BuildRequires:  python3-click-didyoumean
BuildRequires:  python3-click-plugins
BuildRequires:  python3-click-repl
BuildRequires:  python3-dns
BuildRequires:  python3-dateutil
BuildRequires:  python3-kombu
BuildRequires:  python3-msgpack
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-click
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest-subtests
BuildRequires:  python3-pytz
BuildRequires:  python3-pyyaml
BuildRequires:  python3-redis
BuildRequires:  python3-simplejson
%endif

%description -n python3-celery
%{desc}

%prep
%autosetup -p1 -n celery-%{upstream_version}

# Drop python tzdata requirement which doesn't make sense on Fedora
sed -i 's/tzdata>=2022.7//g' requirements/default.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

#pushd docs
# missing python-sphinx_celery (for the moment)
#make %{?_smp_mflags} html
#popd

# fix custom celery markers in pytest
cp %{SOURCE1} .

%install
%pyproject_install
%pyproject_save_files celery
pushd %{buildroot}%{_bindir}
mv celery celery-%{python3_version}
ln -s celery-%{python3_version} celery-3
ln -s celery-3 celery
popd

%check
# python-moto is not packaged in Fedora, ignore S3 tests
# mongodb is not packaged in Fedora, ignore mongodb tests
# pytest-celery is not packaged in Fedora, ignore integration test
%if %{with tests}
# cache tests
export TEST_BROKER=redis://
export TEST_BACKEND=cache+pylibmc://
%pytest --ignore=t/unit/backends/test_s3.py --ignore=t/unit/backends/test_mongodb.py --ignore=t/distro/test_CI_reqs.py --ignore=t/integration/test_worker.py

# redis tests
export TEST_BROKER=redis://
export TEST_BACKEND=redis://
%pytest --ignore=t/unit/backends/test_s3.py --ignore=t/unit/backends/test_mongodb.py --ignore=t/distro/test_CI_reqs.py --ignore=t/integration/test_worker.py

# rabbitmq tests
export TEST_BROKER=pyamqp://
export TEST_BACKEND=rpc
%pytest --ignore=t/unit/backends/test_s3.py --ignore=t/unit/backends/test_mongodb.py --ignore=t/distro/test_CI_reqs.py --ignore=t/integration/test_worker.py
%endif

%files doc
%license LICENSE

%files -n python3-celery -f %{pyproject_files}
%license LICENSE
%doc README.rst TODO CONTRIBUTORS.txt examples
%{_bindir}/celery
%{_bindir}/celery-3*

%changelog
%autochangelog
