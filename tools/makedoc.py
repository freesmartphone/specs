#!/usr/bin/env python
# (C) 2008 Michael 'Mickey' Lauer <mlauer@vanille-media.de>
# GPLv2

import sys
from xml.sax import parse
from xml.sax.handler import ContentHandler

#----------------------------------------------------------------------------#
class Entity( object ):
#----------------------------------------------------------------------------#
    def __init__( self, name, attrs=None ):
        print "creating entity: ", self.__class__.__name__, name
        self.name = name
        self.attrs = attrs

    def output( self ):
        pass

    def out( self ):
        return ""

    def outputSectionHeader( self, content, size=1 ):
        return "<h%s>%s</h%s>" % ( size, content, size )

    def outputParagraph( self, content ):
        return "<p>%s</p>" % ( content )

    def outputTypewriter( self, content ):
        return "<tt>%s</tt>" % ( content )

    def outputAnchorLink( self, content ):
        return """<a href="#%s">%s</a>""" % ( content, content )

    def outputAnchorLabel( self, content ):
        return """<a name="%s">%s</a>""" % ( content, content )

    def outputList( self, entries ):

        if not len( entries ):
            return "<i>None</i>\n"

        else:
            t = "<ul>\n"
            for entry in entries:
                t += "<li>%s</li>\n" % entry
            t += "</ul>\n"
            return t

    def outputHeader( self ):
        return \
"""
<html>
    <head>
        <title>%s</title>
    </head>
    <body>
""" % self.title

    def outputFooter( self ):
        return \
"""
    </body>
</html>
"""

#----------------------------------------------------------------------------#
class Interface( Entity ):
#----------------------------------------------------------------------------#
    def __init__( self, filename ):
        self.filename = filename

        self.methods = []
        self.signals = []
        self.errors = []
        self.outfile = None

    def output( self ):
        self.outfilename = self.filename.replace( ".xml.in", ".html" )
        self.outfile = open( self.outfilename, "w" )

        text = self.outputHeader()
        text += "\n"

        text += self.outputSectionHeader( self.namespace )

        # description
        text += self.outputSectionHeader( "Description", 2 )
        text += "\n"
        text += self.outputParagraph( self.description )
        text += "\n"

        # namespace
        text += self.outputSectionHeader( "Namespace", 2 )
        text += "\n"
        text += self.outputParagraph( self.outputTypewriter( self.namespace ) )
        text += "\n"

        # method overview
        text += self.outputSectionHeader( "Methods", 2 )
        text += self.outputList( [ self.outputAnchorLink(method.name) for method in self.methods ] )

        # signal overview
        text += self.outputSectionHeader( "Signals", 2 )
        text += self.outputList( [ self.outputAnchorLink(method.name) for method in self.signals ] )

        # error overview
        text += self.outputSectionHeader( "Errors", 2 )
        text += self.outputList( [ self.outputAnchorLink(method.name) for method in self.errors ] )

        # methods en detail
        if len( self.methods ):
            text += self.outputSectionHeader( "Methods" )
            for m in self.methods:
                text += m.out()

        # signals en detail
        if len( self.signals ):
            text += self.outputSectionHeader( "Signals" )
            for s in self.signals:
                text += s.out()

        # errors en detail
        if len( self.errors ):
            text += self.outputSectionHeader( "Errors" )
            for e in self.errors:
                text += e.out()

        text += self.outputFooter()
        text += "\n"

        assert self.outfile is not None
        self.outfile.write( text )

#----------------------------------------------------------------------------#
class Method( Entity ):
#----------------------------------------------------------------------------#
    def __init__( self, name, attrs ):
        Entity.__init__( self, name, attrs )
        self.args = []

    def signature( self ):
        outparam = ""
        inparam = ""
        for arg in self.args:
            if arg.attrs["direction"] == "in":
                inparam += arg.attrs["type"]
            else:
                outparam += arg.attrs["type"]
        return inparam, outparam

    def out( self ):
        text = ""
        inparam, outparam = self.signature()
        if inparam and outparam:
            text += "%s ( %s ) &rarr; %s" % ( self.outputAnchorLabel( self.name ), inparam, outparam )
            text += "\n"
            text += self.inparam()
            text += self.outparam()
        elif inparam and not outparam:
            text += "%s ( %s )" % ( self.outputAnchorLabel( self.name ), inparam )
            text += "\n"
            text += self.inparam()
        elif not inparam and outparam:
            text += "%s ( ) &rarr; %s" % ( self.outputAnchorLabel( self.name ), outparam )
            text += "\n"
            text += self.outparam()
        else:
            text += "%s ( )" % ( self.outputAnchorLabel( self.name ), outparam )

        text = self.outputSectionHeader( text, 3 )
        text += "\n"

        return text

    def inparam( self ):
        text = self.outputSectionHeader( "Parameters", 4 )
        for arg in self.args:
            if arg.attrs["direction"] == "in":
                text += arg.out()
        return text

    def outparam( self ):
        text = self.outputSectionHeader( "Returns", 4 )
        for arg in self.args:
            if arg.attrs["direction"] == "out":
                text += arg.out()
        return text

