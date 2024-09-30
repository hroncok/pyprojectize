# Wants to download sample data, also wants firefox or geckodriver etc.
# So, we skip tests and rely on upstream's CI
%bcond_with tests

%global pypi_name bokeh

%global _description %{expand:
Bokeh is an interactive visualization library for modern web browsers. It
provides elegant, concise construction of versatile graphics, and affords
high-performance interactivity over large or streaming data sets. Bokeh can help
anyone who would like to quickly and easily make interactive plots, dashboards,
and data applications.}

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        16%{?dist}
Summary:        Interactive plots and applications in the browser from Python

# License breakdown: licensecheck -r . | sed '/UNKNOWN/ d' | sort -t ':' -k 2
# The software is released under the BSD license, but includes files that are
# independently also marked with ASL 2.0 and MIT licenses
# The JS bits are npm based

# ASL:
# bokeh/palettes.py
# bokeh/server/static/lib/lib.*

# BSD:
# bokeh/server/static/js/bokeh-api.js
# bokeh/server/static/js/bokeh-api.legacy.js
# bokeh/server/static/js/bokeh-api.legacy.min.js
# bokeh/server/static/js/bokeh-api.min.js
# bokeh/server/static/js/bokeh.js
# bokeh/server/static/js/bokeh.legacy.js
# bokeh/server/static/js/bokeh.legacy.min.js
# bokeh/server/static/js/bokeh.min.js
# bokeh/server/static/js/bokeh-tables.js
# bokeh/server/static/js/bokeh-tables.legacy.js
# bokeh/server/static/js/bokeh-widgets.js
# bokeh/server/static/js/bokeh-widgets.legacy.js
# bokeh/server/static/js/bokeh-widgets.legacy.min.js
# bokeh/server/static/js/bokeh-widgets.min.js
# bokeh/server/static/js/compiler.js
# bokeh/server/static/js/compiler/prelude.js
# tests/unit/bokeh/test___init__.py
# bokeh/server/static/js/lib/api/palettes.js
# bokeh/server/static/js/types/api/palettes.d.ts

# MIT (Expat)
# bokeh/server/static/js/lib/core/util/array.js
# bokeh/server/static/js/lib/core/util/callback.js
# bokeh/server/static/js/lib/core/util/types.js
# bokeh/server/static/js/lib/core/util/wheel.js
# bokeh/server/static/js/types/core/util/wheel.d.ts

# Multiple licenses:
# bokeh/server/static/js/bokeh.json: Expat License Apache License 2.0
# bokeh/server/static/js/bokeh-tables.legacy.min.js: Expat License BSD 3-clause "New" or "Revised" License
# bokeh/server/static/js/bokeh-tables.min.js: Expat License BSD 3-clause "New" or "Revised" License

# Also see the breakdown in the bundled JS below
# and https://github.com/bokeh/bokeh/blob/branch-2.2/bokehjs/LICENSE
# Automatically converted from old format: BSD and ASL 2.0 and MIT and ISC - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND Apache-2.0 AND LicenseRef-Callaway-MIT AND ISC
URL:            https://github.com/bokeh/bokeh
Source0:        %pypi_source
# Read package-lock.json and general list of bundled runtime libraries their versions
Source1:        parse-deps.py
# From https://github.com/bokeh/bokeh/commit/865c54896e6158c1195e5ec8352f300cbf10920f
# https://github.com/bokeh/bokeh/pull/10987
Patch0:         bokeh-pr10987-python312-configparser.patch
# https://github.com/bokeh/bokeh/commit/7047c6a90535564c9d05121fc8a095aef1de3c21
# https://github.com/bokeh/bokeh/pull/11174
Patch1:         bokeh-pr11174-replace-jinja2-markup.patch

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

