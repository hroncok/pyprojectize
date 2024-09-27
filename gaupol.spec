%bcond tests 1

Name:           gaupol
Version:        1.15
Release:        %autorelease
Summary:        Editor for text-based subtitle files

# Everything is GPL-3.0-or-later, except:
#   - data/io.otsaloma.gaupol.appdata.xml.in is CC0-1.0, which is allowed for
#     content only
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://otsaloma.io/gaupol/
%global forgeurl https://github.com/otsaloma/gaupol
Source:         %{forgeurl}/archive/%{version}/gaupol-%{version}.tar.gz

BuildArch:      noarch

# We cannot use dynamic BuildRequires or automatic Requires generation, as
# setup.py does not have the relevant metadata. We must do it the old-fashioned
# way, by perusing READMEs, plus grepping source and inspecting imports.
BuildRequires:  python3-devel

# This package still uses distutils (with heavy customization, so it cannot be
# trivially ported to setuptools).
#
# In Python 3.12, distutils is removed from the standard library:
#
#   Remove the distutils package. It was deprecated in Python 3.10 by PEP 632
#   “Deprecate distutils module”. For projects still using distutils and cannot
#   be updated to something else, the setuptools project can be installed: it
#   still provides distutils. (Contributed by Victor Stinner in gh-92584.)
#
# We must therefore BuildRequire python3dist(setuptools) to get distutils.
BuildRequires:  python3dist(setuptools)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# For AppData file validation
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

%if %{with tests}
BuildRequires:  python3dist(pygobject) >= 3.12
BuildRequires:  gtk3 >= 3.12
# The gstreamer and mpv weak dependencies are not actually used in the tests,
# but we BuildRequire them anyway to make sure they are satisfiable.
BuildRequires:  gstreamer1 >= 1.6
BuildRequires:  gstreamer1-plugins-base >= 1.6
BuildRequires:  gstreamer1-plugins-good >= 1.6
BuildRequires:  gstreamer1-plugins-good-gtk >= 1.6
BuildRequires:  gstreamer1-vaapi >= 1.6
# svt-av1 is ExclusiveArch: x86_64
BuildRequires:  (gstreamer1-svt-av1 if python3(x86-64))
# svt-vp9 is ExclusiveArch: x86_64
BuildRequires:  (gstreamer1-svt-vp9 if python3(x86-64))
BuildRequires:  mpv
BuildRequires:  iso-codes
BuildRequires:  gspell >= 1.0.0
BuildRequires:  (python3dist(charset-normalizer) with python3dist(charset-normalizer) > 2)

BuildRequires:  python3dist(pytest)
# Support graphical tests in non-graphical environment
BuildRequires:  xorg-x11-server-Xvfb
%endif

# For /usr/share/icons/hicolor/{scalable,symbolic}/apps
Requires:  hicolor-icon-theme

Requires:       python3dist(pygobject) >= 3.12
Requires:       gtk3 >= 3.12
Requires:       iso-codes
Recommends:     gstreamer1
Requires:       (gstreamer1 >= 1.6 if gstreamer1)
Recommends:     gstreamer1-plugins-base
Requires:       (gstreamer1-plugins-base >= 1.6 if gstreamer1-plugins-base)
Recommends:     gstreamer1-plugins-good
Requires:       (gstreamer1-plugins-good >= 1.6 if gstreamer1-plugins-good)
Recommends:     gstreamer1-plugins-good-gtk
Requires:       (gstreamer1-plugins-good-gtk >= 1.6 if gstreamer1-plugins-good-gtk)
Recommends:     gstreamer1-vaapi
Requires:       (gstreamer1-vaapi >= 1.6 if gstreamer1-vaapi)
# svt-av1 is ExclusiveArch: x86_64
Recommends:     (gstreamer1-svt-av1 if python3(x86-64))
# svt-vp9 is ExclusiveArch: x86_64
Recommends:     (gstreamer1-svt-vp9 if python3(x86-64))
# Default preview video player on non-Windows systems, and currently (of mpv,
# mplayer, and VLC) the only one packaged in Fedora.
Recommends:     mpv
Recommends:     gspell
Requires:       (gspell >= 1.0.0 if gspell)

