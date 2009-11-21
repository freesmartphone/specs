SUBDIRS := \
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
  org.freesmartphone.Time \
  org.freesmartphone.MusicPlayer

.PHONY: all clean check docs xml

all:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) all docs xml) || exit 1 ; done

clean:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) clean) || exit 1 ; done

check:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) check) || exit 1 ; done

docs:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) docs) || exit 1 ; done

xml:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) xml) || exit 1 ; done
    
