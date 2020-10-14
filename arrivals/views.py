from django.shortcuts import render

from .models import Arrivals


def new_arrivals(request):
    """ The view which returns latest arrivals """

    arrivals = Arrivals.objects.all()

    context = {
        'arrivals': arrivals,
    }

    return render(request, 'arrivals/arrivals.html', context)
