#sbs-git:slp/unmodified/fribidi fribidi 0.19.5 b36fcb1ced2e1294dd147e36f120f5161e53406d

Name:           fribidi
Version:        0.19.5
Release:        5
License:        LGPL-2.0+
Summary:        Library implementing the Unicode Bidirectional Algorithm
Url:            http://fribidi.org
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%package devel
Summary:        Libraries and include files for FriBidi
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Include files and libraries needed for developing applications which use
FriBidi.

%prep
%setup -q


%build

%configure --disable-static
make %{?_smp_mflags}

%install
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc README AUTHORS COPYING ChangeLog THANKS NEWS TODO
%{_bindir}/fribidi
%{_libdir}/libfribidi.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/fribidi
%{_libdir}/libfribidi.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/%{name}_*.gz

