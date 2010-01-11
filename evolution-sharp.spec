%define name evolution-sharp
%define version 0.21.1
%define release %mkrel 3

Summary: Evolution C# bindings for mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0: evolution-sharp-0.21.1-adopt-newer-evo.patch
License: GPL
Group: Development/Other
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: evolution-data-server-devel >= 1.5
BuildRequires: mono-devel
BuildRequires: gtk-sharp2
BuildRequires: gtk-sharp2-devel
BuildRequires: gnome-common
Requires: evolution

%description
Evolution# is a .NET language binding for various Ximian Evolution (tm)
libraries.

%prep
%setup -q
%patch0 -p1

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/lib*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MAINTAINERS AUTHORS ChangeLog
%_prefix/lib/mono/evolution-sharp/
%_prefix/lib/mono/gac/evolution-sharp/
%_libdir/libevolutionglue.so
%_libdir/pkgconfig/evolution-sharp.pc
%_datadir/gapi-2.0/evolution-api.xml


