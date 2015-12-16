%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname pygtk
#rpmlint wants %mklibname

Summary:	Python bindings for the GTK+2 widget set
Name:		pygtk2.0
Version:	2.24.0
Release:	17
License:	LGPLv2+
Group:		Development/GNOME and GTK+
Url:		http://www.pygtk.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pygtk/%{url_ver}/%{oname}-%{version}.tar.bz2
Patch0:		pygtk2.0-2.24.0-pango-leaks.patch
BuildRequires:	gnome-common
BuildRequires:	xsltproc
BuildRequires:	python-numpy-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pycairo)
Requires:	python2-numpy
Requires:	python2-gobject
Requires:	python2-cairo
Provides:	pygtk2 = %{EVRD}

%description
PyGTK is an extension module for python that gives you access to the GTK+
widget set. Just about anything you can write in C with GTK+ you can write
in python with PyGTK (within reason), but with all of python's benefits.

This new release includes GTK2 support.

%files
%doc AUTHORS NEWS README MAPPING ChangeLog 
%dir %{py2_platsitedir}/gtk-2.0/gtk/
%{py2_platsitedir}/gtk-2.0/gtk/*.py*
%{py2_platsitedir}/gtk-2.0/gtk/_*.so
%{py2_platsitedir}/gtk-2.0/gtkunixprint*
%{py2_platsitedir}/gtk-2.0/atk*.so
%{py2_platsitedir}/gtk-2.0/pango*.so

#----------------------------------------------------------------------------

%package devel
Summary:	Files needed to build wrappers for GTK+ addon libraries
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{EVRD}

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with pygtk.

This new release includes GTK2 support.

%files devel
%{_bindir}/pygtk-codegen-2.0
%{_includedir}/pygtk-2.0/*
%dir %{_datadir}/pygtk
%dir %{_datadir}/pygtk/2.0
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_datadir}/pygtk/2.0/defs/pangocairo.override
%{_libdir}/pkgconfig/pygtk-2.0.pc
%{_datadir}/gtk-doc/html/pygtk/

#----------------------------------------------------------------------------

%package libglade
Summary:	A wrapper for the libglade library for use with PyGTK
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{EVRD}

%description libglade
This module contains a wrapper for the libglade library.  Libglade is a
library similar to the pyglade module, except that it is written in C (so
is faster) and is more complete.

%files libglade
%{py2_platsitedir}/gtk-2.0/gtk/glade.so

#----------------------------------------------------------------------------

%package demos
Summary:	Examples and demos for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name}-devel = %{EVRD}

%description demos
This package contains example programs and demos for %{name}.

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

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
%patch0 -p1

%build
export PYTHON=%{__python2}
%configure2_5x  \
	--enable-thread \
	--enable-numpy

%make LIBS="`python2-config --libs`"

%install
%makeinstall_std

#(tpg) remove svn form docs
rm -rf `find -name .svn` %{buildroot}%{_docdir}

