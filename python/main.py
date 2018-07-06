#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2
import cgi

JINJA_ENVIROMENT=jinja2.Enviroment(
    loader=jinja2.FileSystemLoader(os.path.dirname(_file_)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler)):
    def render(self,html,values={}):
        template=JINJA_ENVIROMENT.get_template(html)
        self.response.write(template.render(values))

class MainHandler(BaseHandler):
    def get(self):
        self.render("main1.html")

class SubHandler(BaseHandler):
    def get(self):
        self.render("main2.html")
        word1=List(cgi.escape(self.request.get("word1")))
        word2=List(cgi.escape(self.request.get("word2")))
        n=len(word1)
        m=len(word2)
        mixword=""
        for i in range(n):
            mixword+=word1[i:i+1]+word2[i(m/n):i+1(m/n)]
        self.response.out.write(mixword)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/',SubHandler),
], debug=True)
