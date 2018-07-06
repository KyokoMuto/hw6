#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2
import cgi
import json
import codecs

f=codecs.open("train.json",'r',"utf-8")
train=json.load(f)
train_load={}

for p in train:
    for i,v in p.items():
        if i=='Stations':  
            before='none'
            for j in v:
                if before!='none':
                    train_load.setdefault(j,[0]).append(before)
                    train_load.setdefault(before,[0]).append(j)
                before=j
f.close

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


class SubHandler(BaseHandler):
    def get(self):
        self.render("main3.html")
        word1=self.request.get("firstword")
        word2=self.request.get("secondword")
        next_word=[word1] 
        way=[word2]
        parent={}
        while(True):
            next=next_word[0]
            if next==word2:
                break
            else:
                for j in range(1,len(train_load[next])):
                    if train_load[train_load[next][j]][0]==0:
                        next_word.append(train_load[next][j])
                        train_load[train_load[next][j]][0]=1
                        parent[train_load[next][j]]=next
            del next_word[0]
        word=word2    
        while(True):
            way.append(parent[word])
            word=parent[word]
            if word==word1:
                break
        for k in range(len(way)):
            self.response.out.write(way[len(way)-1-k])
            #print(way[len(way)-1-k])

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/seni',SubHandler),
], debug=True)
