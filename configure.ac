##############################################################################
# init
AC_INIT([fso-specs], [2012.07.27.4], [fso@openphoenux.org], [fso-specs])
AC_CONFIG_SRCDIR([tools/rules.mk])
AM_INIT_AUTOMAKE([-Wall -Werror foreign no-dist-gzip dist-xz])
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

##############################################################################
# xlst is necessary for specs generation
AC_PATH_PROG(XSLTPROC, xsltproc, no)
AC_SUBST(XSLTPROC)
if test $XSLTPROC = "no"; then
    AC_MSG_ERROR([xsltproc is mandatory for this package])
fi

##############################################################################
# output
AC_CONFIG_FILES([
        Makefile
        fso-specs.pc
])
AC_OUTPUT
echo
echo
echo
echo "fso-specs configured successfully."
echo
echo "Now type 'make' to compile and 'make install' to install this package."
