%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %global python_sitelib %(%{__python}26 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:		glances		
Version:	2.5.1
Release:	1%{?dist}
Summary:	CLI curses based monitoring tool

Group:		Applications/System		
License:	GPLv3
URL:		https://github.com/nicolargo/glances
Source0:	https://github.com/nicolargo/glances/archive/v%{version}.tar.gz
BuildArch:	noarch
%if 0%{?rhel} && 0%{?rhel} <= 5
BuildRequires:	python26-distribute
Requires:	python26-distribute
Requires:	python26-psutil >= 0.4.1
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
%else
BuildRequires:	python-setuptools
Requires:	python-setuptools
Requires:	python-psutil >= 2.0.0
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


%clean
rm -rf %{buildroot} 


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.rst NEWS 
%{_bindir}/glances
%{python_sitelib}/*
%exclude %{_datadir}/doc/glances
%{_datadir}/man/man1/glances.1.gz

%changelog
* Sat Nov  7 2015 Edouard Bourguignon <madko@linuxed.net> - 2.5.1
- Update to 2.5.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 01 2015 Edouard Bourguignon <madko@linuxed.net> - 2.3-1
- Update to 2.3

* Sat Jan 03 2015 Edouard Bourguignon <madko@linuxed.net> - 2.2.1-2
- Upstream patch for non root build

* Fri Jan 02 2015 Edouard Bourguignon <madko@linuxed.net> - 2.2.1-1
- Update to 2.2.1
- Add glances.conf and glances-test.conf

* Mon Oct 20 2014 Edouard Bourguignon <madko@linuxed.net> - 2.1.2-2
- Remove old python-setuptools-devel, now using python-setuptools instead

* Mon Oct 20 2014 Edouard Bourguignon <madko@linuxed.net> - 2.1.2-1
- Update to 2.1.2

* Thu Aug 07 2014 Edouard Bourguignon <madko@linuxed.net> - 2.0-1
- Update to 2.0.0

* Thu Jun 12 2014 Edouard Bourguignon <madko@linuxed.net> - 1.7.7-1
- Update to 1.7.7

* Wed Mar 26 2014 Edouard Bourguignon <madko@linuxed.net> - 1.7.6-1
- Update to 1.7.6

* Sat Mar 15 2014 Edouard Bourguignon <madko@linuxed.net> - 1.7.5-1
- Update to 1.7.5

* Mon Jan 20 2014 Edouard Bourguignon <madko@linuxed.net> - 1.7.4-1
- Update to 1.7.4

* Mon Jan 13 2014 Edouard Bourguignon <madko@linuxed.net> - 1.7.3-1
- Update to 1.7.3

* Tue Nov 12 2013 Edouard Bourguignon <madko@linuxed.net> - 1.7.2-1
- Update to 1.7.2

* Fri Aug 23 2013 Edouard Bourguignon <madko@linuxed.net> - 1.7.1-1
- Update to 1.7.1

* Sun Aug 11 2013 Edouard Bourguignon <madko@linuxed.net> - 1.7-1
- Update to 1.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 18 2013 Michel Salim <salimma@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

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
