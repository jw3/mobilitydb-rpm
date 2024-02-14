Summary:    An open source geospatial trajectory data management & analysis platform.
Name:       mobilitydb
Version:    1.0.0
Release:    1%{?dist}
License:    PostgreSQL
URL:        https://github.com/MobilityDB/MobilityDB
Source0:    %{url}/archive/refs/tags/v1.0.zip

BuildRequires: clang
BuildRequires: cmake
BuildRequires: gsl-devel
BuildRequires: geos-devel
BuildRequires: proj-devel
BuildRequires: json-c-devel
BuildRequires: postgresql14-devel
BuildRequires: postgis33_14-devel

Requires: postgresql14-server
Requires: postgis33_14

%description
MobilityDB provides the necessary database support for storing and
querying geospatial trajectory data.

%prep
%setup -q -n MobilityDB-1.0

%build
%set_build_flags

mkdir build && cd build || exit 1
%cmake -DCMAKE_BUILD_TYPE=Release ..
%cmake_build


%install
cd build
%cmake_install

%files -n %{name}
%{_exec_prefix}/pgsql-14/lib/libMobilityDB-1.0.so
%{_exec_prefix}/pgsql-14/share/extension/mobilitydb--1.0.0.sql
%{_exec_prefix}/pgsql-14/share/extension/mobilitydb.control

%changelog
* Tue Feb 13 2024 John Wass <wassj@ctc.com> 1.0.0-1
- New release
