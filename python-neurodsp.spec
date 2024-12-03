%bcond_without tests

%global pypi_name neurodsp

%global _description %{expand:
NeuroDSP is package of tools to analyze and simulate neural 
time series, using digital signal processing.

Available modules in NeuroDSP include:

* filt : Filter data with bandpass, highpass, lowpass, or
notch filters
* burst : Detect bursting oscillations in neural signals
* rhythm : Find and analyze rhythmic and recurrent patterns
in time series
* spectral : Compute spectral domain features such as power
spectra
* timefrequency : Estimate instantaneous measures of
oscillatory activity
* sim : Simulate time series, including periodic and
aperiodic signal components
* plts : Plotting functions

If you use this code in your project, please cite:

Cole, S., Donoghue, T., Gao, R., & Voytek, B. (2019).
NeuroDSP: A package for neural digital signal processing.
Journal of Open Source Software, 4(36), 1272.
https://doi.org/10.21105/joss.01272}

Name:           python-%{pypi_name}
Version:        2.2.1
Release:        %autorelease
Summary:        A tool for digital signal processing for neural time series

License:        Apache-2.0
URL:            https://neurodsp-tools.github.io/
Source0:        https://github.com/neurodsp-tools/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist matplotlib}

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%prep
# No keyring/signature from the upstream to verify the source
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# cannot build the docs, as it downloads additional datasets (through mne).

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%if %{with tests}
# Deselected tests that require internet
%pytest --deselect neurodsp/tests/utils/test_download.py
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst paper/*

%changelog
%autochangelog
