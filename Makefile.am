SUBDIRS = \
  org.freesmartphone \
  org.freesmartphone.Data \
  org.freesmartphone.Device \
  org.freesmartphone.Phone \
  org.freesmartphone.Usage \
  org.freesmartphone.Events \
  org.freesmartphone.PIM \
  org.freedesktop.Gypsy \
  org.freesmartphone.GSM \
  org.freesmartphone.Preferences \
  org.freesmartphone.Network \
  org.freesmartphone.Notification \
  org.freesmartphone.Time \
  org.freesmartphone.MusicPlayer

EXTRA_DIST = fso-specs.pc.in

pkgconfigdir = $(datadir)/pkgconfig
dist_pkgconfig_DATA = fso-specs.pc

install-data-local:
	$(INSTALL) -d $(DESTDIR)/$(datadir)/freesmartphone/xml
	for i in xml/*.xml; do $(INSTALL) -m 0644 $$i $(DESTDIR)/$(datadir)/freesmartphone/$$i; done
