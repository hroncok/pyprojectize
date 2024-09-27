%global pkgname dirsrv

# Exclude i686 bit arches
ExcludeArch: i686

%bcond bundle_jemalloc 1
%if %{with bundle_jemalloc}
%global jemalloc_name jemalloc
%global jemalloc_ver 5.3.0
%global __provides_exclude ^libjemalloc\\.so.*$
%endif

%bcond bundle_libdb %{defined rhel}
%if %{with bundle_libdb}
%global libdb_version 5.3
%global libdb_base_version db-%{libdb_version}.28
%global libdb_full_version lib%{libdb_base_version}-59
%global libdb_bundle_name libdb-%{libdb_version}-389ds.so
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 11
# RPM 4.20
%global libdb_base_dir lib%{libdb_base_version}-build/%{libdb_base_version}
%else
%global libdb_base_dir %{libdb_base_version}
%endif
%endif

# This is used in certain builds to help us know if it has extra features.
%global variant base
# This enables a sanitized build.
%bcond asan 0
%bcond msan 0
%bcond tsan 0
%bcond ubsan 0

%if %{with asan} || %{with msan} || %{with tsan} || %{with ubsan}
%global variant base-xsan
%endif

# Use Clang instead of GCC
%bcond clang 0
%if %{with msan}
%bcond clang 1
%endif

%if %{with clang}
%global toolchain clang
%global _missing_build_ids_terminate_build 0
%endif

# Build cockpit plugin
%bcond cockpit 1

# fedora 15 and later uses tmpfiles.d
# otherwise, comment this out
%{!?with_tmpfiles_d: %global with_tmpfiles_d %{_sysconfdir}/tmpfiles.d}

# systemd support
%global groupname %{pkgname}.target

# Filter argparse-manpage from autogenerated package Requires
%global __requires_exclude ^python.*argparse-manpage

# Force to require nss version greater or equal as the version available at the build time
# See bz1986327
%define dirsrv_requires_ge()  %(LC_ALL="C" echo '%*' | xargs -r rpm -q --qf 'Requires: %%{name} >= %%{epoch}:%%{version}\\n' | sed -e 's/ (none):/ /' -e 's/ 0:/ /' | grep -v "is not")

Summary:          389 Directory Server (%{variant})
Name:             389-ds-base
Version:          3.1.1
Release:          %{autorelease -n %{?with_asan:-e asan}}%{?dist}
License:          GPL-3.0-or-later AND (0BSD OR Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT) AND (CC-BY-4.0 AND MIT) AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (MIT OR CC0-1.0) AND (MIT OR Unlicense) AND 0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MIT AND ISC AND MPL-2.0 AND PSF-2.0
URL:              https://www.port389.org
Obsoletes:        %{name}-legacy-tools < 1.4.4.6
Obsoletes:        %{name}-legacy-tools-debuginfo < 1.4.4.6
Provides:         ldif2ldbm >= 0

