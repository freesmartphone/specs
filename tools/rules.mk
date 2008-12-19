XMLLINT_FLAGS =
XMLLINT = xmllint $(XMLLINT_FLAGS)

XSLT_FLAGS = -o $@ ../tools/spec-strip-docs.xsl $<
XSLT = xsltproc $(XSLT_FLAGS)

docbook_xml_files = $(addprefix docbook-, $(files))
docbook_xhtml_files = $(addprefix xhtml/, $(docbook_xml_files:.xml=.xhtml))
pydoc_html_files = $(files:.xml=.html)

# choose your style sheet
docbook_style_sheet = /usr/share/sgml/docbook/xsl-stylesheets/xhtml/docbook.xsl
#docbook_style_sheet = /usr/share/xml/docbook/stylesheet/nwalsh/xhtml/docbook.xsl

all: pydocs

xml: $(files)

check:
	@echo checking integrity...
	@xmllint *.xml.in >/dev/null && echo "OK" || echo "FAIL"

doc-dirs:
	@mkdir -p xhtml

docs: doc-dirs $(docbook_xhtml_files)

pydocs: $(pydoc_html_files)

$(pydoc_html_files): %.html: %.xml.in
	@echo processing $@
	../tools/makedoc.py $< >/dev/null

$(docbook_xhtml_files): xhtml/%.xhtml: %.xml
	@echo processing $@ ...
	@xsltproc -o $@ $(docbook_style_sheet) $<

$(docbook_xml_files): docbook-%.xml: %.xml.in
	@echo processing $@ ...
	@xsltproc -o $@ ../tools/spec-to-docbook.xsl $<

$(files): %.xml: %.xml.in
	@echo processing $@ ...
	@xsltproc -o ../xml/$@ ../tools/spec-strip-docs.xsl $<

clean:
	@rm -f $(files) *~
	for i in $(pydoc_html_files); do rm -f ../html/$$i; done
	for i in $(files); do rm -f ../xml/$$i; done
	@rm -rf xhtml *.html
