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

BuildRequires:  gnome-common
BuildRequires:  xsltproc
#BuildRequires:  x11-server-xvfb
BuildRequires:  python-numpy-devel
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(pygobject-2.0)
BuildRequires:  pkgconfig(pycairo)

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
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

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

