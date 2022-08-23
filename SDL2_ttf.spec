#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL2_ttf
Version  : 2.20.1
Release  : 21
URL      : https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.20.1.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.20.1.tar.gz
Source1  : https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.20.1.tar.gz.sig
Summary  : ttf library for Simple DirectMedia Layer with FreeType 2 support
Group    : Development/Tools
License  : FTL GPL-2.0 MIT Zlib
Requires: SDL2_ttf-lib = %{version}-%{release}
Requires: SDL2_ttf-license = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-ft)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(x11)

%description
This is HarfBuzz, a text shaping library.
For bug reports, mailing list, and other information please visit:

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
%setup -q -n SDL2_ttf-2.20.1
cd %{_builddir}/SDL2_ttf-2.20.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661296876
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1661296876
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL2_ttf
cp %{_builddir}/SDL2_ttf-%{version}/Xcode/iOS/SDL2.framework/License.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/56855624d497345923d749f17502a18029d72631
cp %{_builddir}/SDL2_ttf-%{version}/Xcode/macOS/SDL2.framework/Versions/A/Resources/License.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/56855624d497345923d749f17502a18029d72631
cp %{_builddir}/SDL2_ttf-%{version}/Xcode/pkg-support/resources/FreeType-LICENSE.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/64b7f213ddd72695d94866a1a9532ee5b3a472a8
cp %{_builddir}/SDL2_ttf-%{version}/Xcode/pkg-support/resources/HarfBuzz-LICENSE.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/18c194fb2b96b6a60289a79265e76976ffdb303d
cp %{_builddir}/SDL2_ttf-%{version}/Xcode/tvOS/SDL2.framework/License.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/56855624d497345923d749f17502a18029d72631
cp %{_builddir}/SDL2_ttf-%{version}/external/freetype/LICENSE.TXT %{buildroot}/usr/share/package-licenses/SDL2_ttf/4ddaa192f25581d05cb4d3219d57c1edc76167b7
cp %{_builddir}/SDL2_ttf-%{version}/external/freetype/docs/GPLv2.TXT %{buildroot}/usr/share/package-licenses/SDL2_ttf/dac7127c82749e3107b53530289e1cd548860868
cp %{_builddir}/SDL2_ttf-%{version}/external/harfbuzz/COPYING %{buildroot}/usr/share/package-licenses/SDL2_ttf/07f9ad4e387c060c0032e3d02e9ac287ea720785
cp %{_builddir}/SDL2_ttf-%{version}/external/harfbuzz/src/ms-use/COPYING %{buildroot}/usr/share/package-licenses/SDL2_ttf/689ec0681815ecc32bee639c68e7740add7bd301
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL_ttf.h
/usr/lib64/cmake/SDL2_ttf/sdl2_ttf-config-version.cmake
/usr/lib64/cmake/SDL2_ttf/sdl2_ttf-config.cmake
/usr/lib64/libSDL2_ttf.so
/usr/lib64/pkgconfig/SDL2_ttf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2_ttf-2.0.so.0
/usr/lib64/libSDL2_ttf-2.0.so.0.2000.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL2_ttf/07f9ad4e387c060c0032e3d02e9ac287ea720785
/usr/share/package-licenses/SDL2_ttf/18c194fb2b96b6a60289a79265e76976ffdb303d
/usr/share/package-licenses/SDL2_ttf/4ddaa192f25581d05cb4d3219d57c1edc76167b7
/usr/share/package-licenses/SDL2_ttf/56855624d497345923d749f17502a18029d72631
/usr/share/package-licenses/SDL2_ttf/64b7f213ddd72695d94866a1a9532ee5b3a472a8
/usr/share/package-licenses/SDL2_ttf/689ec0681815ecc32bee639c68e7740add7bd301
/usr/share/package-licenses/SDL2_ttf/dac7127c82749e3107b53530289e1cd548860868
