from django.shortcuts import render
from django import forms
from pexpect import pxssh
import getpass

def index(request):
    if "GET" == request.method:
        return render(request, 'myapp/index.html', {})
    else:       
        ip = request.POST.get('ip')
        username = request.POST.get('username')
        password = request.POST.get('password')

        s = pxssh.pxssh()
        s.login (ip, username, password)

        s.sendline('top > Log.txt')   # run a command
        s.prompt()             # match the prompt
        f = open("Log.txt")
        memory_usage = f.read(1)
        while memory_usage != "":
             memory_usage = f.read(1)
        #memory_usage = s.before
        print (memory_usage)        

        return render(request, 'myapp/metric.html', {"ip":ip,"username":username,"password":"******","memory_usage":memory_usage})
