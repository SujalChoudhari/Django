# author Sujal Choudhari
from django.http import HttpResponse
from django.shortcuts import render

def index(req):

    text = req.POST.get("text","default")
    ogtext = text
    removepunc = req.POST.get("removepunc","off")
    fullcaps = req.POST.get("fullcaps","off")
    newlineremover = req.POST.get("newlineremover","off")
    extraspaceremover = req.POST.get("extraspaceremover","off")

    if text == "default":
        return render(req,"index.html")

    modifiers = ""

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in punctuations:
            text = text.replace(char,"")

        modifiers += "Removed Punctuations\n"
    
    if fullcaps == "on":
        text = text.upper()
        modifiers += "Changed to Uppercase\n"

    if newlineremover == "on":
        text = text.replace("\n","")
        text = text.replace("\r","")
        modifiers += "Removed New Lines\n"

    if extraspaceremover == "on":
        text = text.replace("  "," ")
        modifiers += "Removed Extra Spaces\n"
     
    params = {"original":ogtext,"final":text,"modifiers":modifiers}

    return render(req,"index.html",params)