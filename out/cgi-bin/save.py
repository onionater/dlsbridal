#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
###!/usr/bin/python

import cgitb, cgi, MySQLdb, ast
#import cgitb, cgi, ast
import base64
import random

myform=cgi.FieldStorage()
cgitb.enable()
#cursor = MySQLdb.connect(host="localhost",user="askerry",passwd="password",db="aesbehave").cursor()

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
    recipevars=['recipetitle', 'recipeing', 'recipeinst','recipehist', 'recipenut', 'recipeauthor','recipetype']
    recipevariables=[]
    recipevalues=[]
    for var in recipevars:
        try:
            value=myform[var].value
            recipevariables.append(var)
            recipevalues.append(value)
        except: 
            pass
    try:
        photo64=myform['recipephoto']
        photo64= photo64.value.split(',')
        for photo in photo64:
            if 'base64' not in photo:
                contentvar="photo"
                recipevalues.append(photo)
                recipevariables.append('recipephoto')
    except:
        pass
    if recipevariables:
        contentvar="recipe"
        recipevariablesstr=', '.join(recipevariables)
        recipevaluesstr='", "'.join(recipevalues)
        recipevaluesstr='"'+recipevaluesstr+'"'
        sql='insert into DLSRECIPE ('+recipevariablesstr+') values ('+recipevaluesstr+')' 
        #print sql
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
try:
    photo64=myform['uploadedphotos']
    photo64=photo64.value.split(',')
    contentvar='photo'
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
#print newhtml 

