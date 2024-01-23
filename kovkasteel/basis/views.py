from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'basis/basis.html')

def project(request):
	return render(request, 'basis/project.html')

def services(request):
	return render(request, 'basis/services.html')

def works(request):
	return render(request, 'basis/works.html')
