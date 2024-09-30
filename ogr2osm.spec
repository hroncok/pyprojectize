Name:           ogr2osm
Version:        1.2.0
Release:        5%{?dist}
Summary:        Convert ogr-readable files like shapefiles into .pbf or .osm data

License:        MIT
URL:            https://github.com/roelderickx/ogr2osm
Source0:        https://github.com/roelderickx/ogr2osm/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3-gdal
Requires:       python3-lxml
Requires:       python3-protobuf

%description
ogr2osm will read any data source that ogr can read and handle reprojection
for you. It takes a python file to translate external data source tags into
OSM tags, allowing you to use complicated logic. If no translation is
specified it will use an identity translation, carrying all tags from the
source to the .pbf or .osm output.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{name}


%files -f %{pyproject_files}
%{_bindir}/%{name}
%doc README.md


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 16 2023 Andrea Musuruane <musuruan@gmail.com> - 1.2.0-1
- Updated to new upstream release

* Sat Aug 26 2023 Andrea Musuruane <musuruan@gmail.com> - 1.1.2-5
- Fix returning None from filter_layer in translations

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.2-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 06 2022 Andrea Musuruane <musuruan@gmail.com> - 1.1.2-1
- Updated to new upstream release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Andrea Musuruane <musuruan@gmail.com> - 1.1.1-1
- Updated to new upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 04 2021 Andrea Musuruane <musuruan@gmail.com> - 1.1.0-1
- new version

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.10

* Mon May 24 2021 Andrea Musuruane <musuruan@gmail.com> - 1.0.1-1
- Updated to new upstream release

* Sun May 09 2021 Andrea Musuruane <musuruan@gmail.com> - 1.0.0-1
- New upstream
- Updated to new upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.11.20200130gitf82e052
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.10.20200130gitf82e052
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Andrea Musuruane <musuruan@gmail.com> - 0.1-0.9.20200130gitf82e052
- BR python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.8.20200130gitf82e052
- Rebuilt for Python 3.9

* Wed Feb 05 2020 Andrea Musuruane <musuruan@gmail.com> - 0.1-0.7.20200130gitf82e052
- Updated to new upstream snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.6.20191023git1b9cc00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Andrea Musuruane <musuruan@gmail.com> - 0.1-0.5.20191023git1b9cc00
- Updated to new upstream snapshot

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.4.20190104git183e226
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.3.20190104git183e226
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.2.20190104git183e226
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr  6 2019 Andrea Musuruane <musuruan@gmail.com> - 0.1-0.1.20190104git183e226
- First release

