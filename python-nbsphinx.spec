Name:           python-nbsphinx
Version:        0.9.5
Release:        %autorelease
Summary:        Jupyter Notebook Tools for Sphinx

# SPDX
License:        MIT
URL:            http://nbsphinx.rtfd.io/
Source0:        %{pypi_source nbsphinx}
Patch0:         allow-errors-in-notebooks-with-external-images.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-ipykernel
BuildRequires:  python3-ipython-sphinx
BuildRequires:  python3-jupyter-client
BuildRequires:  python3-matplotlib
BuildRequires:  python3-nbconvert
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-bibtex
BuildRequires:  python3-sphinx-copybutton
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  python3-sphinx-gallery
BuildRequires:  python3-sphinx-last-updated-by-git
BuildRequires:  git-core
BuildRequires:  pandoc

%description
nbsphinx is a Sphinx extension that provides a source parser for *.ipynb
files. Custom Sphinx directives are used to show Jupyter Notebook code cells
(and of course their results) in both HTML and LaTeX output. Unevaluated
notebooks, i.e. notebooks without stored output cells, will be automatically
executed during the Sphinx build process.

%package -n     python3-nbsphinx
Summary:        %{summary}

%description -n python3-nbsphinx
nbsphinx is a Sphinx extension that provides a source parser for *.ipynb
files. Custom Sphinx directives are used to show Jupyter Notebook code cells
(and of course their results) in both HTML and LaTeX output. Unevaluated
notebooks, i.e. notebooks without stored output cells, will be automatically
executed during the Sphinx build process.

%package -n python-nbsphinx-doc
Summary:        nbsphinx documentation
%description -n python-nbsphinx-doc
Documentation for nbsphinx

%prep
%autosetup -n nbsphinx-%{version} -S git
# Disables custom formatter not available in Fedora.
# The result is that pages:
# https://nbsphinx.readthedocs.io/en/0.8.6/a-markdown-file.html
# https://nbsphinx.readthedocs.io/en/0.8.6/custom-formats.html
# are not available.
# TODO: package jupytext
sed -i "/\['jupytext.reads', {'fmt'/d" doc/conf.py
# Delete the Sphinx extension we don't have packaged in Fedora
# This extension links the code examples to their respective documentation,
# its absence doesn't break the nbsphinx' docs
sed -i "/'sphinx_codeautolink',  # automatic links from code to documentation/d" doc/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# fake the git tag for docs to put the right version in
git tag %{version}
# ignore errors - nbsphinx cannot load images from Internet
echo "nbsphinx_allow_errors = True" >> doc/conf.py
# generate html docs 
PYTHONPATH=build/lib sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/{.doctrees,.buildinfo,conf.py,_sources}

%install
%pyproject_install
%pyproject_save_files -l nbsphinx


%check
%pyproject_check_import


%files -n python3-nbsphinx -f %{pyproject_files}
%doc README.rst

%files -n python-nbsphinx-doc
%license LICENSE
%doc html 

%changelog
%autochangelog
