%global srcname flask-wtf-decorators
%global commit 7fa5a26946d2fdb5b00d07251c0ca7d0e358fc1d
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:           python-%{srcname}
Version:        0.1.2
Release:        0.16.20200715.%{shortcommit}%{?dist}
Summary:        Use decorators to validate forms
BuildArch:      noarch

License:        MIT
URL:            https://github.com/simpleapples/flask-wtf-decorators
Source0:        https://github.com/simpleapples/flask-wtf-decorators/archive/%{commit}/%{name}-%{shortcommit}.tar.gz


%package -n python3-%{srcname}
Summary:       %{summary}
BuildRequires: python3-devel
BuildRequires: python3-flask-wtf


%global _description %{expand:
Flask-WTF-Decorators is easy to use. You can define a view that requires
validation.

    from flask-wtf-decorators import FormValidator

    form_validator = FormValidator()

    @form_validator.validate_form(TestForm)
    @app.route('/', methods=['GET', 'POST'])
    def index(form):
        pass

You can tell Flask-WTF-Decorators what to do when a form is illegal.
To do this you should provide a callback for error_handler.

    @form_validator.error_handler
    def error_handler(errors):
        return jsonify(\{'errors': errors\}), 400
}

%description %_description
%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{commit}


%generate_buildrequires
%pyproject_buildrequires


%check
%{python3} setup.py test


%build
%pyproject_wheel


%install
%pyproject_install


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/flask_wtf_decorators
%{python3_sitelib}/Flask_WTF_Decorators-*.dist-info/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.16.20200715.7fa5a26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.1.2-0.15.20200715.7fa5a26
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.14.20200715.7fa5a26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.13.20200715.7fa5a26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.12.20200715.7fa5a26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.1.2-0.11.20200715.7fa5a26
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.10.20200715.7fa5a26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.9.20200715.7fa5a26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.1.2-0.8.20200715.7fa5a26
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.7.20200715.7fa5a26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.6.20200715.7fa5a26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.2-0.5.20200715.7fa5a26
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.4.20200715.7fa5a26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.3.20200715.7fa5a26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jakub Kadlčík <jkadlcik@redhat.com> - 0.1.2-0.2.20200715.7fa5a26
- Use proper pre-release versioning

* Tue Jul 14 2020 Jakub Kadlcik <jkadlcik@redhat.com> - 0.1.2-20200704.7fa5a26
- Run tests in the check phase
- Rename this file to python-flask-wtf-decorators.spec

* Tue Jul 14 2020 Jakub Kadlcík <jkadlcik@redhat.com> - 0.1.2-20200703.7fa5a26
- Provide python3 subpackage

* Thu Jul 02 2020 Jakub Kadlcik <jkadlcik@redhat.com>
- Initial package