##### Bundled cargo crates list - START #####
Provides:  bundled(crate(addr2line)) = 0.22.0
Provides:  bundled(crate(adler)) = 1.0.2
Provides:  bundled(crate(ahash)) = 0.7.8
Provides:  bundled(crate(atty)) = 0.2.14
Provides:  bundled(crate(autocfg)) = 1.3.0
Provides:  bundled(crate(backtrace)) = 0.3.73
Provides:  bundled(crate(base64)) = 0.13.1
Provides:  bundled(crate(bitflags)) = 2.6.0
Provides:  bundled(crate(byteorder)) = 1.5.0
Provides:  bundled(crate(cbindgen)) = 0.26.0
Provides:  bundled(crate(cc)) = 1.1.7
Provides:  bundled(crate(cfg-if)) = 1.0.0
Provides:  bundled(crate(clap)) = 3.2.25
Provides:  bundled(crate(clap_lex)) = 0.2.4
Provides:  bundled(crate(concread)) = 0.2.21
Provides:  bundled(crate(crossbeam)) = 0.8.4
Provides:  bundled(crate(crossbeam-channel)) = 0.5.13
Provides:  bundled(crate(crossbeam-deque)) = 0.8.5
Provides:  bundled(crate(crossbeam-epoch)) = 0.9.18
Provides:  bundled(crate(crossbeam-queue)) = 0.3.11
Provides:  bundled(crate(crossbeam-utils)) = 0.8.20
Provides:  bundled(crate(errno)) = 0.3.9
Provides:  bundled(crate(fastrand)) = 2.1.0
Provides:  bundled(crate(fernet)) = 0.1.4
Provides:  bundled(crate(foreign-types)) = 0.3.2
Provides:  bundled(crate(foreign-types-shared)) = 0.1.1
Provides:  bundled(crate(getrandom)) = 0.2.15
Provides:  bundled(crate(gimli)) = 0.29.0
Provides:  bundled(crate(hashbrown)) = 0.12.3
Provides:  bundled(crate(heck)) = 0.4.1
Provides:  bundled(crate(hermit-abi)) = 0.1.19
Provides:  bundled(crate(indexmap)) = 1.9.3
Provides:  bundled(crate(instant)) = 0.1.13
Provides:  bundled(crate(itoa)) = 1.0.11
Provides:  bundled(crate(jobserver)) = 0.1.32
Provides:  bundled(crate(libc)) = 0.2.155
Provides:  bundled(crate(linux-raw-sys)) = 0.4.14
Provides:  bundled(crate(lock_api)) = 0.4.12
Provides:  bundled(crate(log)) = 0.4.22
Provides:  bundled(crate(lru)) = 0.7.8
Provides:  bundled(crate(memchr)) = 2.7.4
Provides:  bundled(crate(miniz_oxide)) = 0.7.4
Provides:  bundled(crate(object)) = 0.36.2
Provides:  bundled(crate(once_cell)) = 1.19.0
Provides:  bundled(crate(openssl)) = 0.10.66
Provides:  bundled(crate(openssl-macros)) = 0.1.1
Provides:  bundled(crate(openssl-sys)) = 0.9.103
Provides:  bundled(crate(os_str_bytes)) = 6.6.1
Provides:  bundled(crate(parking_lot)) = 0.11.2
Provides:  bundled(crate(parking_lot_core)) = 0.8.6
Provides:  bundled(crate(paste)) = 0.1.18
Provides:  bundled(crate(paste-impl)) = 0.1.18
Provides:  bundled(crate(pin-project-lite)) = 0.2.14
Provides:  bundled(crate(pkg-config)) = 0.3.30
Provides:  bundled(crate(ppv-lite86)) = 0.2.18
Provides:  bundled(crate(proc-macro-hack)) = 0.5.20+deprecated
Provides:  bundled(crate(proc-macro2)) = 1.0.86
Provides:  bundled(crate(quote)) = 1.0.36
Provides:  bundled(crate(rand)) = 0.8.5
Provides:  bundled(crate(rand_chacha)) = 0.3.1
Provides:  bundled(crate(rand_core)) = 0.6.4
Provides:  bundled(crate(redox_syscall)) = 0.2.16
Provides:  bundled(crate(rustc-demangle)) = 0.1.24
Provides:  bundled(crate(rustix)) = 0.38.34
Provides:  bundled(crate(ryu)) = 1.0.18
Provides:  bundled(crate(scopeguard)) = 1.2.0
Provides:  bundled(crate(serde)) = 1.0.204
Provides:  bundled(crate(serde_derive)) = 1.0.204
Provides:  bundled(crate(serde_json)) = 1.0.121
Provides:  bundled(crate(smallvec)) = 1.13.2
Provides:  bundled(crate(strsim)) = 0.10.0
Provides:  bundled(crate(syn)) = 2.0.72
Provides:  bundled(crate(tempfile)) = 3.10.1
Provides:  bundled(crate(termcolor)) = 1.4.1
Provides:  bundled(crate(textwrap)) = 0.16.1
Provides:  bundled(crate(tokio)) = 1.39.2
Provides:  bundled(crate(tokio-macros)) = 2.4.0
Provides:  bundled(crate(toml)) = 0.5.11
Provides:  bundled(crate(unicode-ident)) = 1.0.12
Provides:  bundled(crate(uuid)) = 0.8.2
Provides:  bundled(crate(vcpkg)) = 0.2.15
Provides:  bundled(crate(version_check)) = 0.9.5
Provides:  bundled(crate(wasi)) = 0.11.0+wasi_snapshot_preview1
Provides:  bundled(crate(winapi)) = 0.3.9
Provides:  bundled(crate(winapi-i686-pc-windows-gnu)) = 0.4.0
Provides:  bundled(crate(winapi-util)) = 0.1.8
Provides:  bundled(crate(winapi-x86_64-pc-windows-gnu)) = 0.4.0
Provides:  bundled(crate(windows-sys)) = 0.52.0
Provides:  bundled(crate(windows-targets)) = 0.52.6
Provides:  bundled(crate(windows_aarch64_gnullvm)) = 0.52.6
Provides:  bundled(crate(windows_aarch64_msvc)) = 0.52.6
Provides:  bundled(crate(windows_i686_gnu)) = 0.52.6
Provides:  bundled(crate(windows_i686_gnullvm)) = 0.52.6
Provides:  bundled(crate(windows_i686_msvc)) = 0.52.6
Provides:  bundled(crate(windows_x86_64_gnu)) = 0.52.6
Provides:  bundled(crate(windows_x86_64_gnullvm)) = 0.52.6
Provides:  bundled(crate(windows_x86_64_msvc)) = 0.52.6
Provides:  bundled(crate(zerocopy)) = 0.6.6
Provides:  bundled(crate(zerocopy-derive)) = 0.6.6
Provides:  bundled(crate(zeroize)) = 1.8.1
Provides:  bundled(crate(zeroize_derive)) = 1.4.2
Provides:  bundled(npm(@aashutoshrathi/word-wrap)) = 1.2.6
Provides:  bundled(npm(@eslint-community/eslint-utils)) = 4.4.0
Provides:  bundled(npm(@eslint-community/regexpp)) = 4.5.1
Provides:  bundled(npm(@eslint/eslintrc)) = 2.0.3
Provides:  bundled(npm(@eslint/js)) = 8.42.0
Provides:  bundled(npm(@fortawesome/fontawesome-common-types)) = 0.2.36
Provides:  bundled(npm(@fortawesome/fontawesome-svg-core)) = 1.2.36
Provides:  bundled(npm(@fortawesome/free-solid-svg-icons)) = 5.15.4
Provides:  bundled(npm(@fortawesome/react-fontawesome)) = 0.1.19
Provides:  bundled(npm(@humanwhocodes/config-array)) = 0.11.10
Provides:  bundled(npm(@humanwhocodes/module-importer)) = 1.0.1
Provides:  bundled(npm(@humanwhocodes/object-schema)) = 1.2.1
Provides:  bundled(npm(@nodelib/fs.scandir)) = 2.1.5
Provides:  bundled(npm(@nodelib/fs.stat)) = 2.0.5
Provides:  bundled(npm(@nodelib/fs.walk)) = 1.2.8
Provides:  bundled(npm(@patternfly/patternfly)) = 4.224.2
Provides:  bundled(npm(@patternfly/react-charts)) = 6.94.19
Provides:  bundled(npm(@patternfly/react-core)) = 4.276.8
Provides:  bundled(npm(@patternfly/react-icons)) = 4.93.6
Provides:  bundled(npm(@patternfly/react-styles)) = 4.92.6
Provides:  bundled(npm(@patternfly/react-table)) = 4.113.0
Provides:  bundled(npm(@patternfly/react-tokens)) = 4.94.6
Provides:  bundled(npm(@types/d3-array)) = 3.0.5
Provides:  bundled(npm(@types/d3-color)) = 3.1.0
Provides:  bundled(npm(@types/d3-ease)) = 3.0.0
Provides:  bundled(npm(@types/d3-interpolate)) = 3.0.1
Provides:  bundled(npm(@types/d3-path)) = 3.0.0
Provides:  bundled(npm(@types/d3-scale)) = 4.0.3
Provides:  bundled(npm(@types/d3-shape)) = 3.1.1
Provides:  bundled(npm(@types/d3-time)) = 3.0.0
Provides:  bundled(npm(@types/d3-timer)) = 3.0.0
Provides:  bundled(npm(acorn)) = 8.8.2
Provides:  bundled(npm(acorn-jsx)) = 5.3.2
Provides:  bundled(npm(ajv)) = 6.12.6
Provides:  bundled(npm(ansi-regex)) = 5.0.1
Provides:  bundled(npm(ansi-styles)) = 4.3.0
Provides:  bundled(npm(argparse)) = 2.0.1
Provides:  bundled(npm(attr-accept)) = 1.1.3
Provides:  bundled(npm(balanced-match)) = 1.0.2
Provides:  bundled(npm(brace-expansion)) = 1.1.11
Provides:  bundled(npm(callsites)) = 3.1.0
Provides:  bundled(npm(chalk)) = 4.1.2
Provides:  bundled(npm(color-convert)) = 2.0.1
Provides:  bundled(npm(color-name)) = 1.1.4
Provides:  bundled(npm(concat-map)) = 0.0.1
Provides:  bundled(npm(core-js)) = 2.6.12
Provides:  bundled(npm(cross-spawn)) = 7.0.3
Provides:  bundled(npm(d3-array)) = 3.2.4
Provides:  bundled(npm(d3-color)) = 3.1.0
Provides:  bundled(npm(d3-ease)) = 3.0.1
Provides:  bundled(npm(d3-format)) = 3.1.0
Provides:  bundled(npm(d3-interpolate)) = 3.0.1
Provides:  bundled(npm(d3-path)) = 3.1.0
Provides:  bundled(npm(d3-scale)) = 4.0.2
Provides:  bundled(npm(d3-shape)) = 3.2.0
Provides:  bundled(npm(d3-time)) = 3.1.0
Provides:  bundled(npm(d3-time-format)) = 4.1.0
Provides:  bundled(npm(d3-timer)) = 3.0.1
Provides:  bundled(npm(debug)) = 4.3.4
Provides:  bundled(npm(deep-is)) = 0.1.4
Provides:  bundled(npm(delaunator)) = 4.0.1
Provides:  bundled(npm(delaunay-find)) = 0.0.6
Provides:  bundled(npm(doctrine)) = 3.0.0
Provides:  bundled(npm(encoding)) = 0.1.13
Provides:  bundled(npm(escape-string-regexp)) = 4.0.0
Provides:  bundled(npm(eslint)) = 8.42.0
Provides:  bundled(npm(eslint-plugin-react-hooks)) = 4.6.0
Provides:  bundled(npm(eslint-scope)) = 7.2.0
Provides:  bundled(npm(eslint-visitor-keys)) = 3.4.1
Provides:  bundled(npm(espree)) = 9.5.2
Provides:  bundled(npm(esquery)) = 1.5.0
Provides:  bundled(npm(esrecurse)) = 4.3.0
Provides:  bundled(npm(estraverse)) = 5.3.0
Provides:  bundled(npm(esutils)) = 2.0.3
Provides:  bundled(npm(fast-deep-equal)) = 3.1.3
Provides:  bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides:  bundled(npm(fast-levenshtein)) = 2.0.6
Provides:  bundled(npm(fastq)) = 1.15.0
Provides:  bundled(npm(file-entry-cache)) = 6.0.1
Provides:  bundled(npm(file-selector)) = 0.1.19
Provides:  bundled(npm(find-up)) = 5.0.0
Provides:  bundled(npm(flat-cache)) = 3.0.4
Provides:  bundled(npm(flatted)) = 3.2.7
Provides:  bundled(npm(focus-trap)) = 6.9.2
Provides:  bundled(npm(fs.realpath)) = 1.0.0
Provides:  bundled(npm(gettext-parser)) = 2.0.0
Provides:  bundled(npm(glob)) = 7.2.3
Provides:  bundled(npm(glob-parent)) = 6.0.2
Provides:  bundled(npm(globals)) = 13.20.0
Provides:  bundled(npm(graphemer)) = 1.4.0
Provides:  bundled(npm(has-flag)) = 4.0.0
Provides:  bundled(npm(hoist-non-react-statics)) = 3.3.2
Provides:  bundled(npm(iconv-lite)) = 0.6.3
Provides:  bundled(npm(ignore)) = 5.2.4
Provides:  bundled(npm(import-fresh)) = 3.3.0
Provides:  bundled(npm(imurmurhash)) = 0.1.4
Provides:  bundled(npm(inflight)) = 1.0.6
Provides:  bundled(npm(inherits)) = 2.0.4
Provides:  bundled(npm(internmap)) = 2.0.3
Provides:  bundled(npm(is-extglob)) = 2.1.1
Provides:  bundled(npm(is-glob)) = 4.0.3
Provides:  bundled(npm(is-path-inside)) = 3.0.3
Provides:  bundled(npm(isexe)) = 2.0.0
Provides:  bundled(npm(js-tokens)) = 4.0.0
Provides:  bundled(npm(js-yaml)) = 4.1.0
Provides:  bundled(npm(json-schema-traverse)) = 0.4.1
Provides:  bundled(npm(json-stable-stringify-without-jsonify)) = 1.0.1
Provides:  bundled(npm(json-stringify-safe)) = 5.0.1
Provides:  bundled(npm(levn)) = 0.4.1
Provides:  bundled(npm(locate-path)) = 6.0.0
Provides:  bundled(npm(lodash)) = 4.17.21
Provides:  bundled(npm(lodash.merge)) = 4.6.2
Provides:  bundled(npm(loose-envify)) = 1.4.0
Provides:  bundled(npm(minimatch)) = 3.1.2
Provides:  bundled(npm(ms)) = 2.1.2
Provides:  bundled(npm(natural-compare)) = 1.4.0
Provides:  bundled(npm(object-assign)) = 4.1.1
Provides:  bundled(npm(once)) = 1.4.0
Provides:  bundled(npm(optionator)) = 0.9.3
Provides:  bundled(npm(p-limit)) = 3.1.0
Provides:  bundled(npm(p-locate)) = 5.0.0
Provides:  bundled(npm(parent-module)) = 1.0.1
Provides:  bundled(npm(path-exists)) = 4.0.0
Provides:  bundled(npm(path-is-absolute)) = 1.0.1
Provides:  bundled(npm(path-key)) = 3.1.1
Provides:  bundled(npm(popper.js)) = 1.16.1
Provides:  bundled(npm(prelude-ls)) = 1.2.1
Provides:  bundled(npm(prop-types)) = 15.8.1
Provides:  bundled(npm(prop-types-extra)) = 1.1.1
Provides:  bundled(npm(punycode)) = 2.3.0
Provides:  bundled(npm(queue-microtask)) = 1.2.3
Provides:  bundled(npm(react)) = 17.0.2
Provides:  bundled(npm(react-dom)) = 17.0.2
Provides:  bundled(npm(react-dropzone)) = 9.0.0
Provides:  bundled(npm(react-fast-compare)) = 3.2.2
Provides:  bundled(npm(react-is)) = 16.13.1
Provides:  bundled(npm(resolve-from)) = 4.0.0
Provides:  bundled(npm(reusify)) = 1.0.4
Provides:  bundled(npm(rimraf)) = 3.0.2
Provides:  bundled(npm(run-parallel)) = 1.2.0
Provides:  bundled(npm(safe-buffer)) = 5.2.1
Provides:  bundled(npm(safer-buffer)) = 2.1.2
Provides:  bundled(npm(scheduler)) = 0.20.2
Provides:  bundled(npm(shebang-command)) = 2.0.0
Provides:  bundled(npm(shebang-regex)) = 3.0.0
Provides:  bundled(npm(strip-ansi)) = 6.0.1
Provides:  bundled(npm(strip-json-comments)) = 3.1.1
Provides:  bundled(npm(supports-color)) = 7.2.0
Provides:  bundled(npm(tabbable)) = 5.3.3
Provides:  bundled(npm(text-table)) = 0.2.0
Provides:  bundled(npm(tippy.js)) = 5.1.2
Provides:  bundled(npm(tslib)) = 2.5.3
Provides:  bundled(npm(type-check)) = 0.4.0
Provides:  bundled(npm(type-fest)) = 0.20.2
Provides:  bundled(npm(uri-js)) = 4.4.1
Provides:  bundled(npm(victory-area)) = 36.6.10
Provides:  bundled(npm(victory-axis)) = 36.6.10
Provides:  bundled(npm(victory-bar)) = 36.6.10
Provides:  bundled(npm(victory-brush-container)) = 36.6.10
Provides:  bundled(npm(victory-chart)) = 36.6.10
Provides:  bundled(npm(victory-core)) = 36.6.10
Provides:  bundled(npm(victory-create-container)) = 36.6.10
Provides:  bundled(npm(victory-cursor-container)) = 36.6.10
Provides:  bundled(npm(victory-group)) = 36.6.10
Provides:  bundled(npm(victory-legend)) = 36.6.10
Provides:  bundled(npm(victory-line)) = 36.6.10
Provides:  bundled(npm(victory-pie)) = 36.6.10
Provides:  bundled(npm(victory-polar-axis)) = 36.6.10
Provides:  bundled(npm(victory-scatter)) = 36.6.10
Provides:  bundled(npm(victory-selection-container)) = 36.6.10
Provides:  bundled(npm(victory-shared-events)) = 36.6.10
Provides:  bundled(npm(victory-stack)) = 36.6.10
Provides:  bundled(npm(victory-tooltip)) = 36.6.10
Provides:  bundled(npm(victory-vendor)) = 36.6.10
Provides:  bundled(npm(victory-voronoi-container)) = 36.6.10
Provides:  bundled(npm(victory-zoom-container)) = 36.6.10
Provides:  bundled(npm(warning)) = 4.0.3
Provides:  bundled(npm(which)) = 2.0.2
Provides:  bundled(npm(wrappy)) = 1.0.2
Provides:  bundled(npm(yocto-queue)) = 0.1.0
##### Bundled cargo crates list - END #####

