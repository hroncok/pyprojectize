%global srcname keep

# no tests currently defined
%bcond_with tests

Name:           python-%{srcname}
Version:        2.10.1
Release:        12%{?dist}
Summary:        A Meta CLI toolkit

License:        MIT
URL:            https://github.com/orkohunter/keep
# pypi archive does not contain license text
# Source0:        {pypi_source}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Personal shell command keeper and snippets manager

## Features
- Save a new command with a brief description
- Search the saved commands using powerful patterns
- Save the commands as a secret GitHub gist
- Use `keep push` and `keep pull` to sync the commands between GitHub
  gist and other computers.

**ProTip : Save the commands you usually forget in ssh sessions and sync
it with your local machine.**}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pygithub)
BuildRequires:  python3dist(terminaltables)

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%if %{with tests}
%check
%pytest -v
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md tutorial.md
%{_bindir}/%{srcname}

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.10.1-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.10.1-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.10.1-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.10.1-1
- Initial package
