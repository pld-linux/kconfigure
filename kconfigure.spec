Summary:	Simplifies compiling and installing software by providing a graphical interface
Summary(pl):	Graficzny interfejs upraszczaj±cy kompilacjê i instalowanie oprogramowania
Name:		kconfigure
Version:	1.2
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f0f5f5758364a91828dd528a49fb968e
Source1:	http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:  81e0b2f79ef76218381270960ac0f55f
URL:		http://kconfigure.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	qt-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)



%description
Kconfigure is a KDE program to compile the sources without the xterm
or other text terminal. Easy to use, click in konqueror the configure
file and configure, make and install the sources in the gui with
kconfigure.

%description -l pl
Kconfigure jest programem pod KDE s³u¿±cym do kompilacji ¼róde³ bez
xterma czy innego terminala tekstowego. Jest ³atwy w u¿yciu, wystarczy
klikn±æ w konquerorze na pliku configure aby przej¶æ przez proces
konfiguracji, kompilacji i instalacji ¼róde³ w graficznym interfejsie
kconfigure.

%prep
%setup -q -a1

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/kconfigure.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

echo "Categories=Qt;KDE;Development;Building;" >>  $RPM_BUILD_ROOT%{_desktopdir}/kconfigure.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kconfigure
%dir %{_datadir}/apps/kconfigure
%dir %{_datadir}/apps/kconfigure/pics
%{_datadir}/apps/kconfigure/pics/*
%{_datadir}/apps/kconfigure/eventsrc
%{_iconsdir}/hicolor/16x16/apps/kconfigure.png
%{_iconsdir}/hicolor/16x16/mimetypes/configure.png
%{_iconsdir}/hicolor/32x32/apps/kconfigure.png
%{_iconsdir}/hicolor/32x32/mimetypes/configure.png
%{_iconsdir}/hicolor/48x48/apps/kconfigure.png
%{_iconsdir}/hicolor/48x48/mimetypes/configure.png
%{_desktopdir}/kconfigure.desktop
%{_datadir}/mimelnk/text/x-configure.desktop
