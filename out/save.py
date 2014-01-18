#!/usr/bin/python
###!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import cgitb, cgi, MySQLdb, ast
#import cgitb, cgi, ast
import base64
import random

myform=cgi.FieldStorage()
cgitb.enable()
cursor = #MySQLdb.connect(host="localhost",user="askerry",passwd="password",db="aesbehave").cursor()

print 'Content-type:text/html\n\n'
#print 'testing'
#print myform.keys()
#print myform.items()
contentvar='?'
try:
    rsvpname=myform['rsvpname']
    rsvpval=myform['rsvpvalues']
    contentvar="RSVP"
    sql='insert into DLSRSVP (name,rsvp) values ("%s", "%s")' %(rsvpname.value, rsvpval.value)
except:
    pass
try:
    photo64=myform['photofield']
    photo64= photo64.value.split(',')
    for photo in photo64:
        if 'base64' not in photo:
            contentvar="photo"
            sql='insert into DLSPHOTO (photo) values ("%s")' %(photo)
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
    print sql
    cursor.execute(sql)
except:
    pass
try:
    contentvar='photo'
    photo64=myform['uploadedphotos']
    photo64=photo64.value.split(',')
    #print len(photo64)
    for photo in photo64:
        if 'base64' not in photo:
            #print photo
            multisql='insert into DLSPHOTO (photo) values ("%s")' %(photo)
            #print multisql
            try:
                cursor.execute(multisql)
                #print "photo uploaded"
            except:
                pass
except:
    pass    

with open("saved.html", "r") as myfile: 
    newhtml=myfile.read().replace('\n', '') 
newhtml=newhtml.replace('CONTENTVARIABLESTRING',contentvar)
print newhtml 
