Name:          piccata
Version:       2.0.1
Release:       8%{?dist}
Summary:       A simple Python based CoAP (RFC7252) toolkit
License:       MIT
URL:           https://github.com/NordicSemiconductor/piccata
Source0:       https://github.com/NordicSemiconductor/piccata/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

%description
Piccata is a simple CoAP (RFC7252) toolkit written in Python.

%package -n python3-piccata
Summary:        A simple Python based CoAP (RFC7252) toolkit

%description -n python3-piccata
Piccata is a simple CoAP (RFC7252) toolkit written in Python.

The toolkit provides basic building blocks for using CoAP in an application.
piccata handles messaging between endpoints (retransmission, deduplication)
and request/response matching.

Handling and matching resources, blockwise transfers, etc. is left to the
application but functions to faciliate this are provided.

Piccata uses a transport abstraction to faciliate using the toolkit for
communication over different link types. Transport for a UDP socket is provided.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files piccata transport

%files -n python3-piccata -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.1-7
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 18 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.1-1
- Initial Package
