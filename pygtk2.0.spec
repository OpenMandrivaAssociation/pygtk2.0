%define oname pygtk
#rpmlint wants %mklibname
Summary:	Python bindings for the GTK+2 widget set
Name:		pygtk2.0
Version:	2.24.0
Release:	4
License:	LGPLv2+
Group:		Development/GNOME and GTK+
URL:		http://www.pygtk.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%oname/%oname-%{version}.tar.bz2

BuildRequires:	gnome-common
BuildRequires:	xsltproc
#BuildRequires:  x11-server-xvfb
BuildRequires:	python-numpy-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pycairo)

Requires:	python-numpy
Requires:	python-gobject
Requires:	python-cairo

Provides:	pygtk2 = %{version}-%{release}

%description
PyGTK is an extension module for python that gives you access to the GTK+
widget set.  Just about anything you can write in C with GTK+ you can write
in python with PyGTK (within reason), but with all of python's benefits.

This new release includes GTK2 support.

%package devel
Summary:	Files needed to build wrappers for GTK+ addon libraries
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with pygtk.

This new release includes GTK2 support.

%package libglade
Summary:	A wrapper for the libglade library for use with PyGTK
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}

%description libglade
This module contains a wrapper for the libglade library.  Libglade is a
library similar to the pyglade module, except that it is written in C (so
is faster) and is more complete.

%package demos
Summary:	Examples and demos for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name}-devel = %{version}-%{release}

%description demos
This package contains example programs and demos for %{name}.

%prep
%setup -q -n pygtk-%{version}
%apply_patches

%build
%configure2_5x  \
	--enable-thread \
	--enable-numpy

%make LIBS="`python-config --libs`"

#%#check
#%#_bindir/xvfb-run -a make check

%install
%makeinstall_std

#(tpg) remove svn form docs
rm -rf `find -name .svn` %{buildroot}%{_docdir}

