SUBDIRS := odevice otapi ophone ousage opreferences

.PHONY: all clean check

all:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) all xml) || exit 1 ; done

clean:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) clean) || exit 1 ; done

check:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) check) || exit 1 ; done