Requires:       python3-aeidon = %{version}-%{release}

Summary(cs):    Editor pro textově založené titulky
Summary(de):    Editor für textbasierte Untertitel
Summary(es):    Editor de archivos de subtítulos basados en texto
Summary(fi):    Muokkain tekstimuotoisille tekstityksille
Summary(fr):    Éditeur de sous-titres au format texte
Summary(ie):    Un redactor por textual subtitules
Summary(is):    Ritill fyrir skjátexta á textaformi
Summary(nl):    Bewerker voor op tekst gebaseerde ondertitels
Summary(pl):    Edytor napisów tekstowych
Summary(pt_BR): Editor para legendas em texto
Summary(pt):    Editor para legendas em texto
Summary(ru):    Редактор текстовых субтитров
Summary(tr):    Metin tabanlı altyazılar için düzenleyici
Summary(zh_CN): 基于文本的字幕编辑器

%global app_id io.otsaloma.gaupol

%description
Gaupol is an editor for text-based subtitle files. It supports multiple
subtitle file formats and provides means of creating subtitles, editing texts
and timing subtitles to match video.

%description -l cs
Gaupol je editor pro textově založené soubory titulků. Podporuje více formátů
souborů titulků a poskytuje prostředky k vytváření titulků, upravování textů a
časování titulků, aby odpovídaly obrazovému záznamu.

%description -l de
Gaupol ist ein Editor für textbasierte Untertiteldateien. Er unterstützt
mehrere Untertiteldateiformate und ermöglicht das Erstellen von Untertiteln,
Textbearbeitung und die zeitliche Anpassung von Untertiteln an das Video.

%description -l es
Gaupol es un editor de archivos de subtítulos basados en texto. Con soporte
para diversos formatos de archivos, proporciona los medios para crear
subtítulos, manipular líneas y sincronizar subtítulos a un vídeo.

%description -l fi
Gaupol on muokkain tekstimuotoisille tekstitystiedostoille. Se tukee useita eri
tekstitystiedostomuotoja ja tarjoaa toimintoja tekstitysten luomiseen, tekstien
muokkaamiseen ja tekstitysten ajoittamiseen videoon sovittaen.

%description -l fr
Gaupol est un éditeur de sous-titres au format texte. Il supporte de nombreux
formats de sous-titres et permet de créer, des sous-titres, d’éditer du texte,
et de synchroniser les sous-titres à une vidéo.

%description -l ie
Gaupol es un redactor por files de textual subtitules. It supporta multiplic
formates de file e permisse vos crear, redacter e colocar subtitules secun un
video.

%description -l is
Gaupol er ritill til meðhöndlunar á skjátextaskrám á textaformi. Hann styður
margar gerðir skjátextaskráa og býður upp á að útbúa nýja skjátexta, breytingar
texta og tímasetningu þeirra svo að þeir samsvari myndskeiðum.

%description -l nl
Gaupol is een bewerker voor op tekst gebaseerde ondertitels. Gaupol ondersteunt
meerdere soorten ondertitelformaten, en kan ook worden gebruikt om nieuwe
ondertitels te maken, teksten aan te passen en ondertitels te timen met
video’s.

%description -l pl
Gaupol to edytor tekstowych plików napisów. Obsługuje wiele formatów plików
napisów i zapewnia środki do tworzenia napisów, edycji tekstów i synchronizacji
napisów w celu dopasowania do wideo.

%description -l pt_BR
Gaupol é um editor de arquivos de legendas em texto. Ele possui suporte a
vários formatos de arquivo de legenda e fornece meios de criar legendas, editar
textos e legendas de tempo para corresponder ao vídeo.

%description -l pt
O Gaupol é um editor de ficheiros de legendas em texto. Possui suporte a vários
formatos de ficheiro de legenda e fornece meios de criar legendas, editar
textos e legendas de tempo para corresponder ao vídeo.

%description -l ru
Gaupol - редактор для текстовых субтитров. Он поддерживает множество форматов
файлов субтитров и предоставляет средства для их создания, редактирования и
синхронизации с видео.

