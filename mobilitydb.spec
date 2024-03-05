Summary:    An open source geospatial trajectory data management & analysis platform.
Name:       mobilitydb
Version:    1.1.0~rc2
Release:    1%{?dist}
License:    PostgreSQL
URL:        https://github.com/MobilityDB/MobilityDB
Source0:    %{url}/archive/refs/tags/v1.1.0rc2.zip

BuildRequires: clang
BuildRequires: cmake
BuildRequires: gsl-devel
BuildRequires: geos-devel
BuildRequires: proj-devel
BuildRequires: json-c-devel
BuildRequires: postgresql16-devel
BuildRequires: postgis34_16-devel

Requires: postgresql16-server
Requires: postgis34_16

%description
MobilityDB provides the necessary database support for
storing and querying geospatial trajectory data.
Built on Postgres v16 and PostGIS 3.4

%prep
%setup -q -n MobilityDB-1.1.0rc2

%build
%set_build_flags

mkdir build && cd build || exit 1
%cmake -DCMAKE_BUILD_TYPE=Release ..
%cmake_build


%install
cd build
%cmake_install

%files -n %{name}
%{_exec_prefix}/pgsql-16/lib/libMobilityDB-1.1.so
%{_exec_prefix}/pgsql-16/share/extension/mobilitydb--1.1.0.sql
%{_exec_prefix}/pgsql-16/share/extension/mobilitydb.control

%changelog
* Tue Mar 05 2024 John Wass <wassj@ctc.com> 1.1.0~rc2-1
- New release

* Tue Feb 13 2024 John Wass <wassj@ctc.com> 1.1.0~rc1-1
- New release
