Name:		glances		
Version:	1.3.4
Release:	1%{?dist}
Summary:	CLI curses based monitoring tool

Group:		Applications/System		
License:	GPLv3
URL:		https://github.com/nicolargo/glances
Source0:	https://github.com/downloads/nicolargo/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	automake	
BuildRequires:	python-devel
Requires:	pystatgrab >= 0.5

%description
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the libstatgrab library to get information from your system.
Glances is developed in Python and uses the python-statgrab lib.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot} 
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/doc/glances
sed -i '1d' %{buildroot}/%{python_sitelib}/%{name}/%{name}.py
mv %{buildroot}/%{_bindir}/glances.py %{buildroot}/%{_bindir}/glances

%clean
rm -rf %{buildroot} 


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_bindir}/glances
%{python_sitelib}/glances
%{_datadir}/man/man1/glances.1.gz

%changelog
* Fri Dec 30 2011 Edouard Bourguignon <madko@linuxed.net> - 1.3.4-1
- Upgrade to version 1.3.4

* Fri Dec 23 2011 Edouard Bourguignon <madko@linuxed.net> - 1.3.3-1
- Upgrade to version 1.3.3

* Wed Dec 21 2011 Edouard Bourguignon <madko@linuxed.net> - 1.3.2-1
- Upgrade to version 1.3.2

* Sat Dec 17 2011 Edouard Bourguignon <madko@linuxed.net> - 1.3.1-1
- Upgrade to version 1.3.1 (fix fs display)

* Wed Dec 14 2011 Edouard Bourguignon <madko@linuxed.net> - 1.3-1
- Upgrade to version 1.3

* Tue Dec 13 2011 Edouard Bourguignon <madko@linuxed.net> - 1.2-1
- Upgrade to version 1.2

* Tue Dec  6 2011 Edouard Bourguignon <madko@linuxed.net> - 1.1.3-1
- Upgrade to version 1.1.3

* Tue Dec  6 2011 Edouard Bourguignon <madko@linuxed.net> - 1.1.2-2
- Fix for review
- Remove shebang from non-executable script
- Add version for libpystatgrab
- Renamed glances.py to glances

* Mon Dec  5 2011 Edouard Bourguignon <madko@linuxed.net> - 1.1.2-1
- Upgrade to 1.1.2

* Mon Dec  5 2011 Edouard Bourguignon <madko@linuxed.net> - 1.1.1-1
- Upgrade to 1.1.1

* Mon Dec  5 2011 Edouard Bourguignon <madko@linuxed.net> - 1.0-1 
- Initial version
