from django.http import HttpResponse
from django.shortcuts import render
from .models import contact

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')
    if removepunc =='on':
        punctuations='''!()-[]{};:'"\,<>_/?@#$%^&*~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose':'remove punctuation','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed +  char.upper()
        params = {'purpose': 'capitalize', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremove =='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'New Line Remove','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html' ,params)
    if(spaceremove =='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index + 1] ==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remove', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(charcount == 'on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        count = len(analyzed)

        params = {'purpose': 'Char count','analyzed_text':analyzed,'char_count':count}
        djtext=analyzed

    return render(request, 'analyze.html',params)

def thankyou(request):
    Idno = request.POST.get('id')
    Name = request.POST.get('name')
    Email = request.POST.get('email')
    Query = request.POST.get('submitted[reason]')
    Message = request.POST.get('message')

    contact_ref = contact(idno=Idno,name=Name, email=Email, query=Query, message=Message)
    contact_ref.save()
    return render(request,'contact.html',{'message':'Thank you for contacting us ..!!!'})

