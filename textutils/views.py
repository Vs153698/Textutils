
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact,Contactmodal
def index(request):
    return render(request,'index.html')
def analyzed(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc',"off")

    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    print(removepunc)
    print(djtext)

    if removepunc =='on':
        analysis = ""

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analysis=analysis+char
        params = {'purpose1': 'Punctuations Had Been Removed', 'analyzed': analysis}
        djtext=analysis

        # return render(request,'analyze.html',params)
    if newlineremover=='on':
        analysis=""
        for char in djtext:
            if char != '\n' and char != '\r':
                analysis=analysis+char
        params = {'purpose3': 'NewLine Had Been Removed Completely', 'analyzed': analysis}
        # return render(request, 'analyze.html', params)
        djtext=analysis


    if extraspaceremover=='on':
        analysis=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analysis=analysis+char

        params={'purpose2': 'Extra Space Had Been Removed', 'analyzed': analysis}
        # return render(request,'analyze.html',params)
        djtext = analysis

    if (removepunc!='on' and newlineremover!='on' and extraspaceremover!='on')  :
        return render(request,'error.html')
    else:
        return render(request, 'analyze.html', params)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        text=request.POST['text']
        # print(name,email,phone,text)
        ins=Contact(name=name,email=email,phone=phone,text=text)
        ins.save()
        return render(request, 'success.html')
    else:
        return render(request, 'contact.html')

def about(request):
    if request.method=="POST":
        namemodal=request.POST['namemodal']
        emailmodal=request.POST['emailmodal']
        textmodal=request.POST['textmodal']
        # print(name,email,phone,text)
        inst=Contactmodal(namemodal=namemodal,emailmodal=emailmodal,textmodal=textmodal)
        inst.save()
        return render(request, 'about.html')
    else:
        return render(request, 'about.html')
def privacy(request):
    return render(request, 'privacy.html')













