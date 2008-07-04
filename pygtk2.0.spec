%define version 2.12.1
%define oname pygtk
#rpmlint wants %mklibname
Summary:	Python bindings for the GTK+2 widget set
Name:		pygtk2.0
Version:	%{version}
Release:	%mkrel 3
License:	LGPLv2+
Group:		Development/GNOME and GTK+
URL:		http://www.pygtk.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%oname/%{version}/%oname-%{version}.tar.bz2
BuildRequires:  gtk+2-devel >= 2.9.3
BuildRequires:	libglade2.0-devel 
BuildRequires:  python-devel >= %{pyver} python-numeric-devel
BuildRequires:  python-gobject-devel >= 2.12.1
%if %mdkversion >= 200810
BuildRequires:  python-cairo-devel >= 1.4.0
%else
BuildRequires:  python-cairo >= 1.0.0
%endif
%if %mdkversion <= 200600
BuildRequires:	XFree86-Xvfb
%else
BuildRequires:  x11-server-xvfb
%endif
BuildRequires:  gnome-common
#BuildRequires:  gtk-doc
BuildRequires:  libxslt-proc
Requires: 	python-numeric
Requires:	python-gobject
Requires:	python-cairo
Conflicts:	pygtk < 0.6.11
Provides:	%{name}-wrapper
Provides:	pygtk2 = %{version}-%{release}
Obsoletes:	%{name}-wrapper
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PyGTK is an extension module for python that gives you access to the GTK+
widget set.  Just about anything you can write in C with GTK+ you can write
in python with PyGTK (within reason), but with all of python's benefits.

This new release includes GTK2 support.

%package devel
Version:	%{version}
Summary:	Files needed to build wrappers for GTK+ addon libraries
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-devel
Requires:	python-devel >= %{pyver}
Requires: python-cairo-devel
Requires:  python-gobject-devel

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with pygtk.

This new release includes GTK2 support.

%package libglade
Version:	%{version}
Summary:	A wrapper for the libglade library for use with PyGTK
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}

%description libglade
This module contains a wrapper for the libglade library.  Libglade is a
library similar to the pyglade module, except that it is written in C (so
is faster) and is more complete.

%package demos
Version:	%{version}
Summary:	Examples and demos for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name}-devel = %{version}-%{release}

%description demos
This package contains example programs and demos for %{name}.

%prep
%setup -q -n pygtk-%{version}

%build
%configure2_5x  --enable-thread --enable-numpy
%make

%check
XDISPLAY=$(i=1; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
%if %mdkversion <= 200600
%{_prefix}/X11R6/bin/Xvfb :$XDISPLAY &
%else
%{_bindir}/Xvfb :$XDISPLAY &
%endif
export DISPLAY=:$XDISPLAY
#gw checks fail currently, as Xvfb is broken
make check
kill $(cat /tmp/.X$XDISPLAY-lock) || :

%install
rm -rf %{buildroot}
%makeinstall_std

#(tpg) remove svn form docs
rm -rf `find -name .svn` %{buildroot}%{_docdir}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README MAPPING ChangeLog 
%dir %{py_platsitedir}/gtk-2.0/gtk/
%{py_platsitedir}/gtk-2.0/gtk/*.py*
%{py_platsitedir}/gtk-2.0/gtk/_*.so
%{py_platsitedir}/gtk-2.0/gtkunixprint*
%{py_platsitedir}/gtk-2.0/atk*.so
%{py_platsitedir}/gtk-2.0/pango*.so

%files libglade
%defattr(-,root,root)
%{py_platsitedir}/gtk-2.0/gtk/glade.so
%{py_platsitedir}/gtk-2.0/gtk/glade.la

%files devel
%defattr(-,root,root)
%{_bindir}/pygtk-codegen-2.0
%{_includedir}/pygtk-2.0/*
%{py_platsitedir}/gtk-2.0/gtk/_*.la
%{py_platsitedir}/gtk-2.0/atk*.la
%{py_platsitedir}/gtk-2.0/pango*.la
%dir %{_datadir}/pygtk
%dir %{_datadir}/pygtk/2.0
%dir %{_datadir}/pygtk/2.0/codegen
%attr(755,root,root) %{_datadir}/pygtk/2.0/codegen/*.py
%{_datadir}/pygtk/2.0/codegen/*.py[co]
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_datadir}/pygtk/2.0/defs/pangocairo.override
%{_libdir}/pkgconfig/pygtk-2.0.pc
%{_datadir}/gtk-doc/html/pygtk/

%files demos
%defattr(644,root,root,755)
%doc examples/{atk,glade,gobject,gtk,ide,pango,simple}
%dir %{_libdir}/pygtk/2.0/demos
%dir %{_libdir}/pygtk/2.0/demos/images
%attr(755,root,root) %{_bindir}/pygtk-demo
%attr(755,root,root) %{_libdir}/pygtk/2.0/pygtk-demo.py
%{_libdir}/pygtk/2.0/pygtk-demo.py[co]
%attr(755,root,root) %{_libdir}/pygtk/2.0/demos/*.py
%{_libdir}/pygtk/2.0/demos/*.py[co]
%{_libdir}/pygtk/2.0/demos/images/*

%clean
rm -rf %{buildroot}
