Summary:	Geoinformation service
Name:		geoclue2
Version:	2.1.10
Release:	2
Source0:	http://www.freedesktop.org/software/geoclue/releases/2.1/geoclue-%{version}.tar.xz
# Source0-md5:	aaa6c7a2a48a8fa74838345722d80e9f
Patch0:		%{name}-more-apps.patch
License:	GPL v2
URL:		http://geoclue.freedesktop.org/
Group:		Applications
BuildRequires:	ModemManager-devel
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib-gio-gsettings
BuildRequires:	json-glib
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
Requires(post,preun,postun):	systemd-units
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post geoclue.service

%preun
%systemd_preun geoclue.service

%postun
%systemd_postun

%files
%defattr(644,root,root,755)
%doc README NEWS
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/geoclue
%dir %{_sysconfdir}/geoclue
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/geoclue/geoclue.conf
%{systemdunitdir}/geoclue.service
/etc/dbus-1/system.d/org.freedesktop.GeoClue2.conf
/etc/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.GeoClue2.service
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.GeoClue2.conf
%{_datadir}/dbus-1/system-services

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/geoclue-2.0.pc
%{_datadir}/dbus-1/interfaces/org.freedesktop.GeoClue2.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.GeoClue2.Agent.xml

