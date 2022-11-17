from django.shortcuts import render
import markdown  
from django.http import HttpResponse
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def md_to_html(title):
    content = util.get_entry(title)
    if  content is None: 
        return None
    else:
        md = markdown.Markdown()
        return md.convert(content)
 

def link(request,title ):    
    
        converter = md_to_html(title)
        
        if converter is None:
            return render(request, "encyclopedia/404.html",{
                 "title" : "404",
                "content":  "Page not  founded"
            })
        else:
            return render(request, "encyclopedia/entry.html", {
        "content": converter,
        "entry_title" : title
    })


def search(request):
    if request.method == 'POST':
        title = request.POST['q']
        converter = md_to_html(title)
      
        if converter is not None:
            return render(request, "encyclopedia/entry.html", {
        "content": converter,
         "entry_title" : title
         })
        else:
            suggestion = []
            entries =  util.list_entries()
            for entry in entries:
                if title.lower() in entry.lower():
                    suggestion.append(entry)
                    return render(request, "encyclopedia/suggestion.html", {
                           "suggestion": suggestion
                  })                 

def New_Page(request):
        return render(request, "encyclopedia/New.html", {
        "title": "Create New Page"
    }) 

def Create_new_page(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        FileExist = util.get_entry(title)
        if FileExist is not None:
            return render(request, "encyclopedia/404.html",{
                "title" : "Already exist",
                "content":  title +" page is already exist"
            })
        else:    
            util.save_entry(title ,content )
            convter = md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
            "entry_title" : title,
            "content": content,
            })

def Show_edit_page(request):
    if request.method == "POST":
        title =  request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content" : content
        })
        
def edit(request):
       if request.method == "POST":
            title =  request.POST['title']
            content = request.POST['content']
            save_edit = util.save_entry(title ,content)
            converter = md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
            "entry_title": title,
            "content" : converter
            })
def Random_Page(request):
    entries = util.list_entries()
    ranEntry = random.choice(entries)
    converter = md_to_html(ranEntry)
    return render(request, "encyclopedia/entry.html", {
        "entry_title": ranEntry,
        "content":converter
    })

 




           
        
           
    


        