# Attach the buildrequires to the top level package:
BuildRequires:    nspr-devel
BuildRequires:    nss-devel >= 3.34
BuildRequires:    openldap-clients
BuildRequires:    openldap-devel
BuildRequires:    lmdb-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    icu
BuildRequires:    libicu-devel
BuildRequires:    pcre2-devel
BuildRequires:    cracklib-devel
BuildRequires:    json-c-devel
%if %{with clang}
BuildRequires:    libatomic
BuildRequires:    clang
BuildRequires:    compiler-rt
BuildRequires:    lld
%else
BuildRequires:    gcc
BuildRequires:    gcc-c++
%if %{with asan}
BuildRequires:    libasan
%endif
%if %{with tsan}
BuildRequires:    libtsan
%endif
%if %{with ubsan}
BuildRequires:    libubsan
%endif
%endif
%if %{without bundle_libdb}
BuildRequires:    libdb-devel
%endif

# The following are needed to build the snmp ldap-agent
BuildRequires:    net-snmp-devel
BuildRequires:    bzip2-devel
BuildRequires:    openssl-devel
# the following is for the pam passthru auth plug-in
BuildRequires:    pam-devel
BuildRequires:    systemd-units
BuildRequires:    systemd-devel
BuildRequires:    systemd-rpm-macros
%{?sysusers_requires_compat}
BuildRequires:    cargo
BuildRequires:    rust
BuildRequires:    pkgconfig
BuildRequires:    pkgconfig(systemd)
BuildRequires:    pkgconfig(krb5)
BuildRequires:    pkgconfig(libpcre2-8)
# Needed to support regeneration of the autotool artifacts.
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
# For our documentation
BuildRequires:    doxygen
# For tests!
BuildRequires:    libcmocka-devel
# For lib389 and related components.
BuildRequires:    python%{python3_pkgversion}
BuildRequires:    python%{python3_pkgversion}-devel
BuildRequires:    python%{python3_pkgversion}-setuptools
BuildRequires:    python%{python3_pkgversion}-ldap
BuildRequires:    python%{python3_pkgversion}-pyasn1
BuildRequires:    python%{python3_pkgversion}-pyasn1-modules
BuildRequires:    python%{python3_pkgversion}-dateutil
BuildRequires:    python%{python3_pkgversion}-argcomplete
BuildRequires:    python%{python3_pkgversion}-argparse-manpage
BuildRequires:    python%{python3_pkgversion}-policycoreutils
BuildRequires:    python%{python3_pkgversion}-libselinux
BuildRequires:    python%{python3_pkgversion}-cryptography

