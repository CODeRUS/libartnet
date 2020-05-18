Name:		libartnet
Version:	1.1.2
Release:	2
Summary:	An Open Source implementation of the ArtNet protocol
Group:      System/Libraries
License:	LGPL
URL:		https://www.openlighting.org/libartnet-main/
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  libtool

%description
Libartnet is an implementation of the ArtNet protocol. ArtNet allows the
transmission of DMX and related data over IP networks.

%package devel
Summary:	Libraries and header files for %{name}
Requires:	%{name}% = %{version}-%{release}

%description devel
Libraries and header files for %{name}

%prep
%setup -q  -n %{name}-%{version}/upstream

%build
autoreconf -fi
./configure --prefix=/usr
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
