#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v4
# autospec commit: da8b975
#
Name     : gnome-tweaks
Version  : 45.1
Release  : 44
URL      : https://download.gnome.org/sources/gnome-tweaks/45/gnome-tweaks-45.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-tweaks/45/gnome-tweaks-45.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0
Requires: gnome-tweaks-bin = %{version}-%{release}
Requires: gnome-tweaks-data = %{version}-%{release}
Requires: gnome-tweaks-locales = %{version}-%{release}
Requires: gnome-tweaks-python = %{version}-%{release}
Requires: gnome-tweaks-python3 = %{version}-%{release}
Requires: pygobject
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(libhandy-1)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GNOME Tweaks
=============================
[Repository](https://gitlab.gnome.org/GNOME/gnome-tweaks)

%package bin
Summary: bin components for the gnome-tweaks package.
Group: Binaries
Requires: gnome-tweaks-data = %{version}-%{release}

%description bin
bin components for the gnome-tweaks package.


%package data
Summary: data components for the gnome-tweaks package.
Group: Data

%description data
data components for the gnome-tweaks package.


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
%setup -q -n gnome-tweaks-45.1
cd %{_builddir}/gnome-tweaks-45.1
pushd ..
cp -a gnome-tweaks-45.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707751022
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-tweaks
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-tweaks

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.tweaks.desktop
/usr/share/glib-2.0/schemas/org.gnome.tweaks.gschema.xml
/usr/share/gnome-tweaks/shell.css
/usr/share/gnome-tweaks/shell.ui
/usr/share/gnome-tweaks/tweaks.ui
/usr/share/icons/hicolor/scalable/apps/org.gnome.tweaks.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.tweaks-symbolic.svg
/usr/share/metainfo/org.gnome.tweaks.appdata.xml

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f gnome-tweaks.lang
%defattr(-,root,root,-)

