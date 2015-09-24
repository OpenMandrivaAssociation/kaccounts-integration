#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

%define rel 1

Summary:        Small system to administer web accounts across the KDE desktop
Name:           kaccounts-integration
Version: 15.08.1
Release:        %mkrel %rel
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz
URL:            https://www.kde.org/

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)

BuildRequires:  kf5-macros
BuildRequires:  kcmutils-devel
BuildRequires:  kio-devel
BuildRequires:  ki18n-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kconfig-devel
BuildRequires:  kwallet-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdepimlibs-devel

BuildRequires:  pkgconfig(libsignon-qt5)
BuildRequires:  pkgconfig(accounts-qt5)

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
Small system to administer web accounts across the KDE desktop

%files 
%_qt5_plugindir/*.so
%_qt5_plugindir/kaccounts/daemonplugins/kaccounts_akonadi_plugin.so
%_kf5_qmldir/org/kde/kaccounts
%_kf5_services/kcm_kaccounts.desktop
%_kf5_services/kded/accounts.desktop

#--------------------------------------------------------------------

%define kaccounts_major 15
%define libkaccounts %mklibname kaccounts %{kaccounts_major}

%package -n %libkaccounts
Summary:      Small system to administer web accounts across the KDE desktop
Group:        System/Libraries


%description -n %libkaccounts
Small system to administer web accounts across the KDE desktop

%files -n %libkaccounts
%_kf5_libdir/libkaccounts.so.%{kaccounts_major}*
%_kf5_libdir/libkaccounts.so.1

#--------------------------------------------------------------------

%define kaccounts_devel %mklibname kaccounts -d

%package -n %kaccounts_devel

Summary:        Devel stuff for %name
Group:          Development/KDE and Qt
Requires:       %name = %version-%release
Requires:       %libkaccounts = %version-%release
Provides:       %name-devel = %{version}-%{release}

%description -n %kaccounts_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %kaccounts_devel
%_includedir/KAccounts
%_libdir/cmake/KAccounts
%_kf5_libdir/libkaccounts.so

#--------------------------------------------------------------------

%prep
%setup -q 
%autopatch -p1

%build
%cmake_kf5
%make

%install
%makeinstall_std -C build



%changelog
* Fri Sep 18 2015 neoclust <neoclust> 15.08.1-1.mga6
+ Revision: 880394
- New version 15.08.1

* Thu Aug 27 2015 neoclust <neoclust> 15.08.0-2.mga6
+ Revision: 870329
- Remove wrong patch

* Wed Aug 19 2015 neoclust <neoclust> 15.08.0-1.mga6
+ Revision: 865912
- New version 15.08.0

* Wed Aug 12 2015 neoclust <neoclust> 15.07.90-2.mga6
+ Revision: 863928
- Plasma Mass Rebuild - Rebuild for new Plasma

* Sun Aug 09 2015 neoclust <neoclust> 15.07.90-1.mga6
+ Revision: 861725
- New version 15.07.90

* Fri Jul 31 2015 wally <wally> 15.07.80-2.mga6
+ Revision: 860144
- add patch to fix paths in CMake files

* Fri Jul 31 2015 neoclust <neoclust> 15.07.80-1.mga6
+ Revision: 859328
- New version 15.07.80

* Sun Jul 19 2015 neoclust <neoclust> 15.04.3-2.mga6
+ Revision: 855266
- Rebuild with correct name

* Sun Jul 19 2015 neoclust <neoclust> 15.04.3-1.mga6
+ Revision: 855253
- imported package kaccounts-integration

