%global srcname jupyter-c-kernel
%global srcname_ jupyter_c_kernel

Name:           python-%{srcname}
Version:        1.2.2
Release:        24%{?dist}
Summary:        Minimalistic C kernel for Jupyter

License:        MIT
URL:            https://github.com/brendan-rius/jupyter-c-kernel
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname_}/%{srcname_}-%{version}.tar.gz
# https://github.com/brendan-rius/jupyter-c-kernel/pull/46
Source1:        README.md
Source2:        LICENSE.txt
# https://github.com/brendan-rius/jupyter-c-kernel/pull/47
Patch0001:      0001-Use-tempfile-instead-of-IPython-to-get-a-temp-dir.patch
 
BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global _description \
%{summary}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-jupyter-client

Requires:       gcc
Requires:       python3-jupyter-client
Requires:       python3-ipykernel

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname_}-%{version} -p1
cp -p %SOURCE1 %SOURCE2 .



%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname_}

%{__python3} %{buildroot}%{_bindir}/install_c_kernel --prefix %{buildroot}%{_prefix}
rm %{buildroot}%{_bindir}/install_c_kernel


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_datadir}/jupyter/kernels/c


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.2.2-23
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.2.2-19
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-17
- Drop support for i686

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.2.2-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.2-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-1
- Initial package.
