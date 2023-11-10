#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kalk
Summary:	kalk
Name:		ka5-%{kaname}
Version:	23.08.3
Release:	1
License:	BSD 2 Clause/BSD 3 Clause/GPL v2+/GPL v3+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5f762b5392d58183317f7fd1e2bcfa8d
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.15.10
BuildRequires:	Qt5Qml-devel >= 5.15.10
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.89.0
BuildRequires:	kf5-kconfig-devel >= 5.89.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.89.0
BuildRequires:	kf5-ki18n-devel >= 5.89.0
BuildRequires:	kf5-kirigami2-devel >= 5.89.0
BuildRequires:	kf5-kunitconversion-devel >= 5.89.0
BuildRequires:	mpfr-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kalk is a convergent calculator application built with the Kirigami framework.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalk
%{_desktopdir}/org.kde.kalk.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.kalk.svg
%{_datadir}/metainfo/org.kde.kalk.appdata.xml
