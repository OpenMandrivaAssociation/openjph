%define libname %mklibname openjph
%define devname %mklibname -d openjph

Name:           openjph
Version:        0.14.2
Release:        1
Summary:        Open-source implementation of JPEG2000 Part-15 (or JPH or HTJ2K)
License:        BSD-2-Clause
Group:          Productivity/Graphics/Libraries
URL:            https://github.com/aous72/OpenJPH
Source:         https://github.com/aous72/OpenJPH/archive/refs/tags/%{version}/OpenJPH-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(libtiff-4)

%description
Open source implementation of High-throughput JPEG2000 (HTJ2K), also known as JPH,
JPEG2000 Part 15, ISO/IEC 15444-15, and ITU-T T.814. Here, we are interested in
implementing the HTJ2K only, supporting features that are defined in JPEG2000 Part 1.
For example, for wavelet transform, only reversible 5/3 and irreversible 9/7 are supported.

%package -n %{libname}
Summary:        JPEG-2000 Parth-15 library
Group:          Productivity/Graphics/Convertors

%description -n %{libname}
This package contains libopenjph, a library implementing the JPEG-2000
standard Part 15.

%package -n %{devname}
Summary:        Development files for libopenjph, a JPEG-2000 library
Group:          Productivity/Graphics/Convertors
Requires:       pkgconfig(libjpeg)
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains libopenjph, a library implementing the JPEG-2000
standard Part 15.

%prep
%autosetup -n OpenJPH-%{version} -p1

%build
%cmake \
%ifarch %{aarch64}
        -DOJPH_DISABLE_INTEL_SIMD=ON \
        -DOJPH_ENABLE_INTEL_AVX512=OFF \
        -DCMAKE_BUILD_TYPE=Release
%else
        -DCMAKE_BUILD_TYPE=Release \
        -DOJPH_ENABLE_INTEL_AVX512=ON
%endif
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/ojph_compress
%{_bindir}/ojph_expand

%files -n %{libname}
%{_libdir}/libopenjph*.so.*

%files -n %{devname}
%{_includedir}/openjph/
%{_libdir}/libopenjph.so
%{_libdir}/pkgconfig/openjph.pc
