from django.shortcuts import render
from .models import Arrival


def new_arrivals(request):
    """ The view which returns latest arrivals """

    arrivals = Arrival.objects.all()

    context = {
        'arrivals': arrivals,
    }

    return render(request, 'arrivals/arrivals.html', context)
