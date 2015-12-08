from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def test(request):
    """ test the capability of bootstrap """

    return render(request,"firsttest.html",{})
