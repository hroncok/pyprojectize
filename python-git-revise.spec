%global shortname git-revise

%global descrip \
git revise is a git subcommand to efficiently update, split, and rearrange\
commits. It is heavily inspired by git rebase, however it tries to be more\
efficient and ergonomic for patch-stack oriented workflows.\
\
By default, git revise will apply staged changes to a target commit, then\
update HEAD to point at the revised history. It also supports splitting commits\
and rewording commit messages.\
\
Unlike git rebase, git revise avoids modifying the working directory or the\
index state, performing all merges in-memory and only writing them when\
necessary. This allows it to be significantly faster on large codebases and\
avoids unnecessarily invalidating builds.

Name:           python-%{shortname}
Version:        0.7.0
Release:        10%{?dist}
Summary:        Efficiently update, split, and rearrange git commits

License:        MIT
URL:            https://github.com/mystor/git-revise
Source0:        https://github.com/mystor/git-revise/archive/%{version}/%{shortname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel >= 3.8
BuildRequires:  python3dist(setuptools)

# For testing purposes
BuildRequires:  python3dist(pytest)
BuildRequires:  git

# Needs gpg in the tests
BuildRequires:  gnupg2

%description    %{descrip}



%package -n %{shortname}
Summary:  %{summary}
Requires: git
Requires: python3-%{shortname} = %{version}-%{release}

%description -n %{shortname}
%{descrip}



%package -n python3-%{shortname}
Summary:    Python modules for git-revise
Requires:   git
Recommends: %{shortname} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{shortname}}

%description -n python3-%{shortname}
This package contains the python modules for the git-revise program.



%prep
%autosetup -n %{shortname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest

%files -n %{shortname}
%license LICENSE
%doc README.md
%{_bindir}/git-revise
%{_mandir}/man1/git-revise.1*

%files -n python3-%{shortname}
%license LICENSE
%doc README.md
%{python3_sitelib}/gitrevise
%{python3_sitelib}/git_revise-%{version}-py%{python3_version}.egg-info



%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.11

* Mon Apr 11 2022 Ian McInerney <ian.s.mcinerney@ieee.org> - 0.7.0-1
- Update to latest upstream release 0.7.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 13 2020 Ian McInerney <ian.s.mcinerney@ieee.org> - 0.6.0-1
- Update to latest upstream release 0.6.0
- Remove manpage location patch (fixed in 0.6.0)

* Thu Jun 11 2020 Ian McInerney <ian.s.mcinerney@ieee.org> - 0.5.1-4
- Rename package and add new subpackages for git-revise and python3-git-revise

* Sat May 16 2020 Ian McInerney <ian.s.mcinerney@ieee.org> - 0.5.1-3
- Add check section to run tests

* Wed May 13 2020 Ian McInerney <ian.s.mcinerney@ieee.org> - 0.5.1-2
- Upstream manpage patch
- Fix review comments

* Fri May 01 2020 Ian McInerney <ian.s.mcinerney@ieee.org> - 0.5.1-1
- Initial package.
