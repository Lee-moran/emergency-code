from django.shortcuts import render
from .models import Category, NonGovernmentOrg


def all_ngos(request):
    """
    A view to show all the NGOs, including
    sorting and search queries
    """

    nongovernmentorgs = NonGovernmentOrg.objects.all()
    context = {
        'nongovernmentorgs': nongovernmentorgs,
    }

    return render(request, 'ngos/ngos.html', context)
