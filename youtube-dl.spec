%global forgeurl https://github.com/ytdl-org/youtube-dl/
%global commit c5098961b04ce83f4615f2a846c84f803b072639

Name:           youtube-dl
Version:        2024.08.06.git%(c=%{commit}; echo ${c:0:7})
Release:        %{autorelease}
Summary:        A small command-line program to download online videos
License:        Unlicense
URL:	        %{forgeurl}
Source:         %{forgeurl}/archive/%{commit}/youtube-dl-%{commit}.tar.gz
Source3:        %{name}.conf
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-setuptools
# Tests failed because of no connection in Koji.
BuildArch:      noarch
BuildRequires:  pandoc
BuildRequires:  make
# https://bugzilla.redhat.com/show_bug.cgi?id=1951630
Recommends:     AtomicParsley
# https://bugzilla.redhat.com/show_bug.cgi?id=2203543
Recommends:     /usr/bin/ffmpeg

# https://github.com/ytdl-org/youtube-dl/pull/32188
Patch:    https://github.com/ytdl-org/youtube-dl/pull/32188.patch#./manpage-formatting.patch

%description
Small command-line program to download videos from YouTube and other sites.


%prep
%autosetup -p 1 -n youtube-dl-%{commit}

cp -a setup.py setup.py.installpath
# Remove files that are installed to the wrong path
sed -i '/youtube-dl.bash-completion/d' setup.py
sed -i '/youtube-dl.fish/d' setup.py
sed -i '/README.txt/d' setup.py

# Remove interpreter shebang from module files.
find youtube_dl -type f -exec sed -i -e '1{/^\#!\/usr\/bin\/env python$/d;};' {} +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
make PYTHON=python3



%install
%pyproject_install
%pyproject_save_files -l youtube_dl

install -Dpm644 %{S:3} -t %{buildroot}%{_sysconfdir}
install -Dpm644 youtube-dl.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/youtube-dl
install -Dpm644 youtube-dl.zsh %{buildroot}%{_datadir}/zsh/site-functions/_youtube-dl
install -Dpm644 youtube-dl.fish %{buildroot}%{_datadir}/fish/vendor_functions.d/youtube-dl.fish

%check
%pyproject_check_import

# This basically cannot work without massive .flake8rc
# starts with flake8 and of course no contributors bothered to make
# their code truly PEP8 compliant.
#
# make offlinetest


%files -f %{pyproject_files}
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf
# Bash completions
# %%{_datadir}/bash-completion/completions is owned by `filesystem`.
%{_datadir}/bash-completion/completions/%{name}
# Zsh completions
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_youtube-dl
# Fish completions
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/youtube-dl.fish

%changelog
%autochangelog
