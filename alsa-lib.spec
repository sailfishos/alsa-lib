Name:       alsa-lib
Summary:    The Advanced Linux Sound Architecture (ALSA) library
Version:    1.0.26
Release:    2
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.alsa-project.org/
Source0:    ftp://ftp.alsa-project.org/pub/lib/alsa-lib-%{version}.tar.bz2
Source1:    asound.conf
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
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA development libraries for developing
against the ALSA libraries and interfaces.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Man and info pages for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static \
    --disable-aload

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/etc
cp -a %{SOURCE1} %{buildroot}/etc

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        ChangeLog TODO doc/asoundrc.txt

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%config %{_sysconfdir}/asound.conf
%{_libdir}/libasound.so.*
%{_bindir}/aserver
%{_libdir}/alsa-lib/
%{_datadir}/alsa/

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/alsa
%{_includedir}/alsa/*.h
%{_includedir}/alsa/sound/*.h
%{_includedir}/sys/asoundlib.h
%{_libdir}/libasound.so
%{_libdir}/pkgconfig/alsa.pc
%{_datadir}/aclocal/alsa.m4

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
