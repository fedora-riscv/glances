%global desc %{expand: \
Glances is a cross-platform monitoring tool which aims to present a large
amount of monitoring information through a curses or Web based interface.
The information dynamically adapts depending on the size of the user interface

It can also work in client/server mode. Remote monitoring could be done via
terminal, Web interface or API (XML-RPC and RESTful). Stats can also be
exported to files or external time/value databases.

Glances is written in Python and uses libraries to grab information from your
system. It is based on an open architecture where developers can add new 
plugins or exports modules.}

Name:		glances	
Version:	3.2.5
Release:	%autorelease
Summary:	A cross-platform curses-based monitoring tool

License:	GPLv3
URL:		https://nicolargo.github.io/glances/
Source0:	https://github.com/nicolargo/glances/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.service

Patch1:		disable-update-check.patch
Patch2:		unitest-python3.patch

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-dateutil
BuildRequires:	pyproject-rpm-macros
BuildRequires:	systemd-units
Requires:	python3-bottle

%py_provides python3-glances

%description
%{desc}

%prep
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files glances

mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 644 conf/glances.conf $RPM_BUILD_ROOT/etc/glances/glances.conf

%check
%tox

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files -n glances -f %{pyproject_files}
%doc AUTHORS COPYING README.rst
%license COPYING
%config(noreplace) %{_sysconfdir}/glances/glances.conf
%exclude %{_datadir}/doc/glances
%{_bindir}/glances
%{_datadir}/man/man1/glances.1*
%{_unitdir}/%{name}.service

%changelog
%autochangelog
