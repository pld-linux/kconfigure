Summary:	Simplifies compiling and installing software by providing a graphical interface
Summary(pl):	Graficzny interfejs upraszczaj±cy kompilacjê i instalowanie oprogramowania
Name:		kconfigure
Version:	2.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/kconfigure/%{name}-%{version}.tar.gz
# Source0-md5:	5b9094af94efdc65ec14fe7f5a7c7ef8
URL:		http://kconfigure.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
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
%setup -q -n %{name}

sed -i -e 's/^Categories=.*/Categories=Qt;KDE;Development;Building;/' kconfigure/kconfigure.desktop

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	mangdir=%{_mandir}/man1

gzip -d $RPM_BUILD_ROOT%{_mandir}/man1/kconfigure.1.gz

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/kconfigure.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kconfigure
%{_datadir}/apps/kconfigure
%{_iconsdir}/hicolor/16x16/apps/kconfigure.png
%{_iconsdir}/hicolor/32x32/apps/kconfigure.png
%{_iconsdir}/hicolor/32x32/mimetypes/configure.png
%{_iconsdir}/hicolor/48x48/apps/kconfigure.png
%{_iconsdir}/hicolor/48x48/mimetypes/configure.png
%{_desktopdir}/kconfigure.desktop
%{_datadir}/mimelnk/text/x-configure.desktop
%{_mandir}/man1/kconfigure.1*
