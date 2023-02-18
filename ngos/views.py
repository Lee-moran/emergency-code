from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.db.models.functions import Lower
from .models import Category, NonGovernmentOrg


def all_ngos(request):
    """
    A view to show all the NGOs, including
    sorting and search queries
    """
    nongovernmentorgs = NonGovernmentOrg.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                nongovernmentorgs = nongovernmentorgs.annotate(
                    lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            nongovernmentorgs = nongovernmentorgs.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            nongovernmentorgs = nongovernmentorgs.filter(
                category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('ngos'))

            queries = (Q(name__icontains=query) |
                       Q(category__icontains=query) |
                       Q(description__icontains=query))
            nongovernmentorgs = nongovernmentorgs.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'nongovernmentorgs': nongovernmentorgs,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'ngos/ngos.html', context)


def ngo_detail(request, nongovernmentorg_id):
    """ A view to show the individual NGO detail page """

    ngos = NonGovernmentOrg.objects.all()
    nongovernmentorg = get_object_or_404(NonGovernmentOrg,
                                         pk=nongovernmentorg_id)

    context = {
        'nongovernmentorg': nongovernmentorg,
    }

    return render(request, 'ngos/ngo_detail.html', context)
