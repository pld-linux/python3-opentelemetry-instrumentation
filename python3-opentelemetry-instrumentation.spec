#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python
Summary(pl.UTF-8):	Narzędzia pomiarowe i automatyczne pomiary dla OpenTelemetry dla Pythona
Name:		python3-opentelemetry-instrumentation
%define	subver	b0
%define	rel	1
Version:	0.61
Release:	0.%{subver}.%{rel}
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/opentelemetry-instrumentation/
Source0:	https://files.pythonhosted.org/packages/source/o/opentelemetry-instrumentation/opentelemetry_instrumentation-%{version}%{subver}.tar.gz
# Source0-md5:	67f5c0264e6129ee71162999cd57dc2c
URL:		https://pypi.org/project/opentelemetry-instrumentation/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
%if %{with tests}
BuildRequires:	python3-opentelemetry-api >= 1.4
BuildRequires:	python3-opentelemetry-api < 2
BuildRequires:	python3-opentelemetry-semantic-conventions = 0.61
BuildRequires:	python3-packaging >= 18.0
BuildRequires:	python3-pytest
BuildRequires:	python3-wrapt >= 1.0.0
BuildRequires:	python3-wrapt < 2
BuildRequires:	python3-typing_extensions >= 4.5.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides commands that help automatically instrument a
program.

%description -l pl.UTF-8
Ten pakiet udostępnia polecenia pomagające przy automatycznym
opomiarowaniu programów.

%prep
%setup -q -n opentelemetry_instrumentation-%{version}%{subver}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/opentelemetry-bootstrap
%attr(755,root,root) %{_bindir}/opentelemetry-instrument
%{py3_sitescriptdir}/opentelemetry/instrumentation
%{py3_sitescriptdir}/opentelemetry_instrumentation-%{version}%{subver}.dist-info
