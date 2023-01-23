%global forgeurl https://github.com/eclipse-ecal/fineftp-server
%global tag v1.3.3

%forgemeta -i

Name:    fineftp-server
Version: 1.3.3
Release: 2%{?dist}
Summary: FineFTP is a minimal FTP server library for Windows and Unix flavors.
URL:     %{forgeurl}
Source:  %{forgesource}
License: BSD-3-Clause

BuildRequires: g++
BuildRequires: cmake
BuildRequires: asio-devel

%description
FineFTP is a minimal FTP server library for Windows and Unix flavors. The project is CMake based and only depends on asio, which is integrated as git submodule. No boost is required.

You can easily embed this library into your own project in order to create an embedded FTP Server. It was developed and tested on Windows 10 (Visual Studio 2015 / 2019, MinGW) and Ubuntu 16.04 - 21.10 (gcc 5.4.0 - 11.2.0).

%package devel
Summary: FineFTP development header and cmake files
Requires: %{name}-libs

%description devel
FineFTP development header and cmake files

%package libs
Summary: FineFTP library files

%description libs
FineFTP library files

%prep
%forgesetup

%build
%cmake -D asio_INCLUDE_DIR=%{_includedir}/asio -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files devel
%{_includedir}/fineftp/fineftp_export.h
%{_includedir}/fineftp/fineftp_version.h
%{_includedir}/fineftp/permissions.h
%{_includedir}/fineftp/server.h
%{_prefix}/lib/cmake/fineftp/fineftpConfig.cmake
%{_prefix}/lib/cmake/fineftp/fineftpTargets.cmake
%{_prefix}/lib/cmake/fineftp/fineftpTargets-release.cmake

%files libs 
%{_prefix}/lib/libfineftp-server.so.1.3.3
%{_prefix}/lib/libfineftp-server.so.1
%{_prefix}/lib/libfineftp-server.so

%files
%license LICENSE
%doc README.md

%changelog
* Mon Jan 23 2023 Leonardo Rossetti <lrossett@redhat.com> - 1.3.3-2
- Adding dependency for devel sub-package

* Sat Jan 21 2023 Leonardo Rossetti <lrossett@redhat.com> - 1.3.3-1
- First version being packaged
