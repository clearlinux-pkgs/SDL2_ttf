#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL2_ttf
Version  : 2.0.15
Release  : 16
URL      : https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.tar.gz
Source99 : https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.tar.gz.sig
Summary  : A library that allows you to use TrueType fonts in your SDL applications (Version 2)
Group    : Development/Tools
License  : FTL GPL-2.0 LGPL-2.1 Zlib
Requires: SDL2_ttf-lib = %{version}-%{release}
Requires: SDL2_ttf-license = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : SDL2-dev32
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : freetype-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32freetype2)
BuildRequires : pkgconfig(32gl)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(ice)
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


%package dev32
Summary: dev32 components for the SDL2_ttf package.
Group: Default
Requires: SDL2_ttf-lib32 = %{version}-%{release}
Requires: SDL2_ttf-dev = %{version}-%{release}

%description dev32
dev32 components for the SDL2_ttf package.


%package lib
Summary: lib components for the SDL2_ttf package.
Group: Libraries
Requires: SDL2_ttf-license = %{version}-%{release}

%description lib
lib components for the SDL2_ttf package.


%package lib32
Summary: lib32 components for the SDL2_ttf package.
Group: Default
Requires: SDL2_ttf-license = %{version}-%{release}

%description lib32
lib32 components for the SDL2_ttf package.


%package license
Summary: license components for the SDL2_ttf package.
Group: Default

%description license
license components for the SDL2_ttf package.


%prep
%setup -q -n SDL2_ttf-2.0.15
pushd ..
cp -a SDL2_ttf-2.0.15 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557076304
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1557076304
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL2_ttf
cp COPYING.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/COPYING.txt
cp VisualC/external/lib/x64/LICENSE.freetype.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/VisualC_external_lib_x64_LICENSE.freetype.txt
cp VisualC/external/lib/x64/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/VisualC_external_lib_x64_LICENSE.zlib.txt
cp VisualC/external/lib/x86/LICENSE.freetype.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/VisualC_external_lib_x86_LICENSE.freetype.txt
cp VisualC/external/lib/x86/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/VisualC_external_lib_x86_LICENSE.zlib.txt
cp Xcode/Frameworks/FreeType.framework/Versions/A/Resources/LICENSE.freetype.txt %{buildroot}/usr/share/package-licenses/SDL2_ttf/Xcode_Frameworks_FreeType.framework_Versions_A_Resources_LICENSE.freetype.txt
cp debian/copyright %{buildroot}/usr/share/package-licenses/SDL2_ttf/debian_copyright
cp external/freetype-2.9.1/docs/GPLv2.TXT %{buildroot}/usr/share/package-licenses/SDL2_ttf/external_freetype-2.9.1_docs_GPLv2.TXT
cp external/freetype-2.9.1/docs/LICENSE.TXT %{buildroot}/usr/share/package-licenses/SDL2_ttf/external_freetype-2.9.1_docs_LICENSE.TXT
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL_ttf.h
/usr/lib64/libSDL2_ttf.so
/usr/lib64/pkgconfig/SDL2_ttf.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libSDL2_ttf.so
/usr/lib32/pkgconfig/32SDL2_ttf.pc
/usr/lib32/pkgconfig/SDL2_ttf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2_ttf-2.0.so.0
/usr/lib64/libSDL2_ttf-2.0.so.0.14.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libSDL2_ttf-2.0.so.0
/usr/lib32/libSDL2_ttf-2.0.so.0.14.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL2_ttf/COPYING.txt
/usr/share/package-licenses/SDL2_ttf/VisualC_external_lib_x64_LICENSE.freetype.txt
/usr/share/package-licenses/SDL2_ttf/VisualC_external_lib_x64_LICENSE.zlib.txt
/usr/share/package-licenses/SDL2_ttf/VisualC_external_lib_x86_LICENSE.freetype.txt
/usr/share/package-licenses/SDL2_ttf/VisualC_external_lib_x86_LICENSE.zlib.txt
/usr/share/package-licenses/SDL2_ttf/Xcode_Frameworks_FreeType.framework_Versions_A_Resources_LICENSE.freetype.txt
/usr/share/package-licenses/SDL2_ttf/debian_copyright
/usr/share/package-licenses/SDL2_ttf/external_freetype-2.9.1_docs_GPLv2.TXT
/usr/share/package-licenses/SDL2_ttf/external_freetype-2.9.1_docs_LICENSE.TXT
