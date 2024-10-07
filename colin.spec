%global pypi_name colin

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

Name:           %{pypi_name}
Version:        0.5.3
Release:        11%{?dist}
Summary:        Tool to check generic rules/best-practices for containers/images/dockerfiles.

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/user-cont/colin
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       python3-%{pypi_name}

%description
`colin` is a tool to check generic rules/best-practices
for containers/images/dockerfiles

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
Recommends:     moby-engine

%description -n python3-%{pypi_name}
`colin` as a tool to check generic rules/best-practices
for containers/images/dockerfiles

%package doc
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
Summary:        colin documentation

%description doc
Documentation for colin

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="${PWD}:${PWD}/docs/" sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%files
%license LICENSE
%{_bindir}/%{pypi_name}
%{_datadir}/bash-completion/completions/%{pypi_name}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.dist-info/
%{_datadir}/%{pypi_name}/
%exclude %{python3_sitelib}/tests

%files doc
%license LICENSE
%doc html

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.3-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.3-9
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.5.3-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.3-2
- Rebuilt for Python 3.11

* Mon Mar 14 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.5.3-1
## Fixes

- Add additional global location of rulesets for default installation from PyPI

## Minor

- Run tests in upstream on the Testing Farm via Packit
- Few code-style changes suggested by Sourcery

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.5.2-1
## Fixes

- The global location of rulesests is now correctly found.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.10

* Fri Mar 12 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.5.0-1
- Prepare release 0.5.0 (Frantisek Lachman)
- Add workflow for uploading release to PyPI (Frantisek Lachman)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- Remove support for ostree format (Lukas Slebodnik)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- Remove unused argument 'fg' (Lukas Slebodnik)
- Drop unused test test_colin_image (Lukas Slebodnik)
- Add rebase check to pre-commit as pre-push hook (Matej Focko)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- Replace old string formating with fstring where flynt can't (Frantisek Lachman)
- Do not template strings when logging (Frantisek Lachman)
- Use flynt to change old formating to the new one (Frantisek Lachman)
- Turn of rebase-check for now (Frantisek Lachman)
- Fix mypy problems (Frantisek Lachman)
- Fix flake8 problems (Frantisek Lachman)
- Reformat using pre-commit (Frantisek Lachman)
- Add pre-commit config (Frantisek Lachman)
- Use docker.io for iamge tests before dropping support for ostree (Lukas Slebodnik)
- Add the umoci utility for unit tests (Lukas Slebodnik)
- Add tests for oci support (Lukas Slebodnik)
- Add support for for scanning images in OCI format (Lukas Slebodnik)
- Use packit aliases (Frantisek Lachman)
- Fix CONTRIBUTING.md to reflect correct CLI args (Rose Judge)
- Add function to convert results to an xunit xml file (#239) (Wheeler Law)
- Fix tests execution on older kernel (Lukas Slebodnik)
- Fix expected string in test_check_command (Lukas Slebodnik)
- check_runner: Allow to overwrite timeout in result_set (Lukas Slebodnik)
- Update Trove classifiers (Hugo van Kemenade)
- Python 3.6 is the minimum (Hugo van Kemenade)
- Add python_requires to help pip (Hugo van Kemenade)
- Add smoke test for testing farm (Frantisek Lachman)
- Update jobs in packit config (Frantisek Lachman)
- Add Developer Certificate of Origin (Laura Barcziova)
- Fix README and setup.py to be able to upload to PyPI (Jiri Popelka)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Lukas Slebodnik <lslebodn@fedoraproject.org> 0.3.1-4
- Change weak dependency in rawhide (docker -> moby-engine)

* Wed May 01 2019 Lukas Slebodnik <lslebodn@fedoraproject.org> 0.3.1-3
- rhbz#1684558 - Remove hard dependency on docker

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Tomas Tomecek <nereone@gmail.com> 0.3.1-1
- 0.3.1 release

* Thu Nov 15 2018 lachmanfrantisek <lachmanfrantisek@gmail.com> 0.3.0-1
- 0.3.0 release

* Mon Oct 22 2018 lachmanfrantisek <lachmanfrantisek@gmail.com> 0.2.1-1
- 0.2.1 release

* Wed Sep 19 2018 Jiri Popelka <jpopelka@redhat.com> 0.2.0-1
- 0.2.0 release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.7

* Wed May 30 2018 Jiri Popelka <jpopelka@redhat.com> 0.1.0-1
- 0.1.0 release

* Wed May 02 2018 Petr Hracek <phracek@redhat.com> - 0.0.4-3
- Polishing texts and remove leftovers (#1572084)

* Wed May 02 2018 Petr Hracek <phracek@redhat.com> - 0.0.4-2
- Fix issues catched by BZ review process (#1572084)

* Wed Apr 25 2018 lachmanfrantisek <flachman@redhat.com> - 0.0.4-1
- bash completion
- better cli
- better ruleset files and loading
- dockerfile support
- python2 compatibility
- better error handling

* Mon Apr 09 2018 Petr Hracek <phracek@redhat.com> - 0.0.3-1
- Initial package.
