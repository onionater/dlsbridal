#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import sys
#import MySQLdb
import cgitb, cgi, MySQLdb, ast
#import cgitb, cgi, ast
import base64
import random
#import site

myform=cgi.FieldStorage()
cgitb.enable()
#cursor = MySQLdb.connect(host="localhost",user="askerry",passwd="password",db="aesbehave").cursor()

print 'Content-type:text/html\n\n'
print 'testing'
print sys.version
print sys.path
#site.getsitepackages()
