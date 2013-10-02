Summary:	Geoinformation service
Name:		geoclue2
Version:	2.0.0
Release:	1
Source0:	http://www.freedesktop.org/software/geoclue/releases/2.0/geoclue-%{version}.tar.xz
# Source0-md5:	401ff99d530b177c62afacef0a33efd9
License:	GPL v2
Group:		Applications
URL:		http://geoclue.freedesktop.org/
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib-gio-gsettings
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
Requires(post,postun):	glib-gio-gsettings
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/geoclue2

%description
GeoClue is a D-Bus geoinformation service. The goal of the Geoclue
project is to make creating location-aware applications as simple as
possible.

%package devel
Summary:	Development package for geoclue
Group:		Development/Libraries
# don't require base

%description devel
Header files for development with geoclue.

%prep
%setup -qn geoclue-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/geoclue
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.GeoClue2.conf
%{_datadir}/dbus-1/system-services

%files devel
%defattr(644,root,root,755)
%dir %{_datadir}/geoclue-2.0
%{_datadir}/geoclue-2.0/geoclue-interface.xml
%{_pkgconfigdir}/geoclue-2.0.pc

