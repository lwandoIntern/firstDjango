from django.shortcuts import render


# Create your views here.
from travello.models import Destination


def index(request):

    dest1 = Destination()

    return render(request, 'index.html', {'dest1': dest1})
