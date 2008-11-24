Summary:	ODE is a library for simulating articulated rigid body dynamics
Summary(pl.UTF-8):	ODE jest biblioteką służącą do symulacji dynamiki bryły sztywnej
Name:		ode
Version:	0.10.1
Release:	1
Epoch:		1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/opende/%{name}-%{version}.tar.bz2
# Source0-md5:	91c396b915539a760617437d56eb1681
URL:		http://ode.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Open Dynamics Engine (ODE) is a free software library for the
simulation of Rigid Body Dynamics. ODE is useful for simulating things
like vehicles, objects in virtual reality environments, and virtual
creatures.

%description -l pl.UTF-8
Open Dynamics Engine (ODE) jest wolną biblioteką służącą do
symulacji dynamiki bryły sztywnej. ODE jest użyteczne przy symulacji
pojazdów, obiektów w przestrzeni wirtualnej i wirtualnych stworzeń.

%package devel
Summary:	Header files for ODE libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek ODE
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for ODE libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek ODE.

%package static
Summary:	Static ODE libraries
Summary(pl.UTF-8):	Statyczne biblioteki ODE
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static ODE libraries.

%description static -l pl.UTF-8
Statyczne biblioteki ODE.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt README.txt
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ode/{README,TODO} ode/doc/{main.dox,pix}
%attr(755,root,root) %{_bindir}/ode-config
%attr(755,root,root) %{_libdir}/libode.so
%{_libdir}/libode.la
%{_includedir}/ode

%files static
%defattr(644,root,root,755)
%{_libdir}/libode.a
