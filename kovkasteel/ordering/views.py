from django.shortcuts import render, redirect

from .forms import ClientForm

def client(request):
	error = ''
	if request.method == 'POST':
		form = ClientForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = "Некорректное заполнение формы"

	form = ClientForm()

	date ={
		'form': form,
		'error': error
	}

	return render(request, 'ordering/addclient.html', date)