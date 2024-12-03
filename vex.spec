Name:           vex
Version:        0.0.19
Release:        %autorelease
Summary:        Run commands in a virtualenv

License:        MIT
URL:            http://github.com/sashahart/%{name}
Source0:        https://github.com/sashahart/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch

Requires:       python3-virtualenv
Requires:       python3-setuptools

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
Vex is an alternative to virtualenv's 'source wherever/bin/activate'
and `deactivate`, and virtualenvwrapper's `workon`, and also
virtualenv-burrito if you use that.
It works in a more elegant way, though it does less. You might find it
nicer to use. And it works with non-bash shells.

%prep
%autosetup -n %{name}-%{version}
# Remove useless files (merge info)
rm -rf %{name}/shell_configs/zsh.orig
rm -rf %{name}/shell_configs/fish.orig

# Port from mock to unittest.mock
sed -i "s/^from mock import /from unittest.mock import /" vex/tests/test_config.py vex/tests/test_main.py vex/tests/test_run.py vex/tests/test_shell_config.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

%check
%pyproject_check_import

%{__python3} -m pytest %{name}/tests/

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/%{name}

%changelog
%autochangelog
