from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import PetForm
from django.contrib.auth.models import User


# Create your views here.
def addPet(request):
	print(request.user)
	if request.method == 'POST':
		form = PetForm(request.POST, request.FILES)
		if form.is_valid():
			petToAdd = form.save(commit=False)
			petToAdd.user = request.user
			petToAdd.save()
			return redirect('profileManager:profile')
	else:
		form = PetForm()
	context = {'form': form}
	return render(request, 'app/petManager/addPet.html', context)
