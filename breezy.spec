# All package versioning is found here:
# the actual version is composed from these below
#   bzrmajor:  main bzr version
#   Version: bzr version, add subrelease version here
%global brzmajor 3.3
%global brzminor .8

Name:           breezy
Version:        %{brzmajor}%{?brzminor}
Release:        %autorelease
Summary:        Friendly distributed version control system

# breezy is GPL-2.0-or-later, but it has Rust dependencies
# see packaged LICENSE.dependencies for details
License:        GPL-2.0-or-later AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND Apache-2.0 AND MIT AND (Unlicense OR MIT)
URL:            http://www.breezy-vcs.org/
Source0:        https://launchpad.net/brz/%{brzmajor}/%{version}%{?brzrc}/+download/%{name}-%{version}%{?brzrc}.tar.gz
Source1:        https://launchpad.net/brz/%{brzmajor}/%{version}%{?brzrc}/+download/%{name}-%{version}%{?brzrc}.tar.gz.asc
Source2:        brz-icon-64.png

BuildRequires:  python3-devel
BuildRequires:  rust-packaging >= 21
BuildRequires:  zlib-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make

# This is the name of the command, note that it is brz, not bzr
Provides:       brz = %{version}-%{release}

# breezy is a fork of bzr and replaces it
Provides:       bzr = %{version}-%{release}
Obsoletes:      bzr < 3
Provides:       git-remote-bzr = %{version}-%{release}
Obsoletes:      git-remote-bzr < 3

# This is needed for launchpad support
Recommends:     python3-launchpadlib

# Docs are not needed, but some might want them
Suggests:       %{name}-doc = %{version}-%{release}

%description
Breezy (brz) is a decentralized revision control system, designed to be easy
for developers and end users alike.

By default, Breezy provides support for both the Bazaar and Git file formats.


%package doc
Summary:        Documentation for Breezy
License:        GPL-2.0-or-later
BuildArch:      noarch

%description doc
This package contains the documentation for the Breezy version control system.

%prep
%autosetup -p1 -n %{name}-%{version}%{?brzrc}

%cargo_prep

# Remove unused shebangs
sed -i '1{/#![[:space:]]*\/usr\/bin\/\(python\|env\)/d}' \
    breezy/__main__.py \
    breezy/git/git_remote_helper.py \
    breezy/git/tests/test_git_remote_helper.py \
    breezy/plugins/bash_completion/bashcomp.py \
    breezy/plugins/zsh_completion/zshcomp.py \
    breezy/tests/ssl_certs/create_ssls.py \
    contrib/brz_access

# Remove Cython generated .c files
find . -name '*_pyx.c' -exec rm \{\} \;


%generate_buildrequires
%cargo_generate_buildrequires
%pyproject_buildrequires -x doc


%build
%py3_build

chmod a-x contrib/bash/brzbashprompt.sh

# Build documents
make docs-sphinx PYTHON=%{__python3}
rm doc/*/_build/html/.buildinfo
rm -f doc/*/_build/html/_static/*/Makefile
pushd doc
for dir in *; do
  test -d $dir/_build/html && mv $dir/_build/html ../$dir
done
popd

# Add Rust licenses
%{cargo_license} > LICENSE.dependencies

%install
%py3_install
chmod -R a+rX contrib
chmod 0644 contrib/debian/init.d
chmod 0644 contrib/bzr_ssh_path_limiter  # note the bzr here
chmod 0644 contrib/brz_access
chmod 0755 %{buildroot}%{python3_sitearch}/%{name}/*.so

install -Dpm 0644 contrib/bash/brz %{buildroot}%{bash_completions_dir}/brz
rm contrib/bash/brz

install -d %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/brz.png

# weird man page location
mv %{buildroot}%{_prefix}/man %{buildroot}%{_datadir}

# move git-remote-bzr to avoid conflict
mv %{buildroot}%{_bindir}/git-remote-bzr %{buildroot}%{_bindir}/git-remote-brz
mv %{buildroot}%{_mandir}/man1/git-remote-bzr.1 %{buildroot}%{_mandir}/man1/git-remote-brz.1

# backwards compatible symbolic links
ln -s brz %{buildroot}%{_bindir}/bzr
ln -s git-remote-brz %{buildroot}%{_bindir}/git-remote-bzr
echo ".so man1/brz.1" > %{buildroot}%{_mandir}/man1/bzr.1
echo ".so man1/git-remote-brz.1" > %{buildroot}%{_mandir}/man1/git-remote-bzr.1

# locales are generated to a weird directory, move them to datadir
mv %{buildroot}%{buildroot}%{_datadir}/locale %{buildroot}%{_datadir}
%find_lang %{name}

%files -f %{name}.lang
%license COPYING.txt LICENSE.dependencies
%doc NEWS README.rst TODO contrib/
%{_bindir}/brz
%{_bindir}/bzr-*-pack
%{_bindir}/git-remote-brz
%{_bindir}/bzr
%{_bindir}/git-remote-bzr
%{_mandir}/man1/*
%{python3_sitearch}/%{name}/
%{python3_sitearch}/*.egg-info/
%{bash_completions_dir}/brz
%{_datadir}/pixmaps/brz.png


%files doc
%license COPYING.txt LICENSE.dependencies
%doc en developers


%changelog
%autochangelog
