%global pypi_name artifacts
%global date 20240518

Name:           %{pypi_name}
Version:        0.0.%{date}
Release:        %autorelease
Summary:        Collection of digital forensic artifacts

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/ForensicArtifacts/artifacts
Source0:        %{url}/releases/download/%{date}/%{pypi_name}-%{date}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml

%description
A free, community-sourced, machine-readable knowledge base of digital
forensic artifacts that the world can use both as an information source
and within other tools.

If you'd like to use the artifacts in your own tools, all you need to be
able to do is read YAML. That is it, no other dependencies. The Python
code in this project is just used to validate all the artifacts to make
sure they follow the specification.

%prep
%autosetup -n %{pypi_name}-%{date}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{_defaultdocdir}/%{pypi_name}/LICENSE

%check
PYTHONPATH=%{buildroot}/%{python3_sitelib}/ pytest-%{python3_version} -v tests

%files
%doc ACKNOWLEDGEMENTS AUTHORS README
%license LICENSE
%{_bindir}/{stats,validator}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{date}*.dist-info

%changelog
%autochangelog

