%global pypi_name qudida

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        5%{?dist}
Summary:        QuDiDA (QUick and DIrty Domain Adaptation)

License:        MIT
URL:            https://github.com/arsenyinfo/qudida
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

Patch0:         001_setup_py.patch

BuildRequires:  python3-devel

# Tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(opencv)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(typing-extensions)

%global _description \
QuDiDA is a micro library for very naive though quick pixel level image domain \
adaptation via scikit-learn transformers. \
Is assumed to be used as image augmentation technique, \
while was not tested in public benchmarks.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%{python3_sitelib}/%{pypi_name}/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.0.4-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.0.4-1
- initial package
