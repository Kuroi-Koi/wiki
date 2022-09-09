from cgitb import html
from django.shortcuts import render

from markdown2 import Markdown

markdowner = Markdown()

import markdown2

from . import util

import random

def convert_to_html(title):
    userinput = util.get_entry(title)
    html = markdown2.markdown(userinput)
    if userinput == None:
        return None 
    else:
        return markdown2.markdown(userinput)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def newEntry(request):
    return render("encyclopedia/newEntry.html")    
    
def userinput(request, title):
    inputPage = util.get_entry(title)
    if inputPage == None:
        return render(request, "encyclopedia/error.html", {
            "userinputTitle": title
         })
    else: return render(request, "encyclopedia/entry.html", {
        "userinput": convert_to_html(title),
        "userinputTitle": title
    })            

def search(request):
    if request == "GET":
        input = request.GET('q')
        html = convert_to_html(input)
        entries = util.list_entries()
        search_page = []
        
        for userinput in entries:
            if input.upper() in userinput.upper():
                search_page.append(userinput)
                
        for userinput in entries:
            if input.upper() == userinput.upper():
                return render(request, "encyclopedia/entry.html", {
                    "userinput": html,
                    "userinputTitle": input
                })
            elif search_page != []:
                return render(request, "encyclopedia/search.html", {
                    "entries": search_page
                })
            else:
                return render(request, "encyclopedia/error.html", {
                    "userinputTitle": input
                })
                
def save(request):
    if request.method == 'post':
            input_title = request.post['title']
            input_text = request.post['text']
            entries = util.list_entries()
            html = convert_to_html(input_title)
            
            already_exist_true = "false"
            for userinput in entries:
                if input_title.uppper() == userinput.upper():
                    already_exist_true = "true"
            
            if already_exist_true == "true":
                return render("encyclodepedia/existing_entry.html", {
                    "userinput": html,
                    "userinputTitle": input_title
                })
                
            else:
                util.save_entry(input_title, input_text)
                return render(request, "encyclopedia/entry.html", {
                    "userinput": convert_to_html(input_title),
                    "userinputTitle": input_title
                })                    