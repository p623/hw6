#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import os
import json, codecs
import jinja2
import cgi

fromToData=[]
f=codecs.open("aliceData.json","r","utf-8")
trainData=json.load(f)


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={"graph": trainData, "graph2":fromToData}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainHandler(BaseHandler):
    def get(self):
        self.render("stephw6-2Page1.html")

class SabHandler(BaseHandler):
    def get(self):
        self.render("stephw6-2Page2.html")
        fromSta=cgi.escape(self.request.get("from"))
        toSta=cgi.escape(self.request.get("to"))
        trainLine=["Mimsy Line","Burrow Grove Express","Chesire","Queens Line", "Caterpillar Way"]
        fromLine=[]
        fromTrain=[]
        toLine=[]
        toTrain=[]
        length=0
        for dict in trainData:
            length+=1
            if fromSta in dict.get("Stations"):
                fromLine.append(1)
                fromTrain.append(dict.get("Name"))
            else:
                fromLine.append(0) 

        for dict in trainData:    
            if toSta in dict.get("Stations"):
                toLine.append(1)
                toTrain.append(dict.get("Name"))
            else:
                toLine.append(0)

        print(fromLine)
        print(fromTrain)
        print(toLine)
        print(toTrain)
        i=0
        while i<length:
            if fromLine[i] == toLine[i] and fromLine[i]==1:
                fromToData.append({"print":"from: "+fromSta})
                fromToData.append({"print":"train: "+trainLine[i]})
                fromToData.append({"print":"to: "+toSta})
                fromToData.append({"print":"--------------------------------------"})
                print(fromToData)
            else:
                if len(toTrain) >= len(fromTrain):
                    pass
                else:
                    pass
            i+=1

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/seni", SabHandler)
], debug=True)