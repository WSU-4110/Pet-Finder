from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import PetForm



# Create your views here.
def addPet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profileManager:profile')

    else:

        form = PetForm()

    context = {'form': form}

    return render(request, 'app/petManager/addPet.html', context)