# For cockpit
%if %{with cockpit}
BuildRequires:    rsync
BuildRequires:    npm
BuildRequires:    nodejs
%endif

Requires:         %{name}-libs = %{version}-%{release}
Requires:         python%{python3_pkgversion}-lib389 = %{version}-%{release}

# this is needed for using semanage from our setup scripts
Requires:         policycoreutils-python-utils
Requires:         libsemanage-python%{python3_pkgversion}
# the following are needed for some of our scripts
Requires:         openldap-clients
Requires:         acl
# this is needed to setup SSL if you are not using the
# administration server package
Requires:         nss-tools
%dirsrv_requires_ge nss
# these are not found by the auto-dependency method
# they are required to support the mandatory LDAP SASL mechs
Requires:         cyrus-sasl-gssapi
Requires:         cyrus-sasl-md5
# This is optionally supported by us, as we use it in our tests
Requires:         cyrus-sasl-plain
# this is needed for backldbm
%if %{without bundle_libdb}
Requires:         libdb
%endif
Requires:         lmdb-libs
# Needed by logconv.pl
%if %{without bundle_libdb}
Requires:         perl-DB_File
%endif
Requires:         perl-Archive-Tar
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
Requires:         perl-debugger
Requires:         perl-sigtrap
%endif
# Needed for password dictionary checks
Requires:         cracklib-dicts
Requires:         json-c
# Log compression
Requires:         zlib-devel
# Picks up our systemd deps.
%{?systemd_requires}

