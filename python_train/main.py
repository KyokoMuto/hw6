#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2
import cgi
import json
import codecs

f=codecs.open("train.json","r","utf-8")
train=json.load(f)
train_load={}
for i,v in f.items():
    if i=="stations":
        for j in v:
            train_load.setdefault(j,[]).append(before)
            before=j
f.close

def broken_train():
    g=codecs.open("train_break.json","r","utf-8")
    f_break=load(g)
    for i in f:
        if i=="stations":
            for j in v:
                train_load.setdefault(j,[]).append(before)
                before=j
    f.close





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
        word1=List(cgi.escape(self.request.get("firstword")))
        word2=List(cgi.escape(self.request.get("secondword")))
        next_word=[word1]
        way=[word1]
        parent={}
        while(True):
            next=next_word[0]
            if next==word2:
                break
            else:
                for j in range(len(train_load[next])):
                    next_word.append(train_load[next][j])
                    parent[train_load[next][j]]=next
        word=word2
        while(true):
            way.append(parent[word])
            word=parent[word]
            if word==word1:
                break
        for k in range(len(way)):
            self.response.out.write(way[len(way)-k])

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/',SubHandler),
], debug=True)
