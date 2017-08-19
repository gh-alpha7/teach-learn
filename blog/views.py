from django.shortcuts import render,redirect
from .models import code,answ,homepage


def topic(request):
    post=homepage.objects.all()
    return render(request,'blog/main.html',{'post':post})

def addtopic(request):
    t1=request.GET.get("topic")
    if t1:
        homepage.objects.create(topic=t1)
        return redirect(topic)
    return render(request,'blog/top.html',{})

def questions(request):
    post=code.objects.all()
    return render(request,'blog/questions.html',{'post':post})

def ask(request):
    t1=request.GET.get("topic")
    q1=request.GET.get("question")
    if t1:
        code.objects.create(topic=t1,ids=3,question=q1)
        post=code.objects.all()
        return redirect(questions)
    return render(request,'blog/ask.html',{})

def answe(request):
    ans=answ.objects.all()
    return render(request,'blog/an.html',{"ans":ans})

def answerwa(request):
    t1=request.GET.get("top")
    q1=request.GET.get("que")
    usr=request.GET.get("user")
    ans=request.GET.get("answer")
    if usr:
        answ.objects.create(topic=t1,ques=q1,user_name=usr,answer=ans)
        ans=answ.objects.all()
        return redirect(answe)
    return render(request,'blog/ans.html',{})

def home(request):
    return redirect(topic)
