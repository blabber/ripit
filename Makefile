VERSION = 3.9.0
RELEASE = 0
INSTALL = /usr/bin/install -c

# Installation directories
prefix = $(DESTDIR)/usr/local
exec_prefix = ${prefix}
mandir = ${prefix}/share/man/man1
bindir = ${exec_prefix}/bin
etcdir = ${prefix}/../../etc/ripit

all:

clean:

install:
	$(INSTALL) -d -m 755 $(bindir)
	$(INSTALL) -m 755 ripit.pl $(bindir)/ripit
	$(INSTALL) -d -m 755 $(mandir)
	$(INSTALL) -m 644 ripit.1 $(mandir)
	$(INSTALL) -d -m 755 $(etcdir)
	$(INSTALL) -b -m 644 config $(etcdir)

tarball:
	@cd .. && tar cvvfz ripit-$(VERSION).tar.gz ripit-$(VERSION)
	@cd .. && md5sum ripit-$(VERSION).tar.gz > ripit-$(VERSION).tar.gz.md5
	@cd .. && tar cvvfj ripit-$(VERSION).tar.bz2 ripit-$(VERSION)
	@cd .. && md5sum ripit-$(VERSION).tar.bz2 > ripit-$(VERSION).tar.bz2.md5

rpm:    tarball
	@cd .. && cp ripit-$(VERSION).tar.* /usr/src/packages/SOURCES/
	rpmbuild -ba --sign ripit.spec
	@mv /usr/src/packages/SRPMS/ripit-$(VERSION)-$(RELEASE).src.rpm \
	    /usr/src/packages/RPMS/noarch/ripit-$(VERSION)-$(RELEASE).noarch.rpm ..

myrpm:	tarball
	rpmbuild --sign -ta ../ripit-$(VERSION).tar.gz
