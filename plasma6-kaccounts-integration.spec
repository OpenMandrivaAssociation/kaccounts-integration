%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Small system to administer web accounts across the KDE desktop
Name:		plasma6-kaccounts-integration
Version:	24.01.95
Release:	1
License:	GPLv2+
Group:		System/Base
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kaccounts-integration-%{version}.tar.xz
URL:		https://www.kde.org/

BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DAV)
BuildRequires:	kdepimlibs-devel
BuildRequires:	pkgconfig(libsignon-qt6)
BuildRequires:	cmake(AccountsQt6)
BuildRequires:	pkgconfig(libaccounts-glib) >= 1.21
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
BuildRequires:	cmake(QCoro6)
Requires:	signon-plugin-oauth2
Requires:	signond >= 8.62
Requires:	signon-ui >= 0.17-0
Requires:	signon-kwallet-extension
Requires:	UbuntuOnlineAccounts-qml

%description
Small system to administer web accounts across the KDE desktop.

%files -f kaccounts-integration.lang
%_qtdir/qml/org/kde/kaccounts
%{_libdir}/qt6/plugins/kf6/kded/kded_accounts.so
%{_libdir}/qt6/plugins/kaccounts
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kaccounts.so
%{_datadir}/applications/kcm_kaccounts.desktop

#--------------------------------------------------------------------

%define kaccounts_major %(echo %{version} |cut -d. -f1)
%define libkaccounts %mklibname kaccounts6

%package -n %{libkaccounts}
Summary:	Small system to administer web accounts across the KDE desktop
Group:		System/Libraries
Requires:	%{name} >= %{EVRD}
Obsoletes:	%{mklibname kaccounts 16} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 16} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 17} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 18} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 19} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 20} < %{EVRD}
Obsoletes:	%{mklibname kaccounts 21} < %{EVRD}

%description -n %{libkaccounts}
Small system to administer web accounts across the KDE desktop.

%files -n %{libkaccounts}
%_libdir/libkaccounts6.so.%{kaccounts_major}*
%_libdir/libkaccounts6.so.2

#--------------------------------------------------------------------

%define kaccounts_devel %mklibname kaccounts6 -d

%package -n %{kaccounts_devel}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkaccounts} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
# intltool-merge is used by KAccountsMacros.cmake
Requires:	intltool

%description -n %{kaccounts_devel}
This package contains header files needed if you wish to build applications
based on %name.

%files -n %{kaccounts_devel}
%_includedir/KAccounts6
%_libdir/cmake/KAccounts6
%_libdir/libkaccounts6.so

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n kaccounts-integration-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kaccounts-integration
