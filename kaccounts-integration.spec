#define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Small system to administer web accounts across the KDE desktop
Name:		kaccounts-integration
Version:	20.08.1
Release:	1
License:	GPLv2+
Group:		System/Base
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DAV)
BuildRequires:	kdepimlibs-devel
BuildRequires:	pkgconfig(libsignon-qt5)
BuildRequires:	pkgconfig(accounts-qt5)
BuildRequires:	pkgconfig(libaccounts-glib) >= 1.21
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
Requires:	signon-plugin-oauth2
Requires:	signond >= 8.58
Requires:	signon-ui >= 0.17-0
Requires:	signon-kwallet-extension
Requires:	UbuntuOnlineAccounts-qml

%description
Small system to administer web accounts across the KDE desktop.

%files -f %{name}.lang
%_kde5_qmldir/org/kde/kaccounts
%_kde5_services/kcm_kaccounts.desktop
%{_libdir}/qt5/plugins/kcms/kcm_kaccounts.so
%{_libdir}/qt5/plugins/kf5/kded/kded_accounts.so
%{_libdir}/qt5/plugins/kaccounts
%{_datadir}/kpackage/kcms/kcm_kaccounts

#--------------------------------------------------------------------

%define kaccounts_major %(echo %{version} |cut -d. -f1)
%define libkaccounts %mklibname kaccounts %{kaccounts_major}

%package -n %{libkaccounts}
Summary:	Small system to administer web accounts across the KDE desktop
Group:		System/Libraries
Requires:	%{name} >= %{EVRD}
Obsoletes:	%{mklibname kaccounts 15} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 16} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 17} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 18} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 19} < %{EVRD}

%description -n %{libkaccounts}
Small system to administer web accounts across the KDE desktop.

%files -n %{libkaccounts}
%_kde5_libdir/libkaccounts.so.%{kaccounts_major}*
%_kde5_libdir/libkaccounts.so.2

#--------------------------------------------------------------------

%define kaccounts_devel %mklibname kaccounts -d

%package -n %{kaccounts_devel}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkaccounts} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{kaccounts_devel}
This package contains header files needed if you wish to build applications
based on %name.

%files -n %{kaccounts_devel}
%_includedir/KAccounts
%_libdir/cmake/KAccounts
%_kde5_libdir/libkaccounts.so

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name}
