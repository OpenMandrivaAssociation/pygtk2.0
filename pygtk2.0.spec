%define version 2.10.4
%define oname pygtk
#rpmlint wants %mklibname
Summary:	The sources for the PyGTK2 Python extension modules
Name:		pygtk2.0
Version:	%{version}
Release: %mkrel 2
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%oname/%oname-%{version}.tar.bz2
#gw from svn: adapt to GtkTooltips API change
Patch: pygtk-2831-fix-build-with-new-gtk.patch
License:	LGPL
Group:		Development/GNOME and GTK+
BuildRequires:  gtk+2-devel >= 2.9.3
BuildRequires:	libglade2.0-devel 
BuildRequires:  python-devel >= %{pyver} python-numeric-devel
BuildRequires:  python-gobject-devel >= 2.12.1
BuildRequires:  python-cairo >= 1.0.0
%if %mdkversion <= 200600
BuildRequires:	XFree86-Xvfb
%else
BuildRequires:  x11-server-xvfb
%endif
BuildRequires:  gnome-common
#BuildRequires:  gtk-doc
BuildRequires:  libxslt-proc
BuildRoot:	%_tmppath/%name-%version-root
URL:		http://www.daa.com.au/~james/software/pygtk/

Summary:	Python bindings for the GTK+2 widget set
Group:		Development/GNOME and GTK+
Requires: 	python-numeric
Requires:  python-gobject
Requires:  python-cairo
Conflicts:	pygtk < 0.6.11
Provides: %name-wrapper
Obsoletes: %name-wrapper

%description
PyGTK is an extension module for python that gives you access to the GTK+
widget set.  Just about anything you can write in C with GTK+ you can write
in python with PyGTK (within reason), but with all of python's benefits.

This new release includes GTK2 support.


%package devel
Version: %{version}
Summary: Files needed to build wrappers for GTK+ addon libraries
Group: Development/GNOME and GTK+
Requires: %name = %{version}
Requires: gtk2-devel
Requires: python-devel >= %{pyver}

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with pygtk.

This new release includes GTK2 support.

%package libglade
Version:	%{version}
Summary:	A wrapper for the libglade library for use with PyGTK
Group:		Development/GNOME and GTK+
Requires: 	%name = %version

%description libglade
This module contains a wrapper for the libglade library.  Libglade is a
library similar to the pyglade module, except that it is written in C (so
is faster) and is more complete.

%prep
%setup -q -n pygtk-%{version}
%patch -p1

%build
%configure2_5x  --enable-thread
%make

%check
XDISPLAY=$(i=1; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
%if %mdkversion <= 200600
%{_prefix}/X11R6/bin/Xvfb :$XDISPLAY &
%else
%{_bindir}/Xvfb :$XDISPLAY &
%endif
export DISPLAY=:$XDISPLAY
#gw checks fail currently
#make check
kill $(cat /tmp/.X$XDISPLAY-lock) || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%dir %{_libdir}/python%{pyver}/site-packages/gtk-2.0/gtk/
%{_libdir}/python%{pyver}/site-packages/gtk-2.0/gtk/*.py*
%{_libdir}/python%{pyver}/site-packages/gtk-2.0/gtk/_*.so
%{_libdir}/python%{pyver}/site-packages/gtk-2.0/gtk/_*.la
%{_libdir}/python%{pyver}/site-packages/gtk-2.0/gtkunixprint*
%{_libdir}/python%{pyver}/site-packages/gtk-2.0/atk*
%{_libdir}/python%{pyver}/site-packages/gtk-2.0/pango*

%doc AUTHORS NEWS README MAPPING ChangeLog 

%files libglade
%defattr(-,root,root)
%{_libdir}/python%{pyver}/site-packages/gtk-2.0/gtk/glade.so
%{_libdir}/python%{pyver}/site-packages/gtk-2.0/gtk/glade.la

%files devel
%defattr(-,root,root)
%doc docs examples
%{_bindir}/pygtk-codegen-2.0
%{_bindir}/pygtk-demo
%{_includedir}/pygtk-2.0/*
%dir %{_datadir}/pygtk
%dir %{_datadir}/pygtk/2.0
%{_datadir}/pygtk/2.0/codegen
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_datadir}/pygtk/2.0/defs/pangocairo.override
%{_libdir}/pygtk/2.0/pygtk-demo*
%{_libdir}/pygtk/2.0/demos
%{_libdir}/pkgconfig/pygtk-2.0.pc
%_datadir/gtk-doc/html/pygtk/

%clean
rm -rf $RPM_BUILD_ROOT