Source0:          %{name}-%{version}.tar.bz2
Source2:          %{name}-devel.README
%if %{with bundle_jemalloc}
Source3:          https://github.com/jemalloc/%{jemalloc_name}/releases/download/%{jemalloc_ver}/%{jemalloc_name}-%{jemalloc_ver}.tar.bz2
%endif
Source4:          389-ds-base.sysusers
%if %{with bundle_libdb}
Source5:          https://fedorapeople.org/groups/389ds/libdb-5.3.28-59.tar.bz2
%endif

%description
389 Directory Server is an LDAPv3 compliant server.  The base package includes
the LDAP server and command line utilities for server administration.
%if %{with asan}
WARNING! This build is linked to Address Sanitisation libraries. This probably
isn't what you want. Please contact support immediately.
Please see http://seclists.org/oss-sec/2016/q1/363 for more information.
%endif


%package          libs
Summary:          Core libraries for 389 Directory Server (%{variant})
Provides:         svrcore = 4.1.4
Obsoletes:        svrcore <= 4.1.3
Conflicts:        svrcore
%dirsrv_requires_ge nss
Requires:         nspr
Requires:         openldap
Requires:         systemd-libs
# Pull in sasl
Requires:         cyrus-sasl-lib
# KRB
Requires:         krb5-libs
%if %{with clang}
Requires:         llvm
Requires:         compiler-rt
%else
%if %{with asan}
Requires:         libasan
%endif
%if %{with tsan}
Requires:         libtsan
%endif
%if %{with ubsan}
Requires:         libubsan
%endif
%endif

%description      libs
Core libraries for the 389 Directory Server base package.  These libraries
are used by the main package and the -devel package.  This allows the -devel
package to be installed with just the -libs package and without the main package.

%package          devel
Summary:          Development libraries for 389 Directory Server (%{variant})
Provides:         svrcore-devel = 4.1.4
Obsoletes:        svrcore-devel <= 4.1.3
Conflicts:        svrcore-devel
Requires:         %{name}-libs = %{version}-%{release}
Requires:         pkgconfig
Requires:         nspr-devel
Requires:         nss-devel >= 3.34
Requires:         openldap-devel
# systemd-libs contains the headers iirc.
Requires:         systemd-libs

%description      devel
Development Libraries and headers for the 389 Directory Server base package.

%package          snmp
Summary:          SNMP Agent for 389 Directory Server
Requires:         %{name} = %{version}-%{release}

Obsoletes:        %{name} <= 1.4.0.0

%description      snmp
SNMP Agent for the 389 Directory Server base package.

%if %{with bundle_libdb}
%package          bdb
Summary:          Berkeley Database backend for 389 Directory Server
%description      bdb
Berkeley Database backend for 389 Directory Server
Warning! This backend is deprecated in favor of lmdb and its support
may be removed in future versions.

