from django.shortcuts import render,redirect
from .models import Super
from .forms import SuperForm

# Create your views here.



def ShowForm(request):
    cus = Super.objects.all()
    if request.method == 'POST':
        form = SuperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # or redirect
    else:
        form = SuperForm()
    return render(request, 'app/home.html', {'form': form,'cus':cus})

