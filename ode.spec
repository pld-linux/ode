Summary:	ODE is a library for simulating articulated rigid body dynamics
Summary(pl):	ODE jest bibliotek± s³u¿±c± do symulacji dynamiki bry³y sztywnej
Name:		ode
Version:	0.039
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/opende/%{name}-%{version}.tgz
# Source0-md5:	5a6675043791dc432eb56c58d87f6180
URL:		http://q12.org/ode/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Open Dynamics Engine (ODE) is a free software library for the
simulation of Rigid Body Dynamics. ODE is useful for simulating things
like vehicles, objects in virtual reality environments, and virtual
creatures.

%description -l pl
Open Dynamics Engine (ODE) jest woln± bibliotek± s³u¿±c± do symulacji
dynamiki bry³y sztywnej. ODE jest u¿yteczne przy symulacji pojazdów,
obiektów w przestrzeni wirtualnej i witrualnych stworzeñ.

%package devel
Summary:	Header files for ODE library
Summary(pl):	Pliki nag³ówkowe biblioteki ODE
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for ODE library.

%description devel -l pl
Pliki nag³ówkowe biblioteki ODE.

%prep
%setup -q

%build
%{__make} configure
%{__make} ode-lib \
	C_FLAGS="-c -fno-rtti -fno-exceptions -ffast-math -Iinclude -DdNODEBUG \
	%{rpmcflags}"
%{__make} drawstuff-lib \
	C_FLAGS="-c -fno-rtti -fno-exceptions -ffast-math -Iinclude -DdNODEBUG \
	%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install lib/lib* $RPM_BUILD_ROOT%{_libdir}
cp -R include/* $RPM_BUILD_ROOT%{_includedir}

rm -f $RPM_BUILD_ROOT%{_includedir}/%{name}/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{_libdir}/lib*.a

%files devel
%defattr(644,root,root,755)
%doc ode/{README,TODO} ode/doc/{ode.html,pix}
%{_includedir}/*
