Summary:	Kconfigure simplifies compiling and installing software by providing a graphical interface
Summary(pl):	Kconfigure dostarcza graficznego interfejsu upraszczaj±cego kompilacjê i instalacjê oprogramowania
Name:		kconfigure
Version:	1.2
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://kconfigure.sourceforge.net
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	qt-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
Kconfigure is a KDE program to compile the sources without the xterm or console. Easy to use, click in konqueror the
configure file and configure, make and install the sources in the gui with kconfigure.

%description -l pl
Kconfigure jest programem pod KDE s³u¿±cym do kompilacji ¼róde³ bez xterma czy konsoli. £atwy w u¿yciu, wystarczy
klikn±æ w konquerorze na pliku configure aby przej¶æ przez proces konfiguracji, kompilacji i instalacji ¼róde³ w gui
kconfigure.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Development/Tools
mv $RPM_BUILD_ROOT/%{_applnkdir}/Applications/kconfigure.desktop $RPM_BUILD_ROOT%{_applnkdir}/Development/Tools/kconfigure.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/bin/kconfigure
%{_applnkdir}/Development/Tools/kconfigure.desktop
%{_prefix}/share/apps/kconfigure/pics/*
%{_prefix}/share/apps/kconfigure/eventsrc
%{_pixmapsdir}/hicolor/16x16/apps/kconfigure.png
%{_pixmapsdir}/hicolor/16x16/mimetypes/configure.png
%{_pixmapsdir}/hicolor/32x32/apps/kconfigure.png
%{_pixmapsdir}/hicolor/32x32/mimetypes/configure.png
%{_pixmapsdir}/hicolor/48x48/apps/kconfigure.png
%{_pixmapsdir}/hicolor/48x48/mimetypes/configure.png
%{_prefix}/share/locale/es/LC_MESSAGES/kconfigure.mo
%{_prefix}/share/locale/fr/LC_MESSAGES/kconfigure.mo
%{_prefix}/share/mimelnk/text/x-configure.desktop
