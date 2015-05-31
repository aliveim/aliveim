from django.shortcuts import render

def index(request):
    print "INSIDE THE VIEW"
    return render(request, 'landing/index.html')
