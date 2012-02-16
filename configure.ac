##############################################################################
# init
AC_INIT([fso-specs], [2012.02.14.1], [smartphones-standards@linuxtogo.org], [fso-specs])
AC_CONFIG_SRCDIR([tools/rules.mk])
AM_INIT_AUTOMAKE([-Wall -Werror foreign no-dist-gzip dist-bzip2])
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

##############################################################################
# xlst is necessary for specs generation
AC_PATH_PROG(XSLTPROC, xsltproc, no)
AC_SUBST(XSLTPROC)
if test $XSLTPROC = "no"; then
    AC_MSG_ERROR([xsltproc is mandatory for this package])
fi

##############################################################################
# python is mandatory for docs generation
AC_PATH_PROG(PYTHON, python, no)
AC_SUBST(PYTHON)
if test $PYTHON = "no"; then
    AC_MSG_ERROR([python is mandatory for this package])
fi

##############################################################################
# output
AC_CONFIG_FILES([
        Makefile
        html/index.html
        fso-specs.pc
])
AC_OUTPUT
echo
echo
echo
echo "fso-specs configured successfully."
echo
echo "Now type 'make' to compile and 'make install' to install this package."
