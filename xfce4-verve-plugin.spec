Summary:	A minicmd-plugin for the Xfce panel
Name:		xfce4-verve-plugin
Version:	0.3.6
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-verve-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-verve-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.3
Requires:	exo
BuildRequires:	xfce4-panel-devel >= 4.3
BuildRequires:	exo-devel >= 0.3.1.3
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
And more are yet to come!
A MUST!

%prep
%setup -q

%build
%configure2_5x \
	--enable-final

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#fix name and location of bin file
rm -rf %{buildroot}/usr/bin
mkdir  %{buildroot}%{_bindir}
install -m 755 scripts/verve-focus %{buildroot}%{_bindir}/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README THANKS TODO
%{_bindir}/verve-focus
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libdir}/xfce4/panel-plugins/*
