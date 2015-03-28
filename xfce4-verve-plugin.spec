%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A minicmd-plugin for the Xfce panel
Name:		xfce4-verve-plugin
Version:	1.0.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-verve-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-verve-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(exo-1)
BuildRequires:	pkgconfig(libxfcegui4-1.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	perl(XML::Parser)

%description
This plugin is like the (quite old) xfce4-minicmd-plugin, except that it
feature more cool features, like autocompletion and command history.

%prep
%setup -q

%build
%configure \
	--enable-final \
	--enable-dbus

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README THANKS
%{_bindir}/verve-focus
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libexecdir}/xfce4/panel-plugins/*

