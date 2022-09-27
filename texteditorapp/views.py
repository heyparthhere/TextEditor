from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import UserLogin, UserRegistration, Contactform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import*
from django.conf import settings
from gtts import gTTS
import os
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            # username = form.cleaned_data["username"]
            email=form.cleaned_data["email"]

        #     print(username)

            # for sending mails
            
            subject = f'Registration Successfully Completed {first_name}'
            message = f'Hi {first_name}, thank you for registering in our website.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list =[f"{email}"]
            send_mail( subject, message, email_from, recipient_list )
            
        #     # ----------------------------------------------------------------------

            form.save()
            messages.success(request,f'{first_name} Successfully Registred')
            form = UserRegistration()
        return render(request, 'register.html', {'form': form})
    else:
        form = UserRegistration()
        context = {'form': form }
    return render(request, 'register.html', context)


def login1(request):
    form = UserLogin()
    if request.method == "POST":
        uname=request.POST['username']
        upass=request.POST['password']
        user = authenticate(username=uname,password=upass)
        if user is None:
            messages.error(request,'Please Enter Correct Details...')
            return redirect('login1')
        else:
            login(request, user)
            messages.success(request,'Login Successfull...')
            return redirect('/index/')
    else:
        if request.user.is_authenticated:
            return redirect('/index/')
        else:
            return render(request,'login1.html',{'form':form})

def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Successfully Loged Out")
        return redirect("login1")
    else:
        messages.info(request,"Please Login First")
    return redirect("login1")

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Hello Parth Shah</h1>")

def analyze(request):
    # Get the text
    og_text = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    upcase=request.POST.get('upcase','off')
    lower=request.POST.get('lower', 'off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    tts=request.POST.get('tts','off')
    saveaudio=request.POST.get('saveaudio','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in og_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        og_text=analyzed
        # return render(request, 'analyze.html', params)

    if (upcase == "on"):
        analyzed = ""
        for char in og_text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        og_text=analyzed
        # return render(request, 'analyze.html', params)

    if (lower == "on"):
        analyzed = ""
        for char in og_text:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        og_text=analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in og_text:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        og_text=analyzed
        # return render(request, 'analyze.html', params)

    if(spaceremover == "on"):
        analyzed = ""
        for char in og_text:
            if char !=" ":
                analyzed = analyzed + char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}

    if(tts == "on"):
        engine.say(og_text)
        engine.runAndWait()
        params = {'purpose': 'Text To Voice'}


    if(saveaudio=="on"):
        analyzed = "Audio Saved Successfully"
        saytext = og_text
        language = 'en'
        say_obj = gTTS(text= saytext, lang=language, slow=False)
        say_obj.save('SavedAudio.mp3')
        os.system('mpg321 SavedAudio.mp3')
        params = {'purpose': 'Save Audio', 'analyzed_text': analyzed}

    if(removepunc != "on" and upcase != "on" and newlineremover != "on" and spaceremover != "on" and lower!="on" and tts!="on" and saveaudio !="on"):
        return render(request, 'error.html')
        # return HttpResponse('<h1>Error In Analyzing...<br><br>Please Select Valid Option...<br><br><a href="/index/">Back</a>')
    
    return render(request, 'analyze.html', params)

def Contact(request):
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.login_id = request.user
            instance.save()
                # form.save()
            messages.success(request,"Response Successfully Recorded We Will Get Back You Soon...")
            form = Contactform()
            return render(request,'contact.html',{'form':form})
        else:
            messages.error(request, "Please Enter Correct Details..")
            return render(request,'contact.html',{'form':form})
    else:
        form = Contactform()
        context = {'form' : form,}
        return render(request,'contact.html',context)

def About(request):
    return render(request, 'about.html')

def MiniProject(request):
    return render(request, 'MiniProjects.html')

def Websites(request):
    return render(request, 'websites.html')

def Applications(request):
    return render(request, 'applications.html')