###### Bundles various js bits #####
# From: https://github.com/bokeh/bokeh/blob/0b9526ef553d938bf5de187e2511564c648c13bd/bokehjs/package-lock.json
# using parse-deps.py
# Also verify using the instructions here
# https://github.com/bokeh/bokeh/blob/branch-2.2/bokehjs/LICENSE#L45
# MIT
Provides: bundled(nodejs-@bokeh/numbro) = 1.6.2
# MIT
Provides: bundled(nodejs-@bokeh/slickgrid) = 2.4.2701
# MIT
Provides: bundled(nodejs-@types/jquery) = 3.5.1
# MIT
Provides: bundled(nodejs-@types/sizzle) = 2.3.2
# MIT
Provides: bundled(nodejs-@types/slickgrid) = 2.1.30
# MIT
Provides: bundled(nodejs-choices.js) = 9.0.1
# ISC
Provides: bundled(nodejs-d) = 1.0.1
# MIT
Provides: bundled(nodejs-deepmerge) = 4.2.2
# ISC
Provides: bundled(nodejs-es5-ext) = 0.10.53
# MIT
Provides: bundled(nodejs-es6-iterator) = 2.0.3
# MIT
Provides: bundled(nodejs-es6-map) = 0.1.5
# MIT
Provides: bundled(nodejs-es6-promise) = 4.2.8
# MIT
Provides: bundled(nodejs-es6-set) = 0.1.5
# ISC
Provides: bundled(nodejs-es6-symbol) = 3.1.3
# ISC
Provides: bundled(nodejs-es6-weak-map) = 2.0.3
# MIT
Provides: bundled(nodejs-event-emitter) = 0.3.5
# ISC
Provides: bundled(nodejs-ext) = 1.4.0
# ISC
Provides: bundled(nodejs-flatbush) = 3.3.0
# MIT
Provides: bundled(nodejs-flatpickr) = 4.6.3
# ISC
Provides: bundled(nodejs-flatqueue) = 1.2.1
# ASL 2.0
Provides: bundled(nodejs-fuse.js) = 3.6.1
# MIT
Provides: bundled(nodejs-hammerjs) = 2.0.8
# MIT
Provides: bundled(nodejs-jquery-ui) = 1.12.1
# MIT
Provides: bundled(nodejs-jquery) = 3.5.1
# MIT
Provides: bundled(nodejs-js-tokens) = 4.0.0
# MIT
Provides: bundled(nodejs-loose-envify) = 1.4.0
# MIT
Provides: bundled(nodejs-mgrs) = 1.0.0
# ISC
Provides: bundled(nodejs-next-tick) = 1.0.0
# MIT
Provides: bundled(nodejs-nouislider) = 14.6.0
# MIT
Provides: bundled(nodejs-proj4) = 2.6.2
# MIT
Provides: bundled(nodejs-redux) = 4.0.5
# BSD
Provides: bundled(nodejs-sprintf-js) = 1.1.2
# MIT
Provides: bundled(nodejs-symbol-observable) = 1.2.0
# MIT
Provides: bundled(nodejs-timezone) = 1.0.23
# BSD
Provides: bundled(nodejs-tslib) = 1.13.0
# ISC
Provides: bundled(nodejs-type) = 1.2.0
# MIT
Provides: bundled(nodejs-underscore.template) = 0.1.7
# MIT
Provides: bundled(nodejs-wkt-parser) = 1.2.4

# Optional deps
# https://docs.bokeh.org/en/latest/docs/installation.html#installation
Recommends:       %{py3_dist jupyter-core}
Recommends:       %{py3_dist networkx}
Recommends:       %{py3_dist pandas}
Recommends:       %{py3_dist psutil}
Recommends:       %{py3_dist sphinx}

# Bokeh will look for whatever browser is available and use that, so not adding
# firefox etc to Recommends
# https://docs.bokeh.org/en/latest/docs/user_guide/export.html#userguide-export

%if %{with tests}
BuildRequires:  %{py3_dist beautifulsoup4}
BuildRequires:  %{py3_dist flaky}
BuildRequires:  %{py3_dist Jinja2} >= 2.7
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist nbconvert}
BuildRequires:  %{py3_dist networkx}
BuildRequires:  %{py3_dist numpy} >= 1.11.3
BuildRequires:  %{py3_dist packaging} >= 16.8
BuildRequires:  %{py3_dist pillow} >= 7.1.0
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist python-dateutil} >= 2.1
BuildRequires:  %{py3_dist PyYAML} >= 3.10
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist selenium}
BuildRequires:  %{py3_dist tornado} >= 5.1
BuildRequires:  %{py3_dist typing_extensions} >= 3.7.4
%endif


%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

# Remove zero length file
rm -f %{buildroot}/%{python3_sitelib}/bokeh/server/static/.keep

%check
%if %{with tests}
# https://docs.bokeh.org/en/latest/docs/dev_guide/testing.html
# skip js tests, skip selenium tests
%pytest -m "not selenium" tests/unit
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{pypi_name}

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.0-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.0-11
- Backport upstream patch for Jinja2 3.1 change

* Tue Jul 25 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.0-10
- Backport upstream patch for python 3.12 SafeConfigParser removal

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.3.0-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.10

* Sun Mar 28 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.3.0-1
- Update to latest release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.2.1-3
- Update naming scheme for bundled bits, also in script
- Comment use of parse script
- Correct parse script shebang

* Thu Sep 17 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.2.1-2
- Include detailed licensing
- Add optional requirements
- Remove commented shebang correction command
- List bundled nodejs libs with licenses
- include parse script in srpm
- Remove zero length files

* Wed Sep 16 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.2.1-1
- Remove dependency generator: no longer needed since F30
- Remove python provide line: no longer needed for F33+
- Initial build
