from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Listing
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_pulished=True)
    paginator = Paginator(listings, 6)

    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'listings': page_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')