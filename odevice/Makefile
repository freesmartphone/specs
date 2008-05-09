XMLLINT_FLAGS =
XMLLINT = xmllint $(XMLLINT_FLAGS)

XSLT_FLAGS = -o $@ ../tools/spec-strip-docs.xsl $<
XSLT = xsltproc $(XSLT_FLAGS)

files = \
  org.freesmartphone.Device.Display.xml \
  org.freesmartphone.Device.IdleNotifier.xml \
  org.freesmartphone.Device.PowerSupply.xml

docbook_xml_files = $(addprefix docbook-, $(files))
docbook_xhtml_files = $(addprefix xhtml/, $(docbook_xml_files:.xml=.xhtml))

# choose your style sheet
docbook_style_sheet = /usr/share/sgml/docbook/xsl-stylesheets-1.73.2/xhtml/docbook.xsl
#docbook_style_sheet = /usr/share/xml/docbook/stylesheet/nwalsh/xhtml/docbook.xsl

all: $(files) docs

check:
	@echo checking integrity...
	@xmllint *.xml.in >/dev/null && echo "OK" || echo "FAIL"

doc-dirs:
	@mkdir -p xhtml

docs: doc-dirs $(docbook_xhtml_files)

$(docbook_xhtml_files): xhtml/%.xhtml: %.xml
	@echo processing $@ ...
	@xsltproc -o $@ $(docbook_style_sheet) $<

$(docbook_xml_files): docbook-%.xml: %.xml.in
	@echo processing $@ ...
	@xsltproc -o $@ ../tools/spec-to-docbook.xsl $<

$(files): %.xml: %.xml.in
	@echo processing $@ ...
	@xsltproc -o $@ ../tools/spec-strip-docs.xsl $<

clean:
	@rm -f $(files) *~
	@rm -f docbook-org.freesmartphone.*.xml
	@rm -rf xhtml
