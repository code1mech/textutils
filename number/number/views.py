#I have created this python file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def analyze(request):
    #Get the text
    # check checkbox values
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    #check which checkbox is on
    params = {}
    if removepunc =="on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()

        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                 analyzed = analyzed + char
        params = {'purpose': 'Removed Newline', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Spaces', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (charcounter == "on"):
        count=0
        for char in djtext:
            if char!=" ":
                count=count+1
        params = {'purpose': 'Total character counted', 'analyzed_text': count}


    return render(request, 'analyze.html', params)



