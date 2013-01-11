Summary:	KNutClient - KDE client for UPS systems using NUT
Summary(pl.UTF-8):	KNutClient - klient KDE dla systemów UPS korzystających z NUT-a
Name:		knutclient
Version:	1.0.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.buzuluk.cz/pub/alo/knutclient/stable/%{name}-%{version}.tar.gz
# Source0-md5:	b01cc17ef72c7598f51cc7cd98e3bf40
Patch0:		%{name}-automakeversion.patch
URL:		http://www.alo.cz/knutclient/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNutClient is a visual KDE client for UPS systems using NUT - Network
UPS Tools.

%description -l pl.UTF-8
KNutClient to klient systemów UPS używających NUT-a (Network UPS
Tools), napisany pod KDE.

%prep
%setup -q

%build
cd build
cmake .. \
	-DCMAKE_INSTALL_PREFIX=/usr/ \
	-DCMAKE_BUILD_TYPE=Release
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/knutclient
%{_datadir}/apps/knutclient
%{_desktopdir}/kde4/knutclient.desktop
%{_iconsdir}/hicolor/*/apps/*