#----------------------------------------------------------------------------#
class Signal( Entity ):
#----------------------------------------------------------------------------#
    def __init__( self, name, attrs ):
        Entity.__init__( self, name, attrs )
        self.args = []

    def signature( self ):
        param = ""
        for arg in self.args:
            param += arg.attrs["type"]
        return param

    def out( self ):
        text = ""
        param = self.signature()
        if param:
            text += "%s ( %s )" % ( self.outputAnchorLabel( self.name ), param )
            text += self.param()
        else:
            text += "%s ( )" % ( self.outputAnchorLabel( self.name ) )

        text = self.outputSectionHeader( text, 3 )
        text += "\n"

        return text

    def param( self ):
        text = self.outputSectionHeader( "Parameters", 4 )
        for arg in self.args:
                text += arg.out()
        return text

#----------------------------------------------------------------------------#
class Error( Entity ):
#----------------------------------------------------------------------------#
    def __init__( self, name, attrs ):
        Entity.__init__( self, name, attrs )

#----------------------------------------------------------------------------#
class Argument( Entity ):
#----------------------------------------------------------------------------#
    def __init__( self, name, attrs ):
        Entity.__init__( self, name, attrs )
        self.docs = ""

    def out( self ):
        text = ""
        text += "<i>%s: %s</i><p>%s</p>" % ( self.attrs["type"], self.attrs["name"], self.docs )
        return text

#----------------------------------------------------------------------------#
class Handler( ContentHandler ):
#----------------------------------------------------------------------------#
    def __init__( self, iface ):
        ContentHandler.__init__( self )
        self.iface = iface
        self.parent = None
        self.current = None
        self.doc = None
        self.method = None
        self.arg = None
        self.text = ""

    def startDocument( self ):
        pass

    def endDocument( self ):
        pass

    def startElement( self, element, attrs ):
        if not element.startswith( "doc" ):
            self.current = element
        else:
            self.doc = element.split( ':' )[1]
        self.name = attrs.get( "name", "" )
        self.attrs = attrs
        print element, self.name, "(in %s)" % self.current or None

        if element == "interface":
            self.iface.namespace = self.name.strip()

        elif element == "method":
            self.method = Method( self.name.strip(), attrs )

        elif element == "arg":
            self.arg = Argument( self.name.strip(), attrs )

        elif element == "signal":
            self.signal = Signal( self.name.strip(), attrs )

    def characters( self, char ):
        c = char.strip() + " "
        if c:
            # print c
            self.text += c

    def endElement( self, element ):

        if element == "doc:summary" and self.current == "node":
            self.iface.title = self.text.strip()

        elif element == "doc:summary" and self.current == "arg":
            self.arg.docs = self.text.strip()

        elif element == "doc:para" and self.current == "interface":
            self.iface.description = self.text.strip()

        elif element == "method":
            assert self.method is not None
            self.iface.methods.append( self.method )
            self.method = None

        elif element == "signal":
            assert self.signal is not None
            self.iface.signals.append( self.signal )
            self.signal = None

        elif element == "arg":
            assert self.arg is not None
            if self.method is not None:
                self.method.args.append( self.arg )
            else:
                self.signal.args.append( self.arg )
            self.arg = None

        print self.text, element

        self.text = ""
        self.current = None
        self.parent = element

#----------------------------------------------------------------------------#
if __name__ == "__main__":
#----------------------------------------------------------------------------#
    import sys
    import xml.sax
    print "parsing..."
    interfaces = []
    for filename in sys.argv[1:]:
        interface = Interface( filename )
        interfaces.append( interface )
        handler = Handler( interface )
        xml.sax.parse( filename, handler )
    print "creating..."
    for iface in interfaces:
        iface.output()
