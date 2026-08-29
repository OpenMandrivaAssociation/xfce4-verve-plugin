%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	A minicmd-plugin for the Xfce panel
Name:		xfce4-verve-plugin
Version:	2.1.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-verve-plugin
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-verve-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel
Requires:	exo
BuildRequires:	meson
BuildRequires:	make
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	xfce4-dev-tools
BuildRequires:	pkgconfig(gthread-2.0)


%description
This plugin is like the (quite old) xfce4-minicmd-plugin, except that it
feature more cool features, like autocompletion and command history.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README* THANKS
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_libdir}/xfce4/panel/plugins/*.so
