from django.shortcuts import render


def index(request):
    return render(request, 'aboutDataPage.html', {'onclick': 'return true'})
