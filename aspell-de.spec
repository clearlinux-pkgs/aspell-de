#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0x71C636695B147849 (dict-upload@aspell.net)
#
Name     : aspell-de
Version  : 20161207.7.0
Release  : 3
URL      : https://mirrors.kernel.org/gnu/aspell/dict/de/aspell6-de-20161207-7-0.tar.bz2
Source0  : https://mirrors.kernel.org/gnu/aspell/dict/de/aspell6-de-20161207-7-0.tar.bz2
Source1  : https://mirrors.kernel.org/gnu/aspell/dict/de/aspell6-de-20161207-7-0.tar.bz2.sig
Source2  : 71C636695B147849.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: aspell-de-license = %{version}-%{release}
BuildRequires : aspell-dev
BuildRequires : buildreq-configure
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-configure-ignore-unknown-options.patch

%description
GNU Aspell 0.60 German Dictionary Package
Version 20161207-7-0
2019-07-23
Maintained By:
Kevin Atkinson <kevina at gnu org>
Roland Rosenfeld <roland at debian org>
Wordlist URL: https://packages.debian.org/testing/aspell-de
Source URL: https://www.j3e.de/ispell/igerman98/

%package license
Summary: license components for the aspell-de package.
Group: Default

%description license
license components for the aspell-de package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 71C636695B147849' gpg.status
%setup -q -n aspell6-de-20161207-7-0
cd %{_builddir}/aspell6-de-20161207-7-0
%patch -P 1 -p1
pushd ..
cp -a aspell6-de-20161207-7-0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713221527
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
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1713221527
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aspell-de
cp %{_builddir}/aspell6-de-20161207-7-0/Copyright %{buildroot}/usr/share/package-licenses/aspell-de/5e720d0c14e06e22d41a5c235c2b22e0efc2b8c0 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/aspell-0.60/de-common.rws
/usr/lib64/aspell-0.60/de.dat
/usr/lib64/aspell-0.60/de.multi
/usr/lib64/aspell-0.60/de_AT-only.rws
/usr/lib64/aspell-0.60/de_AT.multi
/usr/lib64/aspell-0.60/de_CH-only.rws
/usr/lib64/aspell-0.60/de_CH.multi
/usr/lib64/aspell-0.60/de_DE-only.rws
/usr/lib64/aspell-0.60/de_DE.multi
/usr/lib64/aspell-0.60/de_affix.dat
/usr/lib64/aspell-0.60/de_phonet.dat
/usr/lib64/aspell-0.60/deutsch.alias
/usr/lib64/aspell-0.60/german.alias

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aspell-de/5e720d0c14e06e22d41a5c235c2b22e0efc2b8c0
