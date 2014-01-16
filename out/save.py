#!/usr/bin/python

import cgitb, cgi, MySQLdb, ast
#import cgitb, cgi, ast
import base64
import random

myform=cgi.FieldStorage()
cgitb.enable()
cursor = MySQLdb.connect(host="localhost",user="askerry",passwd="password",db="aesbehave").cursor()

print 'Content-type:text/html\n\n'

try:
    rsvpname=myform['rsvpname']
    rsvpval=myform['rsvpvalues']
    contentvar="RSVP"
    sql='insert into DLSRSVP (name,rsvp) values ("%s", "%s")' %(rsvpname.value, rsvpval.value)
except:
    pass
try:
    photo64=myform['photofield']
    contentvar="photo"
    sql='insert into DLSPHOTO (photo) values ("%s")' %(photo64.value)
except:
    pass
try:
    msg=myform['textmessage']
    contentvar="text"
    sql='insert into DLSMSG (msg) values ("%s")' %(msg.value)
except:
    pass
try:
    vid=myform['videosaved']
    contentvar="video"
except:
    pass
try:
    cursor.execute(sql)
except:
    pass
#g = open("/home/www/mindhive/saxe/aesvid/files/aesoutput"+str(random.randint(0,10000))+".jpg", "w")
#g.write(base64.decodestring(photo64))
#g.close()

with open("saved.html", "r") as myfile: 
    newhtml=myfile.read().replace('\n', '') 
newhtml=newhtml.replace('CONTENTVARIABLESTRING',contentvar)
print newhtml 

