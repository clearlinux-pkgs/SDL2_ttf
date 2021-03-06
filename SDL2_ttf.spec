#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL2_ttf
Version  : 2.0.15
Release  : 20
URL      : https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.tar.gz
Source1  : https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.tar.gz.sig
Summary  : Simple DirectMedia Layer - Sample TrueType Font Library
Group    : Development/Tools
License  : FTL GPL-2.0 LGPL-2.1 Zlib
Requires: SDL2_ttf-lib = %{version}-%{release}
Requires: SDL2_ttf-license = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : pkg-config
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(x11)

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package dev
Summary: dev components for the SDL2_ttf package.
Group: Development
Requires: SDL2_ttf-lib = %{version}-%{release}
Provides: SDL2_ttf-devel = %{version}-%{release}
Requires: SDL2_ttf = %{version}-%{release}

%description dev
dev components for the SDL2_ttf package.


%package lib
Summary: lib components for the SDL2_ttf package.
Group: Libraries
Requires: SDL2_ttf-license = %{version}-%{release}

%description lib
lib components for the SDL2_ttf package.


%package license
Summary: license components for the SDL2_ttf package.
Group: Default

%description license
license components for the SDL2_ttf package.


%prep
%setup -q -n SDL2_ttf-2.0.15
cd %{_builddir}/SDL2_ttf-2.0.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600307421
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1600307421
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL2_ttf
cp %{_builddir}/SDL2_ttf-2.0.15/COPYING.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/b83c637448b14da11c48c8b3bcd811adf1fa91a7
cp %{_builddir}/SDL2_ttf-2.0.15/VisualC/external/lib/x64/LICENSE.freetype.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/05e53e853a9b22774a3bfae7c093fd4fb8d57ff0
cp %{_builddir}/SDL2_ttf-2.0.15/VisualC/external/lib/x64/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/9e9cec973c9a001fecefdf76e6160ce1899eae11
cp %{_builddir}/SDL2_ttf-2.0.15/VisualC/external/lib/x86/LICENSE.freetype.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/05e53e853a9b22774a3bfae7c093fd4fb8d57ff0
cp %{_builddir}/SDL2_ttf-2.0.15/VisualC/external/lib/x86/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/9e9cec973c9a001fecefdf76e6160ce1899eae11
cp %{_builddir}/SDL2_ttf-2.0.15/Xcode/Frameworks/FreeType.framework/Versions/A/Resources/LICENSE.freetype.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/085cea4f82cd31308e4713d5df13aa9baea80221
cp %{_builddir}/SDL2_ttf-2.0.15/debian/copyright %{buildroot}/usr/share/package-licenses/SDL2_ttf/013ddb1bf894657cdbf9844b7496ec2e30f8be59
cp %{_builddir}/SDL2_ttf-2.0.15/external/freetype-2.9.1/docs/GPLv2.TXT %{buildroot}/usr/share/package-licenses/SDL2_ttf/dac7127c82749e3107b53530289e1cd548860868
cp %{_builddir}/SDL2_ttf-2.0.15/external/freetype-2.9.1/docs/LICENSE.TXT %{buildroot}/usr/share/package-licenses/SDL2_ttf/64b7f213ddd72695d94866a1a9532ee5b3a472a8
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL_ttf.h
/usr/lib64/libSDL2_ttf.so
/usr/lib64/pkgconfig/SDL2_ttf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2_ttf-2.0.so.0
/usr/lib64/libSDL2_ttf-2.0.so.0.14.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL2_ttf/013ddb1bf894657cdbf9844b7496ec2e30f8be59
/usr/share/package-licenses/SDL2_ttf/05e53e853a9b22774a3bfae7c093fd4fb8d57ff0
/usr/share/package-licenses/SDL2_ttf/085cea4f82cd31308e4713d5df13aa9baea80221
/usr/share/package-licenses/SDL2_ttf/64b7f213ddd72695d94866a1a9532ee5b3a472a8
/usr/share/package-licenses/SDL2_ttf/9e9cec973c9a001fecefdf76e6160ce1899eae11
/usr/share/package-licenses/SDL2_ttf/b83c637448b14da11c48c8b3bcd811adf1fa91a7
/usr/share/package-licenses/SDL2_ttf/dac7127c82749e3107b53530289e1cd548860868
