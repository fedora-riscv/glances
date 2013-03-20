%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %global python_sitelib %(%{__python}26 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:		glances		
Version:	1.6
Release:	2%{?dist}
Summary:	CLI curses based monitoring tool

Group:		Applications/System		
License:	GPLv3
URL:		https://github.com/nicolargo/glances
Source0:	https://github.com/downloads/nicolargo/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
%if 0%{?rhel} && 0%{?rhel} <= 5
BuildRequires:	python26-distribute
Requires:	python26-distribute
Requires:	python26-psutil >= 0.4.1
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
%else
BuildRequires:	python-setuptools-devel
Requires:	python-setuptools
Requires:	python-psutil >= 0.4.1
%endif

%description
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

It is developed in Python.

%prep
%setup -q

%build


%install
%if 0%{?rhel} && 0%{?rhel} <= 5
%{__python}26 setup.py install --root %{buildroot}
%else
%{__python} setup.py install --root %{buildroot}
%endif
%find_lang %{name}
mv %{buildroot}/usr/etc/ %{buildroot}


%clean
rm -rf %{buildroot} 


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO 
%{_bindir}/glances
%config(noreplace) %{_sysconfdir}/glances
%attr(0655,-,-) %{python_sitelib}/glances/glances.py
%attr(0655,-,-) %{python_sitelib}/glances/unitest.py
%{python_sitelib}/*
%{_datadir}/doc/glances
%{_datadir}/glances
%{_datadir}/man/man1/glances.1.gz

%changelog
* Tue Mar 19 2013 Michel Salim <salimma@fedoraproject.org> - 1.6-2
- On el5, build against python26 stack

* Sat Mar 16 2013 Edouard Bourguignon <madko@linuxed.net> - 1.6-1
- Upgrade to 1.6

* Sat Feb 23 2013 Edouard Bourguignon <madko@linuxed.net> - 1.5.2-3
- Patch to fix bug #914837 (noSuchProcess)

* Sat Jan 12 2013 Edouard Bourguignon <madko@linuxed.net> - 1.5.2-2
- Patch to initialize y in displayMem (bug #894347)

* Sun Dec 30 2012 Edouard Bourguignon <madko@linuxed.net> - 1.5.2-1
- Upgrade to 1.5.2

* Tue Nov 13 2012 Edouard Bourguignon <madko@linuxed.net> - 1.5.1-1
- Upgrade to 1.5.1 (fix compute data on el6)

* Thu Nov  8 2012 Edouard Bourguignon <madko@linuxed.net> - 1.5-1
- Upgrade to 1.5

* Sat Sep  1 2012 Edouard Bourguignon <madko@linuxed.net> - 1.4.1.1-1
- Upgrade to 1.4.1.1

* Tue Aug 21 2012 Edouard Bourguignon <madko@linuxed.net> - 1.4-2
- Adding missing dependencies
- Removing shebang in non-executable files

* Tue Aug 21 2012 Edouard Bourguignon <madko@linuxed.net> - 1.4-1
- Upgrade to version 1.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 13 2012 Edouard Bourguignon <madko@linuxed.net> - 1.3.7-2
- Add version for python

* Thu Feb  2 2012 Edouard Bourguignon <madko@linuxed.net> - 1.3.7-1
- Upgrade to version 1.3.7

* Fri Jan 20 2012 Edouard Bourguignon <madko@linuxed.net> - 1.3.6-1
- Upgrade to version 1.3.6 (fix crash when a network intf is removed)

* Tue Jan 17 2012 Edouard Bourguignon <madko@linuxed.net> - 1.3.5-1
- Upgrade to version 1.3.5

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
