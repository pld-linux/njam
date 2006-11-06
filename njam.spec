#
# Conditional build:
%bcond_without	SDL_mixer	# build without SDL_mixer
#
Summary:	Fast paced multiplayer pacman clone
Summary(pl):	Sieciowy klon pacmana o szybkim tempie
Name:		njam
Version:	1.25
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/njam/%{name}-%{version}-src.tar.gz
# Source0-md5:	231fda022d309e1ef4a0d993ca693462
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://njam.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
%{?with_SDL_mixer:BuildRequires:	SDL_mixer-devel}
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Njam is fast-paced pac-man-like game. In this arcade you move through
the maze eating cookies and collecting powerups while trying to avoid
ghosts who chase you.

%description -l pl
Njam jest posiadaj±c± szybkie tempo gr± z rodzaju pac-man. W tej
zrêczno¶ciówce gracz porusza siê po labiryncie zbieraj±c ciastka i
dopalacze, staraj±c siê przy okazji unikaæ ¶cigaj±cych go duchów.

%prep
%setup -q -n %{name}-%{version}-src

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
