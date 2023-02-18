from django.shortcuts import render
from ngos.models import Category, NonGovernmentOrg


def index(request):
    """ A view to return the index page """
    categories = Category.objects.all()
    nongovernmentorg = NonGovernmentOrg.objects.all()

    context = {
        'categories': categories,
        'nongovernmentorg': nongovernmentorg,
    }

    return render(request, 'home/index.html', context)
