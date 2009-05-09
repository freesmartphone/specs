SUBDIRS := \
  org.freesmartphone \
  org.freesmartphone.Device \
  org.freesmartphone.Phone \
  org.freesmartphone.Usage \
  org.freesmartphone.Events \
  org.freesmartphone.PIM \
  org.freedesktop.Gypsy \
  org.freesmartphone.GSM \
  org.freesmartphone.Preferences \
  org.freesmartphone.Network \
  org.freesmartphone.Time

.PHONY: all clean check

all:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) all docs xml) || exit 1 ; done

clean:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) clean) || exit 1 ; done

check:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) check) || exit 1 ; done

docs:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) docs) || exit 1 ; done

