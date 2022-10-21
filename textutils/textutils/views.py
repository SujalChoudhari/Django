# author Sujal Choudhari
from django.http import HttpResponse
from django.shortcuts import render

def index(req):

    text = req.GET.get("text","default")
    ogtext = text
    removepunc = req.GET.get("removepunc","off")
    fullcaps = req.GET.get("fullcaps","off")
    newlineremover = req.GET.get("newlineremover","off")
    extraspaceremover = req.GET.get("extraspaceremover","off")

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
        modifiers += "Removed New Lines\n"

    if extraspaceremover == "on":
        text = text.replace("  "," ")
        modifiers += "Removed Extra Spaces\n"
     
    params = {"original":ogtext,"final":text,"modifiers":modifiers}

    return render(req,"index.html",params)