Requires:         %{name} = %{version}-%{release}
# Berkeley DB database libdb was marked as deprecated since F40:
# https://fedoraproject.org/wiki/Changes/389_Directory_Server_3.0.0
# because libdb was marked as deprecated since F33
# https://fedoraproject.org/wiki/Changes/Libdb_deprecated
Provides:         deprecated()
%endif


%package -n python%{python3_pkgversion}-lib389
Summary:  A library for accessing, testing, and configuring the 389 Directory Server
BuildArch:        noarch
Requires: %{name} = %{version}-%{release}
Requires: openssl
# This is for /usr/bin/c_rehash tool, only needed for openssl < 1.1.0
Requires: openssl-perl
Requires: iproute
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-distro
Requires: python%{python3_pkgversion}-ldap
Requires: python%{python3_pkgversion}-pyasn1
Requires: python%{python3_pkgversion}-pyasn1-modules
Requires: python%{python3_pkgversion}-dateutil
Requires: python%{python3_pkgversion}-argcomplete
Requires: python%{python3_pkgversion}-libselinux
Requires: python%{python3_pkgversion}-setuptools
Requires: python%{python3_pkgversion}-cryptography
Recommends: bash-completion
%{?python_provide:%python_provide python%{python3_pkgversion}-lib389}

%description -n python%{python3_pkgversion}-lib389
This module contains tools and libraries for accessing, testing,
 and configuring the 389 Directory Server.

%if %{with cockpit}
%package -n cockpit-389-ds
Summary:          Cockpit UI Plugin for configuring and administering the 389 Directory Server
BuildArch:        noarch
Requires:         cockpit
Requires:         %{name} = %{version}-%{release}
Requires:         python%{python3_pkgversion}
Requires:         python%{python3_pkgversion}-lib389 = %{version}-%{release}

%description -n cockpit-389-ds
A cockpit UI Plugin for configuring and administering the 389 Directory Server
%endif

%prep
%autosetup -p1 -v -n %{name}-%{version}

%if %{with bundle_jemalloc}
%setup -q -n %{name}-%{version} -T -D -b 3
%endif

%if %{with bundle_libdb}
%setup -q -n %{name}-%{version} -T -D -b 5
%endif

cp %{SOURCE2} README.devel

%build

%if %{with clang}
CLANG_FLAGS="--enable-clang"
%endif

%{?with_tmpfiles_d: TMPFILES_FLAG="--with-tmpfiles-d=%{with_tmpfiles_d}"}

%if %{with asan}
ASAN_FLAGS="--enable-asan --enable-debug"
%endif

%if %{with msan}
MSAN_FLAGS="--enable-msan --enable-debug"
%endif

%if %{with tsan}
TSAN_FLAGS="--enable-tsan --enable-debug"
%endif

%if %{with ubsan}
UBSAN_FLAGS="--enable-ubsan --enable-debug"
%endif

RUST_FLAGS="--enable-rust --enable-rust-offline"

%if %{without cockpit}
COCKPIT_FLAGS="--disable-cockpit"
%endif

%if %{with bundle_jemalloc}
# Override page size, bz #1545539
# 4K
%ifarch %ix86 %arm x86_64 s390x
%define lg_page --with-lg-page=12
%endif

# 64K
%ifarch ppc64 ppc64le aarch64
%define lg_page --with-lg-page=16
%endif

# Override huge page size on aarch64
# 2M instead of 512M
%ifarch aarch64
%define lg_hugepage --with-lg-hugepage=21
%endif

# Build jemalloc
pushd ../%{jemalloc_name}-%{jemalloc_ver}
%configure \
        --libdir=%{_libdir}/%{pkgname}/lib \
        --bindir=%{_libdir}/%{pkgname}/bin \
        --enable-prof %{lg_page} %{lg_hugepage}
make %{?_smp_mflags}
popd
%endif

# Build custom libdb package
%if %{with bundle_libdb}
mkdir -p ../%{libdb_base_version}
pushd ../%{libdb_base_version}
tar -xjf  %{_topdir}/SOURCES/%{libdb_full_version}.tar.bz2
mv %{libdb_full_version} SOURCES
rpmbuild  --define "_topdir $PWD" -bc %{_builddir}/%{name}-%{version}/rpm/bundle-libdb.spec
popd
%endif

# Rebuild the autotool artifacts now.
autoreconf -fiv

%configure \
%if %{with bundle_libdb}
           --with-bundle-libdb=%{_builddir}/%{libdb_base_version}/BUILD/%{libdb_base_dir}/dist/dist-tls \
%endif
           --with-selinux $TMPFILES_FLAG \
           --with-systemd \
           --with-systemdsystemunitdir=%{_unitdir} \
           --with-systemdsystemconfdir=%{_sysconfdir}/systemd/system \
           --with-systemdgroupname=%{groupname} \
           --libexecdir=%{_libexecdir}/%{pkgname} \
           $ASAN_FLAGS $MSAN_FLAGS $TSAN_FLAGS $UBSAN_FLAGS $RUST_FLAGS $CLANG_FLAGS $COCKPIT_FLAGS \
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
           --with-libldap-r=no \
%endif
           --enable-cmocka

