Name:       alsa-lib
Summary:    The Advanced Linux Sound Architecture (ALSA) library
Version:    1.2.8
Release:    1
License:    LGPLv2+
URL:        http://www.alsa-project.org/
Source0:    %{name}-%{version}.tar.gz
Source1:    asound.conf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
Requires(post): coreutils
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA runtime libraries to simplify application
programming and provide higher level functionality as well as support for
the older OSS API, providing binary compatibility for most OSS programs.

%package devel
Summary:    Development files from the ALSA library
Requires:   %{name} = %{version}-%{release}

%description devel
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA development libraries for developing
against the ALSA libraries and interfaces.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man and info pages for %{name}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build

%reconfigure --disable-static \
    --disable-aload

%make_build

%install
%make_install
install -D -p -m 0644 %{SOURCE1} %{buildroot}/etc/asound.conf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%config %{_sysconfdir}/asound.conf
%{_libdir}/libasound.so.*
%{_libdir}/libatopology.so.*
%{_bindir}/aserver
%{_datadir}/alsa/

%files devel
%defattr(-,root,root,-)
%{_includedir}/alsa
%{_includedir}/asoundlib.h
%{_includedir}/sys/asoundlib.h
%{_libdir}/libasound.so
%{_libdir}/libatopology.so
%{_libdir}/pkgconfig/alsa.pc
%{_libdir}/pkgconfig/alsa-topology.pc
%{_datadir}/aclocal/alsa.m4

%files doc
%defattr(-,root,root,-)
%doc ChangeLog TODO doc/asoundrc.txt
