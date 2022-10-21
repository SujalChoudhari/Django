# author Sujal Choudhari
from django.http import HttpResponse
from django.shortcuts import render

def index(req):

    text = req.POST.get("text","default")
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
        # remove trailing spaces
        text = text.strip()
        # remove exccess spaces
        text = " ".join(text.split())
        modifiers += "Removed Extra Spaces\n"
     
    params = {"final":text,"modifiers":modifiers}

    return render(req,"index.html",params)