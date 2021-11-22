from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def policies(request):
    return render(request, 'policies.html', {})

def event(request):
    return render(request, 'event.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def create_event(request):
    return render(request, 'create_event.html', {})

def withdraw_historic(request):
    return render(request, 'withdraw_historic.html', {})

def report(request):
    return render(request, 'report.html', {})