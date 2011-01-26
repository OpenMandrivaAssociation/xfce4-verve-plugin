Summary:	A minicmd-plugin for the Xfce panel
Name:		xfce4-verve-plugin
Version:	1.0.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-verve-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-verve-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
BuildRequires:	exo-devel >= 0.6.0
BuildRequires:	libxfcegui4-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	pcre-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-verve-plugin < 0.3.6
Obsoletes:	verve-plugin < 0.3.6
Provides:	xfce-verve-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This plugin is like the (quite old) xfce4-minicmd-plugin, except that it
feature more cool features, like autocompletion and command history.

%prep
%setup -q

%build
%configure2_5x \
	--enable-final \
	--enable-dbus

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README THANKS
%{_bindir}/verve-focus
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libdir}/xfce4/panel-plugins/*
