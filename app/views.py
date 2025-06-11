from django.shortcuts import render
from .models import Super
from .forms import SuperForm

# Create your views here.



def ShowForm(request):
    if request.method == 'POST':
        form = SuperForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/success.html')  # or redirect
    else:
        form = SuperForm()
    return render(request, 'app/base.html', {'form': form})

