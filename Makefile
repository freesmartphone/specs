SUBDIRS := odevice otapi ophone ousage opreferences oevents

.PHONY: all clean check

all:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) all docs xml) || exit 1 ; done

clean:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) clean) || exit 1 ; done

check:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) check) || exit 1 ; done

docs:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) docs) || exit 1 ; done

