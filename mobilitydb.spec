Summary:    An open source geospatial trajectory data management & analysis platform.
Name:       mobilitydb
Version:    1.1.0~rc1
Release:    1%{?dist}
License:    PostgreSQL
URL:        https://github.com/MobilityDB/MobilityDB
Source0:    %{url}/archive/refs/tags/v1.1.0rc1.zip

BuildRequires: clang
BuildRequires: cmake
BuildRequires: geos-devel
BuildRequires: proj-devel
BuildRequires: json-c-devel

%description
MobilityDB provides the necessary database support for storing and
querying geospatial trajectory data.

%prep
%autosetup -n %{name}
mkdir build

%build
cd build || exit
cmake ..
make

%install
make install

%files -n %{name}

