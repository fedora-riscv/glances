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
Version:	3.2.7
Release:	1%{?dist}
Summary:	A cross-platform curses-based monitoring tool

License:	GPLv3
URL:		https://nicolargo.github.io/glances/
Source0:	https://github.com/nicolargo/glances/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.service

Patch1:		disable-update-check.patch

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-dateutil
BuildRequires:	pyproject-rpm-macros
BuildRequires:	systemd-units
Requires:	python3-bottle

%description
%{desc}

%prep
%autosetup -p1 -n %{name}-%{version}

# update disabled, no need for packaging dep
sed -i "s/, 'packaging'//" setup.py
sed -i '/packaging/d' requirements.txt

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
%config(noreplace) %{_sysconfdir}/glances/glances.conf
%exclude %{_datadir}/doc/glances
%{_bindir}/glances
%{_datadir}/man/man1/glances.1*
%{_unitdir}/%{name}.service

%changelog
* Tue Aug 02 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.2.7-1
- Update to 3.2.7 (RHBZ #2088525)

* Tue Jul 12 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.2.6.4-1
- Update to 3.2.6.4 (RHBZ #1870254 and #2088525)

* Wed Jun 22 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.2.5-1
- Update to 3.2.5 (rhbz #1963987 and #1988545)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.4.1-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  1 2020 Edouard Bourguignon <madko@linuxed.net> - 3.1.4.1-7
- Add missing changelog
- Requires python-psutil 5.3 (or even more, for disk IO stats on recent kernels)

* Thu May 28 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.4.1-6
- Rebuilt for Python 3.9

* Wed May 27 2020 Edouard Bourguignon <madko@linuxed.net> - 3.1.4.1-5
- /etc/glances/glances.conf is config(noreplace)

* Wed May 27 2020 Edouard Bourguignon <madko@linuxed.net> - 3.1.4.1-4
- Upgrade to 3.1.4.1
- Adding glances.conf to prevent update checks rhbz#1773662

* Wed May 27 2020 Carl George <carl@george.computer> - 3.1.4.1-3
- Add patch0 to disable outdated warning rhbz#1773662

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.4.1-2
- Rebuilt for Python 3.9 

* Thu May 21 2020 Richard Shaw <hobbes1069@gmail.com> - 3.1.4.1-1
- Update to 3.1.4.1.
- Update BR on psutil based on actual requirement generated.
- Remove long obsolete Group tag in spec file. 

* Sat Mar 14 2020 Edouard Bourguignon <madko@linuxed.net> - 3.1.4-1
- Upgrade to 3.1.4

* Fri Aug 16 2019 Edouard Bourguignon <madko@linuxed.net> - 3.1.1-1
- Upgrade to 3.1.1

* Sun Jun  2 2019 Edouard Bourguignon <madko@linuxed.net> - 3.1.0-1
- Upgrade to 3.1.0

* Sun Jun  2 2019 Edouard Bourguignon <madko@linuxed.net> - 3.0.2-1
- Upgrade to 3.0.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.11.1-7
- Enable python dependency generator

* Thu Jan 10 2019 Miro Hrončok <mhroncok@redhat.com> - 2.11.1-6
- Remove python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.11.1-4
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.11.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

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
