%define oname verve-plugin

Summary:	A minicmd-plugin for the Xfce panel
Name:		xfce-verve-plugin
Version:	0.3.5
Release:	%mkrel 7
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/verve-plugin
Source0:	http://goodies.xfce.org/releases/verve-plugin/%{oname}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.3
Requires:	exo
BuildRequires:	xfce4-panel-devel >= 4.3
BuildRequires:	exo-devel >= 0.3.1.3
BuildRequires:	libxfcegui4-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	pcre-devel
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This plugin is like the (quite old) xfce4-minicmd-plugin, except that it
feature more cool features, like autocompletion and command history.
And more are yet to come!
A MUST!

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#fix name and location of bin file
rm -rf %{buildroot}/usr/bin
mkdir  %{buildroot}%{_bindir}
install -m 755 scripts/verve-focus %{buildroot}%{_bindir}/

%find_lang %{oname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README THANKS TODO
%{_bindir}/verve-focus
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libdir}/xfce4/panel-plugins/*
