Name:           python-xlrd2
Version:        1.3.4
Release:        2%{?dist}
Summary:        Library to extract data from Microsoft Excel legacy spreadsheet files (xls)

License:        Apache-2.0 AND BSD-3-Clause AND BSD-Advertising-Acknowledgement
URL:            https://github.com/DissectMalware/xlrd2
Source0:        https://github.com/DissectMalware/xlrd2/releases/download/v%{version}/xlrd2-%{version}.tar.gz

# https://github.com/DissectMalware/xlrd2/issues/11
# Patch0:         https://patch-diff.githubusercontent.com/raw/DissectMalware/xlrd2/pull/12.patch#/python-xlrd2-00-xmlengine.patch
Patch1:         https://patch-diff.githubusercontent.com/raw/python-excel/xlrd/pull/375.patch#/python-xlrd2-01-defusedxmliter.patch

# documentation having example to xlrd instead of xlrd2
Patch2:         https://github.com/DissectMalware/xlrd2/pull/14.patch#/python-xlrd2-02-rename.patch

BuildArch:      noarch

%global pypi_name xlrd2
# macro is not defined on rhel7
%{!?pytest: %global pytest pytest-3}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-pytest

%if (0%{?fedora}) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
# pkginfo used for generating the documentation, missing on rhel7
BuildRequires:  python%{python3_pkgversion}-pkginfo
%endif

%global common_description %{expand:
The xlrd2 module is an effort to extend [xlrd project]( which is no longer
maintained by its developers). The main goal is to make it suitable for
extracting necessary information from malicious xls documents.
**Xlrd Purpose**: Provide a library for developers to use to extract data
from Microsoft Excel (tm) spreadsheet files.
It is not an end-user tool.
}

%description %common_description


%package -n     python%{python3_pkgversion}-xlrd2
Summary:        %{summary}
%description -n python%{python3_pkgversion}-xlrd2 %common_description
%if 0%{?rhel}
%{?python_provide:%python_provide python%{python3_pkgversion}-xlrd2}
%else
%py_provides    python3-xlrd2
%endif


%package -n python-xlrd2-doc
Summary:        The documentation for python module xlrd2
%description -n python-xlrd2-doc
The Documentation for the python module xlrd2
%common_description


%prep
%autosetup -p 1 -n xlrd2-%{version}
# Remove bundled egg-info
rm -rf .egg-info

# Fix CRLF ends of lines
echo "=== Fixing CRLF ends of lines for all text files"
find ./ -type f '!' '(' -name '*.xls' -o -name '*.xlsx' ')' -print -exec sed '-i' '-e' 's/\r$//' '{}' ';'



%generate_buildrequires
%pyproject_buildrequires



%build
# package doesn't support pyproject yet
%pyproject_wheel

%if (0%{?fedora}) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
# on rhel7 there is missing package python3-pkginfo
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
%endif

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files -l xlrd2


%check
%pyproject_check_import

%pytest -sv -k "not test_names_demo"


%files -n python%{python3_pkgversion}-xlrd2 -f %{pyproject_files}
%doc README.md
%{_bindir}/runxlrd2.py

# on rhel7 there is missing package python3-pkginfo
%files -n python-xlrd2-doc
%license LICENSE docs/licenses.rst
%if (0%{?fedora}) || ( 0%{?rhel} && 0%{?rhel} >= 8 ) 
%doc html
%endif
%doc examples

%changelog
* Thu Aug 01 2024 Michal Ambroz <rebus@seznam.cz> - 1.3.4-2
- fix license metadata
- fix typo in description
- remove duplicate license file

* Sat Dec 10 2022 Michal Ambroz <rebus@seznam.cz> - 1.3.4-1
- Initial package.
