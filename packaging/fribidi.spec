Name:           fribidi
Version:        0.19.4
Release:        1
Summary:        Free Implementation of BiDi Algorithm
License:        LGPL-2.1
Group:          System/Libraries
Url:            http://fribidi.org/
AutoReqProv:    on
Provides:       locale(ar;he)
Source:         fribidi-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  pkg-config

%description
This library implements the algorithm as described in the "Unicode
Standard Annex #9, the Bidirectional Algorithm,
http://www.unicode.org/unicode/reports/tr9/". FriBidi is exhaustively
tested against the Bidi Reference Code and, to the best of the
developers' knowledge, does notcontain any conformance bugs.

The API was inspired by the document "Bi-Di languages support - BiDi
API proposal" by Franck Portaneri, which he wrote as a proposal for
adding BiDi support to Mozilla.

%package devel
License:        LGPL-2.1
Summary:        Development Files for FriBiDi
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       pkg-config

%description devel
This package provides headers and manual files for FriBiDi.

%prep
%setup -q

%build
%configure --disable-static
%__make %{?_smp_mflags}

%check
%__make check

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/fribidi
%{_libdir}/libfribidi.so.*
%license COPYING

%files devel
%defattr(-, root, root)
%dir %{_includedir}/fribidi
%{_includedir}/fribidi/*
%{_libdir}/libfribidi.so
%{_libdir}/pkgconfig/fribidi.pc
%doc %{_mandir}/man3/fribidi_*

%changelog
