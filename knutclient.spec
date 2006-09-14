Summary:	KNutClient
Summary(pl):	KNutClient
Name:		knutclient
Version:	0.9
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.buzuluk.cz/pub/alo/knutclient/stable/%{name}-%{version}.tar.gz
# Source0-md5:	f63e4242b393e14df1b48739a7df1e35
URL:		http://www.alo.cz/knutclient/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNutClient is a visual KDE client for UPS systems using NUT - Network
UPS Tools.

%description -l pl
KNutClient to klient system�w UPS u�ywaj�cych NUT, napisany pod KDE.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL NEWS README
%attr(755,root,root) %{_bindir}/knutclient
%{_datadir}/applnk/Utilities/knutclient.desktop
%{_datadir}/apps/knutclient
%{_iconsdir}/hicolor/*/apps/*