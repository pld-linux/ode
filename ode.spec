Summary:	ODE is a library for simulating articulated rigid body dynamics
Summary(pl):	ODE jest bibliotek± s³u¿±c± do symulacji dynamiki bry³y sztywnej
Name:		ode
Version:	0.5
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/opende/%{name}-%{version}.tgz
# Source0-md5:	b33b21e04ee9661f27802b6b6c8eefd2
Patch0:		%{name}-asm.patch
URL:		http://q12.org/ode/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Open Dynamics Engine (ODE) is a free software library for the
simulation of Rigid Body Dynamics. ODE is useful for simulating things
like vehicles, objects in virtual reality environments, and virtual
creatures.

%description -l pl
Open Dynamics Engine (ODE) jest woln± bibliotek± s³u¿±c± do symulacji
dynamiki bry³y sztywnej. ODE jest u¿yteczne przy symulacji pojazdów,
obiektów w przestrzeni wirtualnej i wirtualnych stworzeñ.

%package devel
Summary:	Header files for ODE libraries
Summary(pl):	Pliki nag³ówkowe bibliotek ODE
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	OpenGL-devel
Requires:	XFree86-devel
Requires:	libstdc++-devel

%description devel
Header files for ODE libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek ODE.

%package static
Summary:	Static ODE libraries
Summary(pl):	Statyczne biblioteki ODE
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static ODE libraries.

%description static -l pl
Statyczne biblioteki ODE.

%prep
%setup -q
%patch0 -p1

%build
%{__make} configure
%{__make} ode-lib \
	CC="libtool --mode=compile %{__cc}" \
	C_FLAGS="-c -fno-rtti -fno-exceptions -ffast-math -Iinclude -DdNODEBUG \
	%{rpmcflags}"
libtool --mode=link %{__cxx} -o lib/libode.la ode/src/*.lo -rpath %{_libdir}

%{__make} drawstuff-lib \
	CC="libtool --mode=compile %{__cc}" \
	C_FLAGS="-c -fno-rtti -fno-exceptions -ffast-math -Iinclude -DdNODEBUG \
	%{rpmcflags}"
libtool --mode=link %{__cxx} -o lib/libdrawstuff.la drawstuff/src/*.lo \
	-rpath %{_libdir} -L/usr/X11R6/lib -lX11 -lGL -lGLU

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

libtool --mode=install install lib/libode.la $RPM_BUILD_ROOT%{_libdir}
libtool --mode=install install lib/libdrawstuff.la $RPM_BUILD_ROOT%{_libdir}

cp -R include/* $RPM_BUILD_ROOT%{_includedir}
rm -f $RPM_BUILD_ROOT%{_includedir}/%{name}/README

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc ode/{README,TODO} ode/doc/{ode.html,pix}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
