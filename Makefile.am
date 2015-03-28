SUBDIRS = \
  org.freesmartphone \
  org.freesmartphone.Data \
  org.freesmartphone.Device \
  org.freesmartphone.Context \
  org.freesmartphone.Events \
  org.freesmartphone.GSM \
  org.freesmartphone.Network \
  org.freesmartphone.Notification \
  org.freesmartphone.Phone \
  org.freesmartphone.PIM \
  org.freesmartphone.Preferences \
  org.freesmartphone.Time \
  org.freesmartphone.Usage \
  org.freesmartphone.Audio

EXTRA_DIST = fso-specs.pc.in

pkgconfigdir = $(datadir)/pkgconfig
dist_pkgconfig_DATA = fso-specs.pc

install-data-local:
	$(MAKE)
	$(INSTALL) -d $(DESTDIR)/$(datadir)/freesmartphone/xml
	for i in xml/*.xml; do $(INSTALL) -m 0644 $$i $(DESTDIR)/$(datadir)/freesmartphone/$$i; done
	find . -name "org*" -type d -exec $(INSTALL) -d $(DESTDIR)/$(datadir)/freesmartphone/doc/{} \;
	for i in */*.xml.in; do $(INSTALL) -m 0644 $$i $(DESTDIR)/$(datadir)/freesmartphone/doc/$$i; done

MAINTAINERCLEANFILES = \
  aclocal.m4 compile config.guess config.sub \
  configure depcomp install-sh ltmain.sh     \
  Makefile.in missing config.h.in            \
  mkinstalldirs \
  src/*.h src/*.c .deps xml/*.xml
