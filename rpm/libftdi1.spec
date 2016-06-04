Summary:   Library to program and control the FTDI USB controller
Name:      libftdi1
Version:   1.0
Release:   1
License:   LGPL for libftdi and GPLv2+linking exception for the C++ wrapper
Group:     System Environment/Libraries
Vendor:    Intra2net AG
Source:    http://www.intra2net.com/en/developer/libftdi/download/%{name}-%{version}.tar.bz2
Buildroot: /tmp/%{name}-%{version}-root
Requires:  libusb1
BuildRequires: libusb1, libusb1-devel, pkgconfig, doxygen
BuildRequires: cmake
BuildRequires: swig
BuildRequires: boost-devel
BuildRequires: libconfuse-devel
Prefix:    /usr
URL:       http://www.intra2net.com/en/developer/libftdi

%package   devel
Summary:   Header files and static libraries for libftdi1
Group:     Development/Libraries
Requires:  libftdi1 = %{version}, libusb1-devel

%description 
Library to program and control the FTDI USB controller

%description devel
Header files and static libraries for libftdi1

%prep
%setup -q

%build

mkdir build
cd build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
cmake -DCMAKE_INSTALL_PREFIX="%{prefix}" ../

make %{?_smp_mflags}

%install
cd build
make DESTDIR=$RPM_BUILD_ROOT install

%postun
ldconfig

%post
ldconfig

# Remove example programs
rm -f $RPM_BUILD_ROOT/usr/bin/simple
rm -f $RPM_BUILD_ROOT/usr/bin/bitbang
rm -f $RPM_BUILD_ROOT/usr/bin/bitbang2
rm -f $RPM_BUILD_ROOT/usr/bin/bitbang_ft2232
rm -f $RPM_BUILD_ROOT/usr/bin/bitbang_cbus
rm -f $RPM_BUILD_ROOT/usr/bin/find_all
rm -f $RPM_BUILD_ROOT/usr/bin/find_all_pp
rm -f $RPM_BUILD_ROOT/usr/bin/serial_test
rm -f $RPM_BUILD_ROOT/usr/bin/baud_test

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING.LIB COPYING.GPL LICENSE
%{_libdir}/libftdi1*.so*
%{_libdir}/libftdipp1*.so*

%files devel
%defattr(-,root,root)
%doc build/doc/html build/doc/man
%{_bindir}/ftdi_eeprom
%{_bindir}/libftdi1-config
%{prefix}/include/libftdi1/*.h
%{prefix}/include/libftdi1/*.hpp
%{_libdir}/libftdi1*.*a
%{_libdir}/libftdipp1*.*a
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/libftdi1/*

