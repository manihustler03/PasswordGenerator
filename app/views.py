from django.shortcuts import render
import random

# Create your views here.

def homePage(request):
    char = []
    
    if request.GET.get('uppercase'):
        char.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if request.GET.get('lowercase'):
        char.extend('abcdefghijklmnopqrstuvwxyz')
        
    if request.GET.get('number'):
        char.extend('0123456789')
        
    if request.GET.get('special'):
        char.extend('\!@#$%^&*()/')
        
    try:
        length = int(request.GET.get('len', 8))
    except ValueError:
        length = 8

    if not char:
        char.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()/')

    gen_password = ''.join(random.choice(char) for i in range(length))
    
    
    return render(request,'app/home.html', {'password':gen_password})