%files
%doc AUTHORS NEWS README MAPPING ChangeLog 
%dir %{py_platsitedir}/gtk-2.0/gtk/
%{py_platsitedir}/gtk-2.0/gtk/*.py*
%{py_platsitedir}/gtk-2.0/gtk/_*.so
%{py_platsitedir}/gtk-2.0/gtkunixprint*
%{py_platsitedir}/gtk-2.0/atk*.so
%{py_platsitedir}/gtk-2.0/pango*.so

%files libglade
%{py_platsitedir}/gtk-2.0/gtk/glade.so

%files devel
%_bindir/pygtk-codegen-2.0
%{_includedir}/pygtk-2.0/*
%dir %{_datadir}/pygtk
%dir %{_datadir}/pygtk/2.0
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_datadir}/pygtk/2.0/defs/pangocairo.override
%{_libdir}/pkgconfig/pygtk-2.0.pc
%{_datadir}/gtk-doc/html/pygtk/

%files demos
%doc examples/{atk,glade,gobject,gtk,ide,pango,simple}
%dir %{_libdir}/pygtk/2.0/demos
%dir %{_libdir}/pygtk/2.0/demos/images
%attr(755,root,root) %{_bindir}/pygtk-demo
%attr(755,root,root) %{_libdir}/pygtk/2.0/pygtk-demo.py
%{_libdir}/pygtk/2.0/pygtk-demo.py[co]
%attr(755,root,root) %{_libdir}/pygtk/2.0/demos/*.py
%{_libdir}/pygtk/2.0/demos/*.py[co]
%{_libdir}/pygtk/2.0/demos/images/*

%changelog
* Fri Mar 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.24.0-4
+ Revision: 785405
- rebuild
- cleaned up spec

* Sun Nov 06 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.24.0-3
+ Revision: 722214
- Rebuild with newer libpng.

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - reenable checks

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 2.24.0-2
+ Revision: 652028
- link with libpython

* Mon Apr 04 2011 Funda Wang <fwang@mandriva.org> 2.24.0-1
+ Revision: 650192
- New version 2.24.0

* Wed Nov 17 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-3mdv2011.0
+ Revision: 598141
- rebuild

* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.22.0-2mdv2011.0
+ Revision: 590712
- rebuild for python-2.7

* Sun Sep 26 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2011.0
+ Revision: 581050
- update to new version 2.22.0

* Sun Aug 08 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.0-1mdv2011.0
+ Revision: 567596
- new version
- drop patch

* Tue Apr 27 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.17.0-4mdv2010.1
+ Revision: 539615
- rebuild so that shared libraries are properly stripped again

* Tue Apr 27 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.17.0-3mdv2010.1
+ Revision: 539594
- rebuild so that shared libraries are properly stripped again

* Mon Apr 19 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.0-2mdv2010.1
+ Revision: 536587
- add patch for too many wakeups (bug #50530)

* Sun Dec 27 2009 Funda Wang <fwang@mandriva.org> 2.17.0-1mdv2010.1
+ Revision: 482706
- new version 2.17.0

* Sun Aug 23 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2010.0
+ Revision: 420096
- new version
- drop patch

* Sun Jun 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.2-1mdv2010.0
+ Revision: 387571
- update to new version 2.15.2

* Mon May 25 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.1-1mdv2010.0
+ Revision: 379435
- update to new version 2.15.1

* Mon May 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.0-1mdv2010.0
+ Revision: 374195
- new version
- depend on python-numpy

* Fri Mar 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.1-1mdv2009.1
+ Revision: 349634
- update to new version 2.14.1

* Sun Feb 01 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-1mdv2009.1
+ Revision: 336055
- update to new version 2.14.0
- fix source URL

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 2.13.0-2mdv2009.1
+ Revision: 318549
- disable the tests as they break with Python 2.6
  (see http://bugzilla.gnome.org/show_bug.cgi?id=565593)

  + Michael Scherer <misc@mandriva.org>
    - rebuild for new python
    - fix format string error

* Sun Aug 24 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.13.0-1mdv2009.0
+ Revision: 275569
- new version
- update file list

* Wed Jul 16 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-5mdv2009.0
+ Revision: 236288
- readd pygtk-codegen-2.0

* Tue Jul 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-4mdv2009.0
+ Revision: 235863
- fix buildrequires
- use xvfb-run
- remove codegen tool (now in python-gobject-devel)

* Fri Jul 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.12.1-3mdv2009.0
+ Revision: 231726
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jan 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-1mdv2008.1
+ Revision: 144829
- new version
- drop the patch

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-3mdv2008.1
+ Revision: 102630
- fix devel deps

* Fri Oct 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.12.0-2mdv2008.1
+ Revision: 100484
- new license policy
- provide patch 0, fixes GNOME bug #479012
- do not package docs twice
- remove svn files from docs
- use macros wherever it is possible
- move *.la files to the devel package
- remove demos and examples from devel package, move them to new subpackage
- spec file clean

* Sun Sep 23 2007 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-2mdv2008.0
+ Revision: 92372
- Add provides for better compatibility with non Mdv packages

* Sun Sep 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-1mdv2008.0
+ Revision: 88450
- new version

* Mon Aug 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.0-1mdv2008.0
+ Revision: 72046
- new version

* Tue Jul 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.6-1mdv2008.0
+ Revision: 50972
- disable checks
- new version

* Wed Jul 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.5-1mdv2008.0
+ Revision: 48126
- new version
- drop patch
- reenable checks

* Wed Jul 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.4-2mdv2008.0
+ Revision: 47970
- disable checks
- fix buildrequires
- fix build


* Mon Feb 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.4-1mdv2007.0
+ Revision: 116502
- new version

* Fri Jan 26 2007 Olivier Blin <oblin@mandriva.com> 2.10.3-4mdv2007.1
+ Revision: 113999
- move huge docs and devel examples in devel package

* Fri Jan 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.3-3mdv2007.1
+ Revision: 110817
- fix buildrequires, reenabling Numeric Python support

* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.3-2mdv2007.1
+ Revision: 88121
- rebuild
- Import pygtk2.0

* Thu Oct 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.3-1mdv2007.0
- New version 2.10.3

* Wed Sep 06 2006 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdv2007.0
- bump deps
- New release 2.10.1

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.9.6-1mdv2007.0
- reenable parallel build
- bump deps
- New release 2.9.6

* Mon Aug 07 2006 Götz Waschk <waschk@mandriva.org> 2.9.5-1mdv2007.0
- drop patch
- New release 2.9.5

* Sun Aug 06 2006 Götz Waschk <waschk@mandriva.org> 2.9.4-1mdv2007.0
- update file list
- spec fixes
- bump deps
- add missing sources
- New release 2.9.4

* Thu Jul 13 2006 Götz Waschk <waschk@mandriva.org> 2.9.3-1mdv2007.0
- drop patch
- New release 2.9.3

* Wed Jun 28 2006 Götz Waschk <waschk@mandriva.org> 2.9.2-3mdv2007.0
- replace patch 0

* Fri Jun 23 2006 Frederic Crozat <fcrozat@mandriva.com> 2.9.2-2mdv2007.0
- Patch0 (CVS): fix for latest GTK+ 2.9.4 (Mdv bug #23259)

* Sat Jun 17 2006 Götz Waschk <waschk@mandriva.org> 2.9.2-1mdv2007.0
- bump deps
- update file list
- New release 2.9.2

* Thu Apr 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.6-1mdk
- New release 2.8.6

* Fri Mar 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.5-1mdk
- New release 2.8.5

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2.8.4-2mdk
- Fix buildrequires

* Wed Jan 11 2006 Götz Waschk <waschk@mandriva.org> 2.8.4-1mdk
- fix installation
- New release 2.8.4

* Wed Jan 11 2006 Götz Waschk <waschk@mandriva.org> 2.8.3-2mdk
- move modules to the right dir
- depend on python-cairo

* Tue Jan 10 2006 Götz Waschk <waschk@mandriva.org> 2.8.3-1mdk
- drop wrapper package
- bump deps
- New release 2.8.3
- use mkrel

* Tue Oct 11 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.2-1mdk
- New release 2.8.2

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.8.1-1mdk
- Release 2.8.1

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.8.0-1mdk
- Release 2.8.0

* Thu May 12 2005 Frederic Crozat <fcrozat@mandriva.com> 2.6.2-1mdk 
- Release 2.6.2

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.6.1-1mdk 
- Release 2.6.1 (based on Götz Waschk package)

* Tue Mar 29 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.1-4mdk 
- Patch0: fix module detection

* Mon Dec 20 2004 Götz Waschk <waschk@linux-mandrake.com> 2.4.1-3mdk
- depend on Xvfb to allow running the tests
- fix deps

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 2.4.1-2mdk
- Rebuild for new python

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 2.4.1-1mdk
- New release 2.4.1

* Mon Aug 09 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.3.96-1mdk
- New release 2.3.96

* Tue Aug 03 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.3.95-1mdk
- New release 2.3.95

* Fri Jul 23 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.3.94-1mdk
- New release 2.3.94

* Wed Jul 21 2004 Götz Waschk <waschk@linux-mandrake.com> 2.3.93-1mdk
- rpmlint fix
- reenable libtoolize
- New release 2.3.93

* Sun May 23 2004 Götz Waschk <waschk@linux-mandrake.com> 2.3.92-1mdk
- bot friendly spec
- New release 2.3.92

* Wed May 05 2004 Olivier Blin <blino@mandrake.org> 2.3.91-2mdk
- use real homepage as URL
- use complete URL of Source0
- require gtk2-devel in devel package

* Sat Apr 17 2004 Götz Waschk <waschk@linux-mandrake.com> 2.3.91-1mdk
- new version

* Tue Apr 06 2004 Götz Waschk <waschk@linux-mandrake.com> 2.3.90-1mdk
- drop the glarea package
- use the configure2_5x macro
- new version

