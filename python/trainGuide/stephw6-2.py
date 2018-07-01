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

        i=0
        while i<length:
            if fromLine[i] == toLine[i] and fromLine[i]==1:
                fromToData.append({"print":"From Station: "+fromSta})
                fromToData.append({"print":"Train: "+trainLine[i]})
                fromToData.append({"print":"To Station: "+toSta})
                fromToData.append({"print":"--------------------------------------"})
            i+=1
        print(fromToData)

        if fromToData==[]:
            for everyLine in fromTrain:
                index=trainLine.index(everyLine)
                stationList=trainData[index].get("Stations")
                for station in stationList:
                    for everyLine2 in toTrain:
                        index2=trainLine.index(everyLine2)
                        if station in trainData[index2].get("Stations"):
                            fromToData.append({"print":"From Station: "+fromSta})
                            fromToData.append({"print":"Train1: "+trainLine[index]})
                            fromToData.append({"print":"Station1: "+station})
                            fromToData.append({"print":"Train2: "+trainLine[index2]})
                            fromToData.append({"print":"To Station: "+toSta})
                            fromToData.append({"print":"--------------------------------------"})
                            print(fromToData)
        
        if fromToData==[]:
            for everyLine in fromTrain:
                index=trainLine.index(everyLine)
                stationList2=trainData[index].get("Stations")
                for station in stationList2:
                    for train in trainLine:
                        if train==everyLine:
                            continue
                        index3=trainLine.index(train)
                        if station in trainData[index3].get("Stations"):
                            for everyStation in trainData[index3].get("Stations"):
                                for everyLine2 in toTrain:
                                    if everyLine2==everyLine:
                                        continue
                                    index4=trainLine.index(everyLine2)
                                    if everyStation in trainData[index4].get("Stations"):
                                        fromToData.append({"print":"From Station: "+fromSta})
                                        fromToData.append({"print":"Train1: "+everyLine})
                                        fromToData.append({"print":"Station1: "+station})
                                        fromToData.append({"print":"Train2: "+trainLine[index3]})
                                        fromToData.append({"print":"Station2: "+everyStation})
                                        fromToData.append({"print":"Train3: "+trainLine[index4]})
                                        fromToData.append({"print":"To Station: "+toSta})
                                        fromToData.append({"print":"--------------------------------------"})
                                        break
        self.render("stephw6-2Page2.html")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/seni", SabHandler)
], debug=True)