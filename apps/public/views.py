from django.shortcuts import render


def home(request):
    values = {
        'title':'Home'
    }
    return render(request, "public/home.html", values)