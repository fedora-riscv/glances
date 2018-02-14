%global sum	CLI curses based monitoring tool

Name:		glances	
Version:	2.11.1
Release:	2%{?dist}
Summary:	%{sum}

Group:		Applications/System		
License:	GPLv3
URL:		https://github.com/nicolargo/glances
Source0:	https://github.com/nicolargo/glances/archive/v%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  python2-devel python3-devel
BuildRequires:	python-setuptools python3-setuptools
BuildRequires:	python2-psutil >= 2.0.0
BuildRequires:	python3-psutil >= 2.0.0

%{?python_provide:%python_provide python3-%{name}}
Requires:	python3-setuptools
Requires:	python3-psutil >= 2.0.0

%description
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

It is developed in Python.


%package -n python2-%{name}
%{?python_provide:%python_provide python2-%{name}}
Requires:	python-setuptools
Requires:	python2-psutil >= 2.0.0
Summary:        %{sum}
Provides:	%{name} = %{version}-%{release}
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

It is developed in Python.


%prep
%autosetup -n %{name}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test


%files -n python2-%{name}
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.rst NEWS 
%license COPYING
%{python2_sitelib}/%{name}/
%{python2_sitelib}/Glances-%{version}-py%{python2_version}.egg-info/
%exclude %{_datadir}/doc/glances
%{_datadir}/man/man1/glances.1.gz

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.rst NEWS
%license COPYING
%{_bindir}/glances
%{python3_sitelib}/%{name}/
%{python3_sitelib}/Glances-%{version}-py%{python3_version}.egg-info/
%exclude %{_datadir}/doc/glances
%{_datadir}/man/man1/glances.1.gz


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 26 2017 Edouard Bourguignon <madko@linuxed.net> - 2.11.1-1
- Upgrade to 2.11.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Edouard Bourguignon <madko@linuxed.net> - 2.7.1-1
- Upgrade to 2.7.1

* Sun Oct 16 2016 Edouard Bourguignon <madko@linuxed.net> - 2.6.1-3
- Fix for python2 and python3 packages

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 28 2016 Edouard Bourguignon <madko@linuxed.net> - 2.6.1
- Update to 2.6.1
- Provides python2 and python3 packages

* Sat Oct 10 2015 Edouard Bourguignon <madko@linuxed.net> - 2.5.1
- Update to 2.5.1

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
