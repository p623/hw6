import webapp2
import os
from google.appengine.api import urlfetch
import json, codecs
import jinja2

f=codecs.open("trainData.json","r","utf-8")
trainData=json.load(f)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={"graph": trainData}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainHandler(BaseHandler):
    def get(self):
        self.render("stephw6-2Page1.html")

class SabHandler(BaseHandler):
    def get(self):
        self.render("stephw6-2Page2.html")
    

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/seni", SabHandler)
], debug=True)