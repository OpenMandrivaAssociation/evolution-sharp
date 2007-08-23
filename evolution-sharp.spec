%define name evolution-sharp
%define version 0.13.3
%define release %mkrel 1

Summary: Evolution C# bindings for mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: evolution-devel >= 2.5
BuildRequires: evolution-data-server-devel >= 1.5
BuildRequires: mono-devel
BuildRequires: gtk-sharp2
BuildRequires: gtk-sharp2-devel
Requires: evolution

%description
Evolution# is a .NET language binding for various Ximian Evolution (tm)
libraries.

%prep
%setup -q

%build
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


