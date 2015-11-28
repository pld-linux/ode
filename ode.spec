# TODO:
# - system libccd
# - assertion "bNormalizationResult" failed in _dNormalize3()
#   [what conditions? assert fails when passed 0-length vector, which cannot be normalized]
#
Summary:	ODE - library for simulating articulated rigid body dynamics
Summary(pl.UTF-8):	ODE - biblioteka służąca do symulacji dynamiki bryły sztywnej
Name:		ode
Version:	0.12
Release:	3
Epoch:		1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opende/%{name}-%{version}.tar.bz2
# Source0-md5:	48fdd41fae1a7e7831feeded09826599
URL:		http://ode.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.10
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	python-Cython >= 0.14.1
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Summary:	Header files for ODE library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ODE
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for ODE library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ODE.

%package static
Summary:	Static ODE library
Summary(pl.UTF-8):	Statyczna biblioteka ODE
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static ODE library.

%description static -l pl.UTF-8
Statyczna biblioteka ODE.

%package -n python-ode
Summary:	Python binding for ODE library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki ODE
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n python-ode
Python binding for ODE library.

%description -n python-ode -l pl.UTF-8
Wiązanie Pythona do biblioteki ODE.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-libccd \
	--enable-shared
%{__make}

srcdir="$(pwd)"
cd bindings/python
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CPPFLAGS="%{rpmcppflags} -I$srcdir/include -DdSINGLE" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd bindings/python
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libode.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt README.txt
%attr(755,root,root) %{_libdir}/libode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libode.so.3

%files devel
%defattr(644,root,root,755)
%doc ode/{README,TODO} ode/doc/{main.dox,pix}
%attr(755,root,root) %{_bindir}/ode-config
%attr(755,root,root) %{_libdir}/libode.so
%{_includedir}/ode
%{_pkgconfigdir}/ode.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libode.a

%files -n python-ode
%defattr(644,root,root,755)
%doc bindings/python/TODO.txt
%attr(755,root,root) %{py_sitedir}/ode.so
%{py_sitedir}/Open_Dynamics_Engine-0.1-py*.egg-info
