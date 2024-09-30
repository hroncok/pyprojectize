Name:          diffoscope
Version:       271
Release:       %autorelease
Summary:       In-depth comparison of files, archives, and directories
License:       GPL-3.0-or-later
URL:           https://diffoscope.org/
#Source0:       https://files.pythonhosted.org/packages/source/d/diffoscope/diffoscope-%%{version}.tar.gz
Source0:       https://salsa.debian.org/reproducible-builds/diffoscope/-/archive/%{version}/diffoscope-%{version}.tar.gz

# The package is arched due to architecture-dependent BR’s and Recommends;
# however, there is no compiled code, so no debug package will be generated.
%global debug_package %{nil}

ExcludeArch:  %{ix86}

%global tools \
    acl \
    abootimg \
    black \
    e2fsprogs \
    cpio \
    llvm, llvm-devel \
    binutils \
    binwalk \
    diffutils \
    html2text \
    gzip \
    unzip \
    bzip2 \
    xz \
    tar \
    zip \
    p7zip \
    sng >= 1.1.0-2 \
    openssl \
    openssh \
    openssh-clients \
    radare2 \
    sqlite \
    genisoimage \
    squashfs-tools \
    /usr/bin/img2txt \
    /usr/bin/rpm2cpio \
    /usr/bin/msgunfmt \
    /usr/bin/ps2ascii \
    /usr/bin/qemu-img \
    /usr/bin/xxd \
    /usr/bin/ghc \
    /usr/bin/cd-iccdump \
    /usr/bin/oggDump \
    /usr/bin/Rscript \
    /usr/bin/fdtdump \
    /usr/bin/gifbuild \
    /usr/bin/dumppdf \
    /usr/bin/h5dump \
    gnupg \
    pgpdump \
    findutils \
    file \
    ImageMagick \
    poppler-utils \
    python3-argcomplete \
    python3-debian \
    python3-h5py \
    python3-magic \
    python3-pdfminer \
    python3-tlsh \
    python3-libarchive-c \
    python3-libguestfs \
    python3-rpm \
    gnumeric \
    odt2txt \
    wabt

# missing:
# aapt
# apktool
# js-beautify
# /usr/bin/dumpxsb from xmlbeans-scripts, xmlbeans
# docx2txt
# dexdump

# Does not work with python3-PyPDF2-1.26.0
# python3-pypdf >= 3.0
# https://bugzilla.redhat.com/show_bug.cgi?id=2073259

%ifnarch ppc64 ppc64le
%global tools2 \
    mono-devel
%endif
%ifarch x86_64 i686 armv7hl
%global tools3 \
    fpc
%endif
%ifnarch s390x
%global tools4 \
    /usr/bin/dumpimage
%endif
%ifarch %{java_arches}
%global tools5 \
    procyon
%endif

%global toolz %(echo "%tools %?tools2 %?tools3 %?tools4 %?tools5" | grep . | tr '\\n' ', ')

BuildRequires: python3-devel
BuildRequires: python3-docutils
# for tests
BuildRequires: python3-pytest
BuildRequires: %toolz
BuildRequires: help2man
BuildRequires: make
BuildRequires: git
%ifarch %{java_arches}
BuildRequires: java-devel
%endif

Recommends:    %toolz

%description
diffoscope will try to get to the bottom of what makes files or directories
different. It will recursively unpack archives of many kinds and transform
various binary formats into more human readable form to compare them. It can
compare two tarballs, ISO images, or PDF just as easily. The differences can
be shown in a text or HTML report.

diffoscope is developed as part of the "reproducible builds" Debian project and
was formerly known as "debbindiff".

%prep
%autosetup -p1 -Sgit
sed -i '1{\@/usr/bin/env@d}' diffoscope/main.py

# We use the python3-file-magic module instead of the python3-magic module.
# They conflict, and python3-file-magic is required by rpmlint.
sed -i s/python-magic/file-magic/ setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
make -C doc

%install
%pyproject_install
%pyproject_save_files 'diffoscope*'
echo %{buildroot}%{python3_sitelib}
install -Dm0644 -t %{buildroot}%{_mandir}/man1/ doc/diffoscope.1
install -Dm0644 -t %{buildroot}/usr/share/zsh/site-functions/ debian/zsh-completion/_diffoscope

%check
DESELECT=(
  # s390x specific issue?
  --deselect=tests/comparators/test_ogg.py::test_diff
  --deselect=tests/comparators/test_ogg.py::test_compare_non_existing
  --deselect=tests/test_tools.py::test_sbin_added_to_path
  --deselect=tests/comparators/test_python.py::test_diff

  # What exactly is the point of those tests?
  --deselect=tests/test_source.py::test_code_is_black_clean

  # Those fail on rawhide. Not reported upstream yet.
  --deselect=tests/comparators/test_fsimage.py::test_differences
  --deselect=tests/comparators/test_fsimage.py::test_differences_fat
  --deselect=tests/comparators/test_elf.py::test_differences_with_dbgsym
  --deselect=tests/comparators/test_elf.py::test_original_gnu_debuglink

  # Those seem to depend on the 'file' implementation, ignore.
  --deselect=tests/comparators/test_html.py::test_diff
  --deselect=tests/comparators/test_text.py::test_text_fallback
)

LC_CTYPE=C.utf8 \
TZ=UTC \
PYTHONPATH=build/lib/ \
%python3 -m pytest tests/ -vv "${DESELECT[@]}"

%files -f %{pyproject_files}
%doc README.rst debian/changelog
%license COPYING
%{_bindir}/diffoscope
/usr/share/zsh/site-functions/_diffoscope
%doc %{_mandir}/man1/diffoscope.1*

%changelog
%autochangelog
