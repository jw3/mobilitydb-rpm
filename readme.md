MobilityDB rpm builds
===

## build

...

## install

```bash
dnf install epel-release
crb enable
dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
dnf -qy module disable postgresql
dnf install -y mobilitydb-1.1.0~rc1-1.el8.x86_64.rpm
```

## test

```bash
sudo service postgresql start
sudo -u postgres createdb _test_
sudo -u postgres psql -d _test_ -c "CREATE EXTENSION mobilitydb CASCADE; SELECT mobilitydb_version()"
```

```text
bash-4.4$ createdb  _test_  
bash-4.4$ psql -d _test_ -c "CREATE EXTENSION mobilitydb CASCADE; SELECT mobilitydb_version()"
NOTICE:  installing required extension "postgis"
CREATE EXTENSION
 mobilitydb_version 
--------------------
 MobilityDB 1.1.0
(1 row)
```

## postgresql yum repo

see full instructions at https://www.postgresql.org/download/linux/redhat/


## dep list

```text
CGAL-4.14-1.rhel8.x86_64                                                                                             
SFCGAL-1.4.1-13.rhel8.x86_64                                                                                         
SFCGAL-libs-1.4.1-13.rhel8.x86_64                                                                                    
SuperLU-5.2.0-7.el8.x86_64                                                                                           
armadillo-12.6.6-1.el8.x86_64                                                                                        
arpack-3.7.0-1.el8.x86_64                                                                                            
atlas-3.10.3-8.el8.1.x86_64                                                                                          
avahi-libs-0.7-21.el8_9.1.x86_64                                                                                     
blas-3.8.0-8.el8.x86_64                                                                                              
boost-atomic-1.66.0-13.el8.x86_64                                                                                    
boost-chrono-1.66.0-13.el8.x86_64                                                                                    
boost-date-time-1.66.0-13.el8.x86_64                                                                                 
boost-serialization-1.66.0-13.el8.x86_64                                                                             
boost-system-1.66.0-13.el8.x86_64                                                                                    
boost-thread-1.66.0-13.el8.x86_64                                                                                    
cfitsio-3.47-1.el8.x86_64                                                                                            
cmake-filesystem-3.26.5-1.el8_9.x86_64                                                                               
cpio-2.12-11.el8.x86_64                                                                                              
crypto-policies-scripts-20230731-1.git3177e06.el8.noarch                                                             
cups-libs-1:2.2.6-54.el8_9.x86_64                                                                                    
dejavu-fonts-common-2.35-7.el8.noarch                                                                                
dejavu-sans-fonts-2.35-7.el8.noarch                                                                                  
dracut-049-228.git20230802.el8.x86_64                                                                                
file-5.33-25.el8.x86_64                                                                                              
findutils-1:4.6.0-21.el8.x86_64                                                                                      
fontconfig-2.13.1-4.el8.x86_64                                                                                       
fontpackages-filesystem-1.44-22.el8.noarch                                                                           
freetype-2.9.1-9.el8.x86_64                                                                                          
freexl-1.0.6-4.el8.x86_64                                                                                            
gdal36-libs-3.6.4-6PGDG.rhel8.x86_64                                                                                 
geos312-3.12.1-1PGDG.rhel8.x86_64                                                                                    
gettext-0.19.8.1-17.el8.x86_64                                                                                       
gettext-libs-0.19.8.1-17.el8.x86_64                                                                                  
giflib-5.1.4-3.el8.x86_64                                                                                            
glx-utils-8.4.0-5.20181118git1830dcb.el8.x86_64                                                                      
gmp-c++-1:6.1.2-10.el8.x86_64                                                                                        
gpsbabel-1.6.0-3.el8.x86_64                                                                                          
graphite2-1.3.10-10.el8.x86_64                                                                                       
groff-base-1.22.3-18.el8.x86_64                                                                                      
grub2-common-1:2.02-150.el8.rocky.0.1.noarch                                                                         
grub2-tools-1:2.02-150.el8.rocky.0.1.x86_64                                                                          
grub2-tools-minimal-1:2.02-150.el8.rocky.0.1.x86_64                                                                  
grubby-8.40-48.el8.x86_64                                                                                            
gsl-2.5-1.el8.x86_64                                                                                                 
hardlink-1:1.3-6.el8.x86_64                                                                                          
harfbuzz-1.7.5-3.el8.x86_64                                                                                          
hdf-4.2.14-5.el8.x86_64                                                                                              
hdf5-1.10.5-4.el8.x86_64                                                                                             
hwdata-0.314-8.19.el8.noarch                                                                                         
jbigkit-libs-2.1-14.el8.x86_64                                                                                       
kbd-2.0.4-11.el8.x86_64                                                                                              
kbd-legacy-2.0.4-11.el8.noarch                                                                                       
kbd-misc-2.0.4-11.el8.noarch                                                                                         
kmod-25-19.el8.x86_64                                                                                                
kpartx-0.8.4-39.el8.x86_64                                                                                           
lapack-3.8.0-8.el8.x86_64                                                                                            
lcms2-2.9-2.el8.x86_64                                                                                               
libICE-1.0.9-15.el8.x86_64                                                                                           
libSM-1.2.3-1.el8.x86_64                                                                                             
libX11-1.6.8-6.el8.x86_64                                                                                            
libX11-common-1.6.8-6.el8.noarch                                                                                     
libX11-xcb-1.6.8-6.el8.x86_64                                                                                        
libXau-1.0.9-3.el8.x86_64                                                                                            
libXext-1.3.4-1.el8.x86_64                                                                                           
libXfixes-5.0.3-7.el8.x86_64                                                                                         
libXxf86vm-1.1.4-9.el8.x86_64                                                                                        
libaec-1.0.2-3.el8.x86_64                                                                                            
libbsd-0.11.7-2.el8.x86_64                                                                                           
libcroco-0.6.12-4.el8_2.1.x86_64                                                                                     
libdrm-2.4.115-2.el8.x86_64                                                                                          
libevdev-1.10.0-1.el8.x86_64                                                                                         
libgeotiff17-1.7.1-3PGDG.rhel8.x86_64                                                                                
libgeotiff17-devel-1.7.1-3PGDG.rhel8.x86_64                                                                          
libgfortran-8.5.0-20.el8.x86_64                                                                                      
libglvnd-1:1.3.4-1.el8.x86_64                                                                                        
libglvnd-egl-1:1.3.4-1.el8.x86_64                                                                                    
libglvnd-glx-1:1.3.4-1.el8.x86_64                                                                                    
libgomp-8.5.0-20.el8.x86_64                                                                                          
libgta-1.2.1-1.el8.x86_64                                                                                            
libgudev-232-4.el8.x86_64                                                                                            
libicu-60.3-2.el8_1.x86_64                                                                                           
libinput-1.16.3-3.el8_6.x86_64                                                                                       
libjpeg-turbo-1.5.3-12.el8.x86_64                                                                                    
libkcapi-1.2.0-2.el8.x86_64                                                                                          
libkcapi-hmaccalc-1.2.0-2.el8.x86_64                                                                                 
libkml-1.3.0-24.el8.x86_64                                                                                           
libmd-1.1.0-1.el8.x86_64                                                                                             
libpciaccess-0.14-1.el8.x86_64                                                                                       
libpkgconf-1.4.2-1.el8.x86_64                                                                                        
libpng-2:1.6.34-5.el8.x86_64                                                                                         
libqhull_r-2015.2-5.el8.x86_64                                                                                       
libquadmath-8.5.0-20.el8.x86_64                                                                                      
librttopo-1.1.0-2.rhel8.x86_64                                                                                       
libspatialite50-5.1.0-2PGDG.rhel8.x86_64                                                                             
libspatialite50-devel-5.1.0-2PGDG.rhel8.x86_64                                                                       
libtiff-4.0.9-29.el8_8.x86_64                                                                                        
libtiff-devel-4.0.9-29.el8_8.x86_64                                                                                  
libtool-ltdl-2.4.6-25.el8.x86_64                                                                                     
libusb-1:0.1.5-12.el8.x86_64                                                                                         
libwacom-1.6-3.el8.x86_64                                                                                            
libwacom-data-1.6-3.el8.noarch                                                                                       
libwayland-client-1.21.0-1.el8.x86_64                                                                                
libwayland-server-1.21.0-1.el8.x86_64                                                                                
libwebp-1.0.0-9.el8_9.1.x86_64                                                                                       
libxcb-1.13.1-1.el8.x86_64                                                                                           
libxkbcommon-0.9.1-1.el8.x86_64                                                                                      
libxkbcommon-x11-0.9.1-1.el8.x86_64                                                                                  
libxshmfence-1.3-2.el8.x86_64                                                                                        
libxslt-1.1.32-6.el8.x86_64                                                                                          
lz4-1.8.3-3.el8_4.x86_64                                                                                             
mariadb-connector-c-3.1.11-2.el8_3.x86_64                                                                            
mariadb-connector-c-config-3.1.11-2.el8_3.noarch                                                                     
memstrack-0.2.5-2.el8.x86_64                                                                                         
mesa-libEGL-23.1.4-1.el8.x86_64                                                                                      
mesa-libGL-23.1.4-1.el8.x86_64                                                                                       
mesa-libgbm-23.1.4-1.el8.x86_64                                                                                      
mesa-libglapi-23.1.4-1.el8.x86_64                                                                                    
minizip-2.8.9-2.el8.x86_64                                                                                           
mobilitydb-1.1.0~rc1-1.el8.x86_64                                                                                    
mtdev-1.1.5-12.el8.x86_64                                                                                            
ncurses-6.1-10.20180224.el8.x86_64                                                                                   
netcdf-4.7.0-3.el8.x86_64                                                                                            
nspr-4.35.0-1.el8_8.x86_64                                                                                           
nss-3.90.0-6.el8_9.x86_64                                                                                            
nss-softokn-3.90.0-6.el8_9.x86_64                                                                                    
nss-softokn-freebl-3.90.0-6.el8_9.x86_64                                                                             
nss-sysinit-3.90.0-6.el8_9.x86_64                                                                                    
nss-util-3.90.0-6.el8_9.x86_64                                                                                       
ogdi41-4.1.0-3.rhel8.x86_64                                                                                          
openblas-0.3.15-6.el8.x86_64                                                                                         
openblas-openmp-0.3.15-6.el8.x86_64                                                                                  
openblas-threads-0.3.15-6.el8.x86_64                                                                                 
openblas-threads64_-0.3.15-6.el8.x86_64                                                                              
openjpeg2-2.4.0-5.el8.x86_64                                                                                         
openssl-1:1.1.1k-9.el8_7.x86_64                                                                                      
os-prober-1.74-9.el8.x86_64                                                                                          
pcre2-utf16-10.32-3.el8_6.x86_64                                                                                     
perl-Carp-1.42-396.el8.noarch                                                                                        
perl-Data-Dumper-2.167-399.el8.x86_64                                                                                
perl-Digest-1.17-395.el8.noarch                                                                                      
perl-Digest-MD5-2.55-396.el8.x86_64                                                                                  
perl-Encode-4:2.97-3.el8.x86_64                                                                                      
perl-Errno-1.28-422.el8.x86_64                                                                                       
perl-Exporter-5.72-396.el8.noarch                                                                                    
perl-File-Path-2.15-2.el8.noarch                                                                                     
perl-File-Temp-0.230.600-1.el8.noarch                                                                                
perl-Getopt-Long-1:2.50-4.el8.noarch                                                                                 
perl-HTTP-Tiny-0.074-2.el8.noarch                                                                                    
perl-IO-1.38-422.el8.x86_64                                                                                          
perl-IO-Socket-IP-0.39-5.el8.noarch                                                                                  
perl-IO-Socket-SSL-2.066-4.module+el8.9.0+1517+e71a7a62.noarch                                                       
perl-MIME-Base64-3.15-396.el8.x86_64                                                                                 
perl-Mozilla-CA-20160104-7.module+el8.9.0+1521+0101edce.noarch                                                       
perl-Net-SSLeay-1.88-2.module+el8.9.0+1517+e71a7a62.x86_64                                                           
perl-PathTools-3.74-1.el8.x86_64                                                                                     
perl-Pod-Escapes-1:1.07-395.el8.noarch                                                                               
perl-Pod-Perldoc-3.28-396.el8.noarch                                                                                 
perl-Pod-Simple-1:3.35-395.el8.noarch                                                                                
perl-Pod-Usage-4:1.69-395.el8.noarch                                                                                 
perl-Scalar-List-Utils-3:1.49-2.el8.x86_64                                                                           
perl-Socket-4:2.027-3.el8.x86_64                                                                                     
perl-Storable-1:3.11-3.el8.x86_64                                                                                    
perl-Term-ANSIColor-4.06-396.el8.noarch                                                                              
perl-Term-Cap-1.17-395.el8.noarch                                                                                    
perl-Text-ParseWords-3.30-395.el8.noarch                                                                             
perl-Text-Tabs+Wrap-2013.0523-395.el8.noarch                                                                         
perl-Time-Local-1:1.280-1.el8.noarch                                                                                 
perl-URI-1.73-3.el8.noarch                                                                                           
perl-Unicode-Normalize-1.25-396.el8.x86_64                                                                           
perl-constant-1.33-396.el8.noarch                                                                                    
perl-interpreter-4:5.26.3-422.el8.x86_64                                                                             
perl-libnet-3.11-3.el8.noarch                                                                                        
perl-libs-4:5.26.3-422.el8.x86_64                                                                                    
perl-macros-4:5.26.3-422.el8.x86_64                                                                                  
perl-parent-1:0.237-1.el8.noarch                                                                                     
perl-podlators-4.11-1.el8.noarch                                                                                     
perl-threads-1:2.21-2.el8.x86_64                                                                                     
perl-threads-shared-1.58-2.el8.x86_64                                                                                
pigz-2.4-4.el8.x86_64                                                                                                
pkgconf-1.4.2-1.el8.x86_64                                                                                           
pkgconf-m4-1.4.2-1.el8.noarch                                                                                        
pkgconf-pkg-config-1.4.2-1.el8.x86_64                                                                                
poppler-20.11.0-10.el8.x86_64                                                                                        
poppler-data-0.4.9-1.el8.noarch                                                                                      
postgis33_15-3.3.5-1PGDG.rhel8.x86_64                                                                                
postgresql15-15.6-1PGDG.rhel8.x86_64                                                                                 
postgresql15-contrib-15.6-1PGDG.rhel8.x86_64                                                                         
postgresql15-libs-15.6-1PGDG.rhel8.x86_64                                                                            
postgresql15-server-15.6-1PGDG.rhel8.x86_64                                                                          
procps-ng-3.3.15-14.el8.x86_64                                                                                       
proj-6.3.2-4.el8.x86_64                                                                                              
proj-datumgrid-1.8-6.3.2.4.el8.noarch                                                                                
proj92-9.2.1-1PGDG.rhel8.x86_64                                                                                      
protobuf-c-1.3.0-8.el8.x86_64                                                                                        
qt5-qtbase-5.15.3-5.el8.x86_64                                                                                       
qt5-qtbase-common-5.15.3-5.el8.noarch                                                                                
qt5-qtbase-gui-5.15.3-5.el8.x86_64                                                                                   
qt5-qtsvg-5.15.3-2.el8.x86_64                                                                                        
shapelib-1.5.0-12.el8.x86_64                                                                                         
systemd-udev-239-78.el8.x86_64                                                                                       
unixODBC-2.3.7-1.el8.x86_64                                                                                          
uriparser-0.9.7-1.el8.x86_64                                                                                         
which-2.21-20.el8.x86_64                                                                                             
xcb-util-0.4.0-10.el8.x86_64                                                                                         
xcb-util-image-0.4.0-9.el8.x86_64                                                                                    
xcb-util-keysyms-0.4.0-7.el8.x86_64                                                                                  
xcb-util-renderutil-0.3.9-10.el8.x86_64                                                                              
xcb-util-wm-0.4.1-12.el8.x86_64                                                                                      
xerces-c-3.2.5-1.el8.x86_64                                                                                          
xkeyboard-config-2.28-1.el8.noarch                                                                                   
xz-5.2.4-4.el8_6.x86_64
```
