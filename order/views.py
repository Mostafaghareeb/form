from django.shortcuts import render
from .forms import FormForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        message = request.POST['message']
        data = FormForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, 'index.html')
    