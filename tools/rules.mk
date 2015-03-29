XMLLINT_FLAGS =
XMLLINT = xmllint $(XMLLINT_FLAGS)

XSLT_FLAGS = -o $@ ../tools/spec-strip-docs.xsl $<
XSLT = xsltproc $(XSLT_FLAGS)

docbook_xml_files = $(addprefix docbook-, $(files))

all: xml

xml: $(files)

$(files): %.xml: %.xml.in
	@echo calling xsltproc spec-strip-docs on $@ ...
	@xsltproc -o ../xml/$@ ../tools/spec-strip-docs.xsl $<

install: xml
	@echo nothing to install here

check:
	@echo checking integrity...
	@xmllint *.xml.in >/dev/null && echo "OK" || echo "FAIL"

clean:
	@rm -f $(files) *~
	for i in $(pydoc_html_files); do rm -f ../html/$$i; done
	for i in $(files); do rm -f ../xml/$$i; done
	@rm -rf xhtml *.html

maintainer-clean: clean
	:

