from django.shortcuts import render

# Create your views here.

#using a function view since later will be adding lot of logics to this
def home_view(request):
    return render(request, 'sales/main.html', {})