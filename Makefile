SUBDIRS := odevice otapi ophone ousage opreferences

.PHONY: all xml clean check

all:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) all) || exit 1 ; done

xml:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) xml) || exit 1 ; done

clean:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) clean) || exit 1 ; done

check:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) check) || exit 1 ; done