%description -l tr
Gaupol, metin tabanlı altyazı dosyaları için bir düzenleyicidir. Birçok altyazı
dosya biçimini destekler ve video eşleştirmek için altyazı oluşturma, metinleri
düzenleme ve altyazıları zamanlama araçları sağlar.

%description -l zh_CN
Gaupol 是一个编辑基于文本的字幕编辑器。它支持多种字幕文件格式，
并提供创建字幕、编辑文本和调整字幕时间轴以匹配视频等功能。


%package -n python3-aeidon
Summary: Read, write, and manipulate text-based subtitle files

Provides:       aeidon = %{version}-%{release}
Obsoletes:      aeidon <= 1.4-11
Conflicts:      aeidon <= 1.4-11

Requires:       iso-codes
Requires:       (python3dist(charset-normalizer) with python3dist(charset-normalizer) > 2)

%description -n python3-aeidon
aeidon is a Python package that provides classes and functions for dealing with
text-based subtitle files of many different formats. Functions exist for
reading and writing subtitle files as well as manipulating subtitle data, i.e.
positions (times or frames) and texts.

The aeidon package is part of the Gaupol subtitle editor, where the other
package, gaupol, provides the GTK user interface.

Separating a user interface independent general-purpose subtitle editing
package from Gaupol has been an afterthought and thus not well designed to be a
reusable component, but on the other hand is proven, working and maintained
code.

API documentation: https://otsaloma.io/gaupol/doc/api/aeidon.html


%prep
%autosetup -p1
# Remove bundled iso-codes:
find data/iso-codes -type f -name '*.json' |
  while read -r fn
  do
    ln -svf "/usr/share/iso-codes/json/$(basename "${fn}")" "${fn}"
  done
# We want to install the Markdown docs in a subdirectory of the package
# documentation directory; copy them to a directory of the desired name.
cp -vrp doc using-gaupol


%build
%py3_build


%install
# From README.aeidon.md:
#
#   When packaging both aeidon and gaupol in a Linux distro, it's best to use
#   the switches in the main `setup.py` for a consistent whole.
#
#       sudo python3 setup.py --without-gaupol install --prefix=/usr/local
#       sudo python3 setup.py --without-aeidon install --prefix=/usr/local
%global py_setup_args --without-iso-codes --without-gaupol
%py3_install
%global py_setup_args --without-iso-codes --without-aeidon
%py3_install

%find_lang gaupol
desktop-file-install \
    --dir='%{buildroot}%{_datadir}/applications' \
    --delete-original \
    --add-category='AudioVideoEditing' \
    '%{buildroot}/%{_datadir}/applications/%{app_id}.desktop'


%check
if [ "$(find data/iso-codes -type f ! -name 'README*' | wc -l)" != 0 ]
then
  echo 'Failed to fully remove bundled iso-codes' 1>&2
  false
fi
# Validate the installed AppData file. Fedora guidelines require validate-relax
# to pass (but not validate-strict), and do require validation at build time.
#
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    '%{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml'
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    '%{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml'

%if %{with tests}
%global __pytest xvfb-run -a pytest
# The skipped test passes in a real Fedora desktop session, but fails under
# xvfb; we do not understand why, although it smells like a trivial font
# issue.
%pytest -k 'not (TestModule and test_char_to_px__font)'
%endif


%files -f gaupol.lang
%license COPYING
%doc AUTHORS.md
%doc README.md
%doc NEWS.md
%doc using-gaupol

%{_bindir}/gaupol

%{python3_sitelib}/gaupol/
%{python3_sitelib}/gaupol-%{version}-py%{python3_version}.egg-info/

%{_datadir}/gaupol/
%{_metainfodir}/%{app_id}.appdata.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/symbolic/apps/%{app_id}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_mandir}/man1/gaupol.1*


%files -n python3-aeidon
%license COPYING
%doc AUTHORS.md
%doc README.aeidon.md
%doc NEWS.md

%{python3_sitelib}/aeidon/
%{python3_sitelib}/aeidon-%{version}-py%{python3_version}.egg-info/


%changelog
%autochangelog
