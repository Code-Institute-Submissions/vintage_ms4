from django.shortcuts import render
from .models import Arrival


def new_arrivals(request):
    """ The view which returns newest additions to the store """

    arrivals = Arrival.objects.all()

    context = {
        'arrivals': arrivals,
    }

    return render(request, 'arrivals/arrivals.html', context)
