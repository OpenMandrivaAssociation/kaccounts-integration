#define debug_package %{nil}

Summary:	Small system to administer web accounts across the KDE desktop
Name:		kaccounts-integration
Version:	15.08.2
Release:	2
License:	GPLv2+
Group:		System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz
URL:		https://www.kde.org/

BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	kdepimlibs-devel

BuildRequires:	pkgconfig(libsignon-qt5)
BuildRequires:	pkgconfig(accounts-qt5)

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
Requires:	signon-plugin-oauth2

%description
Small system to administer web accounts across the KDE desktop

%files
%_qt5_plugindir/*.so
%_qt5_plugindir/kaccounts/daemonplugins/kaccounts_akonadi_plugin.so
%_kde5_qmldir/org/kde/kaccounts
%_kde5_services/kcm_kaccounts.desktop
%_kde5_services/kded/accounts.desktop

#--------------------------------------------------------------------

%define kaccounts_major 15
%define libkaccounts %mklibname kaccounts %{kaccounts_major}

%package -n %{libkaccounts}
Summary:	Small system to administer web accounts across the KDE desktop
Group:		System/Libraries

%description -n %{libkaccounts}
Small system to administer web accounts across the KDE desktop.

%files -n %{libkaccounts}
%_kde5_libdir/libkaccounts.so.%{kaccounts_major}*
%_kde5_libdir/libkaccounts.so.1

#--------------------------------------------------------------------

%define kaccounts_devel %mklibname kaccounts -d

%package -n %{kaccounts_devel}
Summary:	Devel stuff for %name
Group:		Development/KDE and Qt
Requires:	%name = %version-%release
Requires:	%libkaccounts = %version-%release
Provides:	%name-devel = %{version}-%{release}

%description -n %{kaccounts_devel}
This package contains header files needed if you wish to build applications
based on %name.

%files -n %{kaccounts_devel}
%_includedir/KAccounts
%_libdir/cmake/KAccounts
%_kde5_libdir/libkaccounts.so

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

