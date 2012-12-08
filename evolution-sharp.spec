Summary:	Evolution C# bindings for mono
Name:		evolution-sharp
Version:	0.21.1
Release:	12
License:	GPL
Group:		Development/Other
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
# (fc) fix eds detection (Fedora)
Patch0:		evolution-sharp-0.21.1-fix-retarded-version-check.patch
# (fc) fix eds major for eds >= 2.30.2
Patch1:		evolution-sharp-0.21.1-fix-eds-major.patch
Patch2:		evolution-sharp-0.21.1-glib.patch
BuildRequires:	pkgconfig(libecal-1.2)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gnome-common
Requires:	evolution

%description
Evolution# is a .NET language binding for various Ximian Evolution (tm)
libraries.

%package devel
Summary:	Evolution C# bindings for mono
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
Evolution# is a .NET language binding for various Ximian Evolution (tm)
libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .fixmajor
%patch2 -p1

#needed by patches 0, 1
NOCONFIGURE=yes gnome-autogen.sh
%build
%configure2_5x
make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/lib*a

%files
%doc README MAINTAINERS AUTHORS
%{_prefix}/lib/mono/evolution-sharp/
%{_prefix}/lib/mono/gac/evolution-sharp/
%{_libdir}/libevolutionglue.so

%files devel
%doc ChangeLog
%{_libdir}/pkgconfig/evolution-sharp.pc
%{_datadir}/gapi-2.0/evolution-api.xml


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.21.1-8mdv2011.0
+ Revision: 664155
- mass rebuild

* Mon Oct 11 2010 Funda Wang <fwang@mandriva.org> 0.21.1-7mdv2011.0
+ Revision: 584900
- rebuild

* Mon Aug 09 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.21.1-6mdv2011.0
+ Revision: 567876
- update patch for new e-d-s
- split out devel package
- disable parallel build

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 0.21.1-5mdv2010.1
+ Revision: 549351
- Fix patch0 with Fedora version
- Patch1: fix edataserver major

* Tue Jan 12 2010 Funda Wang <fwang@mandriva.org> 0.21.1-4mdv2010.1
+ Revision: 490033
- rebuild

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - rebuild for new libedata-cal

* Mon Dec 28 2009 Funda Wang <fwang@mandriva.org> 0.21.1-2mdv2010.1
+ Revision: 482921
- add patch to build against newer evo

* Tue May 26 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.21.1-1mdv2010.0
+ Revision: 379838
- update to new version 0.21.1

* Tue Mar 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.20.0-1mdv2009.1
+ Revision: 360816
- new version

* Tue Feb 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.19.2.1-1mdv2009.1
+ Revision: 342225
- update to new version 0.19.2.1

* Sun Feb 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.19.2-1mdv2009.1
+ Revision: 340633
- update to new version 0.19.2

* Mon Jan 19 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.19.1-1mdv2009.1
+ Revision: 331128
- update to new version 0.19.1

* Wed Sep 24 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.18.0-1mdv2009.0
+ Revision: 287715
- new version

* Tue Sep 16 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.17.6-1mdv2009.0
+ Revision: 285129
- new version

* Tue Sep 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.17.5-1mdv2009.0
+ Revision: 282915
- new version

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.17.4-1mdv2009.0
+ Revision: 231415
- new version
- update deps

* Sun May 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.16.1.1-1mdv2009.0
+ Revision: 201159
- new version
- drop patch

* Tue Apr 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.16.1-2mdv2009.0
+ Revision: 198992
- fix a crash in beagle

* Tue Apr 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.16.1-1mdv2009.0
+ Revision: 193698
- new version
- drop patch

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.16.0-1mdv2008.1
+ Revision: 183424
- new version

* Tue Feb 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.92-1mdv2008.1
+ Revision: 175388
- fix build on 64 bit
- new version

* Tue Feb 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.91-1mdv2008.1
+ Revision: 165913
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.4-1mdv2008.1
+ Revision: 133605
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.1-1mdv2008.1
+ Revision: 104339
- new version

* Tue Sep 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.0.1-1mdv2008.0
+ Revision: 89817
- new version
- new version

* Thu Aug 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.13.3-1mdv2008.0
+ Revision: 70743
- new version

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.13.2-1mdv2008.0
+ Revision: 57441
- fix buildrequries
- new version

* Thu Jul 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.13.1-1mdv2008.0
+ Revision: 53645
- fix buildrequires
- new version

* Wed Jun 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.13-1mdv2008.0
+ Revision: 41785
- new version

* Tue May 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.4-1mdv2008.0
+ Revision: 26839
- new version

* Tue Apr 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.3-1mdv2008.0
+ Revision: 17739
- new version


* Tue Jan 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.2-1mdv2007.0
+ Revision: 112590
- new version

* Thu Jan 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.1-1mdv2007.1
+ Revision: 104001
- new version
- drop patch
- fix installation

* Wed Nov 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.0-3mdv2007.1
+ Revision: 88531
- bot rebuild
- support evolution 2.9

* Tue Nov 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.0-1mdv2007.1
+ Revision: 85958
- new version
- drop patch

* Thu Nov 02 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.1-4mdv2007.1
+ Revision: 75503
- Import evolution-sharp

* Thu Nov 02 2006 Götz Waschk <waschk@mandriva.org> 0.11.1-4mdv2007.1
- fix patch to have the correct libecal major

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.1-1mdv2007.0
- rebuild for new e-d-s

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 0.11.1-2mdv2007.0
- update patch for new e-d-s

* Wed Jun 07 2006 Frederic Crozat <fcrozat@mandriva.com> 0.11.1-1mdv2007.0
- Release 0.11.1

* Wed May 31 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-6mdv2007.0
- update patch 0 for new e-d-s

* Sat Apr 22 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.10.2-5mdk
- add BuildRequires: libgtkhtml-3.8-devel

* Sat Apr 22 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-4mdk
- fix buildrequires

* Fri Apr 21 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-3mdk
- fix deps
- fix dllmap
- patch for e-d-s 1.5.1

* Mon Jan 16 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-2mdk
- fix buildrequires

* Sat Oct 08 2005 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdk
- New release 0.10.2
- update file list
- bump deps
- patch for e-d-s 1.3.7

* Sat Aug 13 2005 Götz Waschk <waschk@mandriva.org> 0.8-1mdk
- update file list
- fix deps
- drop patch
- New release 0.8

* Tue May 03 2005 Götz Waschk <waschk@mandriva.org> 0.6-3mdk
- fix paths for x86_64

* Fri Apr 22 2005 Götz Waschk <waschk@mandriva.org> 0.6-2mdk
- patch for new e-d-s

* Fri Feb 11 2005 Götz Waschk <waschk@linux-mandrake.com> 0.6-1mdk
- 0.6

* Fri Jan 21 2005 Götz Waschk <waschk@linux-mandrake.com> 0.6-0.20040121.1mdk
- update to snapshot
- New release 0.6

* Tue Sep 21 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.4-1mdk
- New release 0.4

* Fri Sep 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3-2mdk
- fix deps

* Fri Sep 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3-1mdk
- initial package

