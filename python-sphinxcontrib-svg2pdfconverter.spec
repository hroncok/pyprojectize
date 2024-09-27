%global srcname sphinxcontrib-svg2pdfconverter

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        Sphinx SVG to PDF Converter Extension

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.org/project/sphinxcontrib-svg2pdfconverter/
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildArch:      noarch

%description
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).


%package -n python3-%{srcname}-common
Summary:        Sphinx SVG to PDF Converter Extension - common files

%description -n python3-%{srcname}-common
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains common files.


%package -n python3-sphinxcontrib-inkscapeconverter
Summary:        Sphinx SVG to PDF Converter Extension - Inkscape converter

Requires:       /usr/bin/inkscape
Requires:       python3-%{srcname}-common = %{version}-%{release}

%if 0%{?fedora} == 32
%py_provides python3-sphinxcontrib-inkscapeconverter
%endif

%description -n python3-sphinxcontrib-inkscapeconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using Inkscape.


%package -n python3-sphinxcontrib-rsvgconverter
Summary:        Sphinx SVG to PDF Converter Extension - libRSVG converter

Requires:       /usr/bin/rsvg-convert
Requires:       python3-%{srcname}-common = %{version}-%{release}

%if 0%{?fedora} == 32
%py_provides python3-sphinxcontrib-rsvgconverter
%endif

%description -n python3-sphinxcontrib-rsvgconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using libRSVG.


%package -n python3-sphinxcontrib-cairosvgconverter
Summary:        Sphinx SVG to PDF Converter Extension - CairoSVG converter

Requires:       %{py3_dist CairoSVG}
Requires:       python3-%{srcname}-common = %{version}-%{release}

%if 0%{?fedora} == 32
%py_provides python3-sphinxcontrib-cairosvgconverter
%endif

%description -n python3-sphinxcontrib-cairosvgconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using CairoSVG.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


#check
#{__python3} setup.py test


# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}-common
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/sphinxcontrib_svg2pdfconverter*nspkg.pth
%{python3_sitelib}/sphinxcontrib_svg2pdfconverter-*.egg-info


%files -n python3-sphinxcontrib-inkscapeconverter
%{python3_sitelib}/sphinxcontrib/__pycache__/inkscapeconverter.*.pyc
%{python3_sitelib}/sphinxcontrib/inkscapeconverter.py


%files -n python3-sphinxcontrib-rsvgconverter
%{python3_sitelib}/sphinxcontrib/__pycache__/rsvgconverter.*.pyc
%{python3_sitelib}/sphinxcontrib/rsvgconverter.py


%files -n python3-sphinxcontrib-cairosvgconverter
%{python3_sitelib}/sphinxcontrib/__pycache__/cairosvgconverter.*.pyc
%{python3_sitelib}/sphinxcontrib/cairosvgconverter.py


%changelog
%autochangelog
