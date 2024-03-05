FROM rockylinux:8 AS base

RUN dnf install -y epel-release
RUN crb enable

RUN dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
RUN dnf -qy module disable postgresql

# ----------------------

FROM base AS build

RUN dnf install -y rpmdevtools

RUN mkdir -p /root/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
WORKDIR /root/rpmbuild
COPY mobilitydb.spec SPECS
RUN spectool -g SPECS/mobilitydb.spec -C SOURCES
RUN dnf builddep -y SPECS/mobilitydb.spec

RUN ln -s /usr/pgsql-16/bin/pg_config /usr/bin
RUN rpmbuild -bb SPECS/mobilitydb.spec

# ----------------------

FROM base

COPY --from=build /root/rpmbuild/RPMS/x86_64/mobilitydb-1.1.0~rc2-1.el8.x86_64.rpm /tmp
RUN dnf install -y /tmp/mobilitydb-1.1.0~rc2-1.el8.x86_64.rpm
RUN dnf install -y nano

ENV PATH=$PATH:/usr/pgsql-16/bin
RUN su postgres -c 'initdb --pgdata=/var/lib/pgsql/15/data/ --username=postgres --pwfile=<(printf "%s\n" "Postgres")'

RUN echo "local all all trust" > /var/lib/pgsql/15/data/pg_hba.conf
RUN echo "host all all all md5" >> /var/lib/pgsql/15/data/pg_hba.conf

COPY postgresql.conf /var/lib/pgsql/16/data
    RUN echo "listen_addresses = '0.0.0.0'" >> /var/lib/pgsql/15/data/postgresql.conf

RUN systemctl enable postgresql-16

EXPOSE 5432

ENTRYPOINT [ "/usr/sbin/init" ]
