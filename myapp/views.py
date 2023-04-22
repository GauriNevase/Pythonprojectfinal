from django.shortcuts import render
from .forms import sos , sosform


# Create your views here.
def sos(request):
    print("Hello")
    if request.method == 'POST':
        form = sos(request.POST)
        if form.is_valid():

            La = form.cleaned_data['La']
    

    form = sos()
    return render(request, 'sos.html', {'form': form} )

def sos_details(request):
    if request.mthod == 'POST':
        form = sosform(request.POST)
        if form.is_valid():
            form.save()
            print("Sucessfully completed")

    form = sosform()
    return render(request, 'sos.html', {'form': form} )