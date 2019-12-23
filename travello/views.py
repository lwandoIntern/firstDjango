from django.shortcuts import render


# Create your views here.
from travello.models import Destination


def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'Some Indian City, don\'t care'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.desc = 'Beautiful city'
    dest3.img = 'destination_3.jpg'
    dest3.price = 845
    dest3.offer= True

    destinations = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dest1': destinations})
