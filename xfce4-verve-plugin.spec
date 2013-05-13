%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A minicmd-plugin for the Xfce panel
Name:		xfce4-verve-plugin
Version:	1.0.0
Release:	5
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-verve-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-verve-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
BuildRequires:	exo-devel >= 0.6.0
BuildRequires:	pkgconfig(libxfcegui4-1.0)
BuildRequires:	dbus-glib-devel
BuildRequires:	pcre-devel
BuildRequires:	perl(XML::Parser)

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
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README THANKS
%{_bindir}/verve-focus
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libdir}/xfce4/panel-plugins/*


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-4mdv2012.0
+ Revision: 791568
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-3
+ Revision: 790033
- Rebuild

* Thu Feb 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-2
+ Revision: 772266
- Rebuild

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1
+ Revision: 632787
- update to new version 1.0.0
- update url for Source0
- fix docs list

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.6-4mdv2010.1
+ Revision: 543445
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.3.6-3mdv2010.0
+ Revision: 446154
- rebuild

* Fri Mar 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.6-2mdv2009.1
+ Revision: 349538
- rebuild for xfce-4.6.0

* Mon Nov 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.6-1mdv2009.1
+ Revision: 306384
- update to new version 0.3.6
- new license policy
- spec file clean
- change name to be closer with upstream

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5-7mdv2009.1
+ Revision: 294987
- rebuild for new Xfce4.6 beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.3.5-6mdv2009.0
+ Revision: 262428
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.3.5-5mdv2009.0
+ Revision: 257039
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Nov 21 2007 Jérôme Soyer <saispo@mandriva.org> 0.3.5-3mdv2008.1
+ Revision: 111063
- Fix BuildRequires and Requires

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5-2mdv2008.0
+ Revision: 33271
- spec file clean

