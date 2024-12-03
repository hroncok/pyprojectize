Summary:       Debugger using ptrace written in Python
Name:          python-ptrace
Version:       0.9.9
Release:       4%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           https://github.com/vstinner/python-ptrace
Source0:       https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: python3-devel
%global _description \
python-ptrace is a debugger using ptrace written in Python. \
Features: \
 o High level Python object API : PtraceDebugger and PtraceProcess \
 o Able to control multiple processes: catch fork events on Linux \
 o Read/write bytes to arbitrary address: take care of memory alignment \
   and split bytes to cpu word \
 o Execution step by step using ptrace_singlestep() \
   or hardware interruption 3 \
 o Dump registers, memory mappings, stack, etc. \
 o Syscall tracer and parser (strace.py command) \
 o Can use distorm disassembler (if available)
%description %_description
%package    -n python3-ptrace
Summary:       Debugger using ptrace written in Python 3
%description -n python3-ptrace %_description

%prep
%autosetup
chmod 0644 examples/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}
%{__python3} setup_cptrace.py build

%install
%{pyproject_install}
%pyproject_save_files -l cptrace ptrace
%{__python3} setup_cptrace.py install -O1 --skip-build --root %{buildroot}

rm -f %{buildroot}%{_bindir}/{gdb,strace}.{pyo,pyc}

%check
%pyproject_check_import

%{__python3} runtests.py || :

%files -n python3-ptrace -f %{pyproject_files}
%doc README.rst
%doc doc/* examples
%{_bindir}/gdb.py
%{_bindir}/strace.py

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.9-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.9-2
- Rebuilt for Python 3.13

* Wed Mar 13 2024 Terje Rosten <terje.rosten@ntnu.no> - 0.9.9-1
- 0.9.9

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 09 2023 Terje Rosten <terje.rosten@oracle.com> - 0.9.8-9
- Avoid use of imp

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.8-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.8-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.8-2
- Rebuilt for Python 3.10

* Thu Mar 18 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.9.8-1
- 0.9.8
- Remove leagcy Python 2 bits

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.9.7-1
- 0.9.7

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.9.5-1
- 0.9.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-3
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-2
- No Python 2 in newer Fedoras

* Sun Aug 18 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-1
- 0.9.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.9.3-6
- Use correct python macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Oct 01 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.9.3-1
- 0.9.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 09 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.9.2-1
- 0.9.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-1
- 0.8.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.6-5
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Jan 20 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.6.6-2
- Patch still needed

* Mon Jan 20 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.6.6-1
- 0.6.6

* Sun Oct 27 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.6.5-1
- 0.6.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.6.4-2
- Add patch to build with Python 3.3

* Wed Dec 05 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.6.4-1
- 0.6.4
- Add python 3 subpackage

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.6.3-1
- 0.6.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 11 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Dec 05 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6.2-1
- 0.6.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  8 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6-4
- Build with all rpm versions

* Sun Mar  8 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6-3
- Remove %%exclude

* Thu Mar  5 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6-2
- switch to %%global, fix files listing, remove comments

* Wed Mar  4 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6-1
- 0.6

* Sat Sep 13 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.5-1
- 0.5
