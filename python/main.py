#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2
import cgi

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainHandler(BaseHandler):
    def get(self):
        self.render('main2.html')
 
#class MainHandler(webapp2.RequestHandler):
 #   def get(self):
  #      self.response.headers['Content-Type']='text/html'
   #     self.render("main2.html")
        #self.response.write("")
        

class SubHandler(BaseHandler):
    def get(self):
        self.render("main3.html")
        word1=self.request.get("firstword")
        word2=self.request.get("secondword")
        n=len(word1)
        m=len(word2)
        mixword=""
        for i in range(n):
            mixword+=word1[i:i+1]+word2[i*m/n:(i+1)*m/n]
        self.response.out.write(mixword)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/seni',SubHandler),
], debug=True)