# Avoid "Unknown key name 'XXX' in section 'Service', ignoring." warnings from systemd on older releases
%if 0%{?rhel} && 0%{?rhel} < 9
  sed -r -i '/^(Protect(Home|Hostname|KernelLogs)|PrivateMounts)=/d' %{_builddir}/%{name}-%{version}/wrappers/*.service.in
%endif

# lib389
make src/lib389/setup.py
pushd ./src/lib389
%py3_build
popd
# argparse-manpage dynamic man pages have hardcoded man v1 in header,
# need to change it to v8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}/src/lib389/man/dsconf.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}/src/lib389/man/dsctl.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}/src/lib389/man/dsidm.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}/src/lib389/man/dscreate.8

# Generate symbolic info for debuggers
export XCFLAGS=$RPM_OPT_FLAGS

make %{?_smp_mflags}

%install

mkdir -p %{buildroot}%{_datadir}/gdb/auto-load%{_sbindir}
%if %{with cockpit}
mkdir -p %{buildroot}%{_datadir}/cockpit
%endif
make DESTDIR="$RPM_BUILD_ROOT" install

%if %{with cockpit}
find %{buildroot}%{_datadir}/cockpit/389-console -type d | sed -e "s@%{buildroot}@@" | sed -e 's/^/\%dir /' > cockpit.list
find %{buildroot}%{_datadir}/cockpit/389-console -type f | sed -e "s@%{buildroot}@@" >> cockpit.list
%endif

find %{buildroot}%{_libdir}/%{pkgname}/plugins/ -type f -iname 'lib*.so' | sed -e "s@%{buildroot}@@" > plugins.list
%if %{with bundle_libdb}
sed -i -e "/libback-bdb/d" plugins.list
%endif

# Copy in our docs from doxygen.
cp -r %{_builddir}/%{name}-%{version}/man/man3 $RPM_BUILD_ROOT/%{_mandir}/man3

# lib389
pushd src/lib389
%py3_install
popd

# Register CLI tools for bash completion
for clitool in dsconf dsctl dsidm dscreate ds-replcheck
do
    register-python-argcomplete "${clitool}" > "${clitool}"
    install -p -m 0644 -D -t '%{buildroot}%{bash_completions_dir}' "${clitool}"
done

mkdir -p $RPM_BUILD_ROOT/var/log/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lib/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lock/%{pkgname} \
    && chmod 770 $RPM_BUILD_ROOT/var/lock/%{pkgname}

# for systemd
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/systemd/system/%{groupname}.wants
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/389-ds-base.conf

#remove libtool and static libs
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/plugins/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libsvrcore.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libsvrcore.la

%if %{with bundle_jemalloc}
pushd ../%{jemalloc_name}-%{jemalloc_ver}
make DESTDIR="$RPM_BUILD_ROOT" install_lib install_bin
cp -pa COPYING ../%{name}-%{version}/COPYING.jemalloc
cp -pa README ../%{name}-%{version}/README.jemalloc
popd
%endif

%if %{with bundle_libdb}
pushd ../%{libdb_base_version}
libdbbuilddir=$PWD/BUILD/%{libdb_base_dir}
libdbdestdir=$PWD/../%{name}-%{version}
cp -pa $libdbbuilddir/LICENSE $libdbdestdir/LICENSE.libdb
cp -pa $libdbbuilddir/README $libdbdestdir/README.libdb
cp -pa $libdbbuilddir/lgpl-2.1.txt $libdbdestdir/lgpl-2.1.txt.libdb
cp -pa $libdbbuilddir/dist/dist-tls/.libs/%{libdb_bundle_name} $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/%{libdb_bundle_name}
popd
%endif


%check
# This checks the code, if it fails it prints why, then re-raises the fail to shortcircuit the rpm build.
%if %{with tsan}
export TSAN_OPTIONS=print_stacktrace=1:second_deadlock_stack=1:history_size=7
%endif
%if %{without asan} && %{without msan}
if ! make DESTDIR="$RPM_BUILD_ROOT" check; then cat ./test-suite.log && false; fi
%endif

%post
if [ -n "$DEBUGPOSTTRANS" ] ; then
    output=$DEBUGPOSTTRANS
    output2=${DEBUGPOSTTRANS}.upgrade
else
    output=/dev/null
    output2=/dev/null
fi

# reload to pick up any changes to systemd files
/bin/systemctl daemon-reload >$output 2>&1 || :

# https://fedoraproject.org/wiki/Packaging:UsersAndGroups#Soft_static_allocation
# Soft static allocation for UID and GID
# sysusers.d format https://fedoraproject.org/wiki/Changes/Adopting_sysusers.d_format
%sysusers_create_compat %{SOURCE4}

# Reload our sysctl before we restart (if we can)
sysctl --system &> $output; true

# Gather the running instances so we can restart them
instbase="%{_sysconfdir}/%{pkgname}"
ninst=0
for dir in $instbase/slapd-* ; do
    echo dir = $dir >> $output 2>&1 || :
    if [ ! -d "$dir" ] ; then continue ; fi
    case "$dir" in *.removed) continue ;; esac
    basename=`basename $dir`
    inst="%{pkgname}@`echo $basename | sed -e 's/slapd-//g'`"
    echo found instance $inst - getting status  >> $output 2>&1 || :
    if /bin/systemctl -q is-active $inst ; then
       echo instance $inst is running >> $output 2>&1 || :
       instances="$instances $inst"
    else
       echo instance $inst is not running >> $output 2>&1 || :
    fi
    ninst=`expr $ninst + 1`
done
if [ $ninst -eq 0 ] ; then
    echo no instances to upgrade >> $output 2>&1 || :
    exit 0 # have no instances to upgrade - just skip the rest
else
    # restart running instances
    echo shutting down all instances . . . >> $output 2>&1 || :
    for inst in $instances ; do
        echo stopping instance $inst >> $output 2>&1 || :
        /bin/systemctl stop $inst >> $output 2>&1 || :
    done
    for inst in $instances ; do
        echo starting instance $inst >> $output 2>&1 || :
        /bin/systemctl start $inst >> $output 2>&1 || :
    done
fi


%preun
if [ $1 -eq 0 ]; then # Final removal
    # remove instance specific service files/links
    rm -rf %{_sysconfdir}/systemd/system/%{groupname}.wants/* > /dev/null 2>&1 || :
fi

%postun
if [ $1 = 0 ]; then # Final removal
    rm -rf /var/run/%{pkgname}
fi

%post snmp
%systemd_post %{pkgname}-snmp.service

%preun snmp
%systemd_preun %{pkgname}-snmp.service %{groupname}

%postun snmp
%systemd_postun_with_restart %{pkgname}-snmp.service

exit 0

%files -f plugins.list
%if %{with bundle_jemalloc}
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.jemalloc
%license COPYING.jemalloc
%else
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl
%endif
%dir %{_sysconfdir}/%{pkgname}
%dir %{_sysconfdir}/%{pkgname}/schema
%config(noreplace)%{_sysconfdir}/%{pkgname}/schema/*.ldif
%dir %{_sysconfdir}/%{pkgname}/config
%dir %{_sysconfdir}/systemd/system/%{groupname}.wants
%{_sysusersdir}/389-ds-base.conf
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/slapd-collations.conf
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/certmap.conf
%{_datadir}/%{pkgname}
%{_datadir}/gdb/auto-load/*
%{_unitdir}
%{_bindir}/dbscan
%{_mandir}/man1/dbscan.1.gz
%{_bindir}/ds-replcheck
%{_mandir}/man1/ds-replcheck.1.gz
%{bash_completions_dir}/ds-replcheck
%{_bindir}/ds-logpipe.py
%{_mandir}/man1/ds-logpipe.py.1.gz
%{_bindir}/ldclt
%{_mandir}/man1/ldclt.1.gz
%{_bindir}/logconv.pl
%{_mandir}/man1/logconv.pl.1.gz
%{_bindir}/pwdhash
%{_mandir}/man1/pwdhash.1.gz
%{_sbindir}/ns-slapd
%{_mandir}/man8/ns-slapd.8.gz
%{_sbindir}/openldap_to_ds
%{_mandir}/man8/openldap_to_ds.8.gz
%{_libexecdir}/%{pkgname}/ds_systemd_ask_password_acl
%{_libexecdir}/%{pkgname}/ds_selinux_restorecon.sh
%{_mandir}/man5/99user.ldif.5.gz
%{_mandir}/man5/certmap.conf.5.gz
%{_mandir}/man5/slapd-collations.conf.5.gz
%{_mandir}/man5/dirsrv.5.gz
%{_mandir}/man5/dirsrv.systemd.5.gz
%{_libdir}/%{pkgname}/python
%dir %{_libdir}/%{pkgname}/plugins
# This has to be hardcoded to /lib - $libdir changes between lib/lib64, but
# sysctl.d is always in /lib.
%{_prefix}/lib/sysctl.d/*
%dir %{_localstatedir}/lib/%{pkgname}
%dir %{_localstatedir}/log/%{pkgname}
%ghost %dir %{_localstatedir}/lock/%{pkgname}
%exclude %{_sbindir}/ldap-agent*
%exclude %{_mandir}/man1/ldap-agent.1.gz
%exclude %{_unitdir}/%{pkgname}-snmp.service
%if %{with bundle_jemalloc}
%{_libdir}/%{pkgname}/lib/
%{_libdir}/%{pkgname}/bin/
%exclude %{_libdir}/%{pkgname}/bin/jemalloc-config
%exclude %{_libdir}/%{pkgname}/bin/jemalloc.sh
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc.a
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc.so
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc_pic.a
%exclude %{_libdir}/%{pkgname}/lib/pkgconfig
%endif

%files devel
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%{_mandir}/man3/*
%{_includedir}/svrcore.h
%{_includedir}/%{pkgname}
%{_libdir}/libsvrcore.so
%{_libdir}/%{pkgname}/libslapd.so
%{_libdir}/%{pkgname}/libns-dshttpd.so
%{_libdir}/%{pkgname}/libldaputil.so
%{_libdir}/pkgconfig/svrcore.pc
%{_libdir}/pkgconfig/dirsrv.pc

%files libs
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%dir %{_libdir}/%{pkgname}
%{_libdir}/libsvrcore.so.*
%{_libdir}/%{pkgname}/libslapd.so.*
%{_libdir}/%{pkgname}/libns-dshttpd.so.*
%{_libdir}/%{pkgname}/libldaputil.so.*
%{_libdir}/%{pkgname}/librewriters.so*
%if %{with bundle_jemalloc}
%{_libdir}/%{pkgname}/lib/libjemalloc.so.2
%endif

%files snmp
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/ldap-agent.conf
%{_sbindir}/ldap-agent*
%{_mandir}/man1/ldap-agent.1.gz
%{_unitdir}/%{pkgname}-snmp.service

%if %{with bundle_libdb}
%files bdb
%doc LICENSE LICENSE.GPLv3+ README.devel LICENSE.libdb README.libdb lgpl-2.1.txt.libdb
%{_libdir}/%{pkgname}/%{libdb_bundle_name}
%{_libdir}/%{pkgname}/plugins/libback-bdb.so
%endif

%files -n python%{python3_pkgversion}-lib389
%doc LICENSE LICENSE.GPLv3+
%{python3_sitelib}/lib389*
%{_sbindir}/dsconf
%{_mandir}/man8/dsconf.8.gz
%{_sbindir}/dscreate
%{_mandir}/man8/dscreate.8.gz
%{_sbindir}/dsctl
%{_mandir}/man8/dsctl.8.gz
%{_sbindir}/dsidm
%{_mandir}/man8/dsidm.8.gz
%{_libexecdir}/%{pkgname}/dscontainer
%{bash_completions_dir}/dsctl
%{bash_completions_dir}/dsconf
%{bash_completions_dir}/dscreate
%{bash_completions_dir}/dsidm

%if %{with cockpit}
%files -n cockpit-389-ds -f cockpit.list
%{_datarootdir}/metainfo/389-console/org.port389.cockpit_console.metainfo.xml
%doc README.md
%endif

%changelog
%autochangelog
