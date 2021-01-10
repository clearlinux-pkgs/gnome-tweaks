#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-tweaks
Version  : 3.34.1
Release  : 21
URL      : https://download.gnome.org/sources/gnome-tweaks/3.34/gnome-tweaks-3.34.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-tweaks/3.34/gnome-tweaks-3.34.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0
Requires: gnome-tweaks-bin = %{version}-%{release}
Requires: gnome-tweaks-data = %{version}-%{release}
Requires: gnome-tweaks-libexec = %{version}-%{release}
Requires: gnome-tweaks-locales = %{version}-%{release}
Requires: gnome-tweaks-python = %{version}-%{release}
Requires: gnome-tweaks-python3 = %{version}-%{release}
Requires: pygobject
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pygobject

%description
GNOME TWEAKS
================
BUILD
-----
The only build-time dependency is [meson](https://mesonbuild.com/).

%package bin
Summary: bin components for the gnome-tweaks package.
Group: Binaries
Requires: gnome-tweaks-data = %{version}-%{release}
Requires: gnome-tweaks-libexec = %{version}-%{release}

%description bin
bin components for the gnome-tweaks package.


%package data
Summary: data components for the gnome-tweaks package.
Group: Data

%description data
data components for the gnome-tweaks package.


%package libexec
Summary: libexec components for the gnome-tweaks package.
Group: Default

%description libexec
libexec components for the gnome-tweaks package.


%package locales
Summary: locales components for the gnome-tweaks package.
Group: Default

%description locales
locales components for the gnome-tweaks package.


%package python
Summary: python components for the gnome-tweaks package.
Group: Default
Requires: gnome-tweaks-python3 = %{version}-%{release}

%description python
python components for the gnome-tweaks package.


%package python3
Summary: python3 components for the gnome-tweaks package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gnome-tweaks package.


%prep
%setup -q -n gnome-tweaks-3.34.1
cd %{_builddir}/gnome-tweaks-3.34.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610303297
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-tweaks

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-tweaks

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.tweaks.desktop
/usr/share/gnome-tweaks/shell.css
/usr/share/gnome-tweaks/shell.ui
/usr/share/icons/hicolor/scalable/apps/org.gnome.tweaks.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.tweaks-symbolic.svg
/usr/share/metainfo/org.gnome.tweaks.appdata.xml

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-tweak-tool-lid-inhibitor

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f gnome-tweaks.lang
%defattr(-,root,root,-)

