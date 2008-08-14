SUBDIRS := odevice otapi ousage opreferences

all:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE)) || exit 1 ; done

xml:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE)) || exit 1 ; done

clean:
	@for i in $(SUBDIRS); do (cd $$i && $(MAKE) clean) || exit 1 ; done
