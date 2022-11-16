from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import DetailView, ListView
import json

from .models import Category, Advertisement, User, Location

def index(request):
    return JsonResponse({'status': 'ok'})

@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()

        response = []
        [response.append(category.get_dict()) for category in categories]

        return JsonResponse(response, safe=False)

    def post(self, request):
        category_data = json.loads(request.body)
        category = Category()
        [setattr(category, name, value) for name, value in category_data.items()]
        category.save()
        return JsonResponse(category.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        categories = Category.objects.all()

        response = []
        [response.append(category.get_dict()) for category in categories]

        return JsonResponse(response, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse(category.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsView(View):
    def get(self, request):
        ads = Advertisement.objects.all()

        response = []
        [response.append(ad.get_dict()) for ad in ads]

        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Advertisement()
        [setattr(ad, name, value) for name, value in ad_data.items()]
        ad.save()
        return JsonResponse(ad.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsListView(ListView):
    model = Advertisement

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        ads = Advertisement.objects.all()

        response = []
        [response.append(ad.get_dict()) for ad in ads]

        return JsonResponse(response, safe=False)

    # def post(self, request):
    #     ad_data = json.loads(request.body)
    #     ad = Advertisement()
    #     [setattr(ad, name, value) for name, value in ad_data.items()]
    #     ad.save()
    #     return JsonResponse(ad.get_dict(), safe=False)

class AdvertisementsDetailView(DetailView):
    model = Advertisement

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse(ad.get_dict(), safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class LocationsListView(ListView):
    model = Location

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        locs = Location.objects.all()

        response = []
        [response.append(loc.get_dict()) for loc in locs]

        return JsonResponse(response, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UsersListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        users = User.objects.all()

        response = []
        [response.append(user.get_dict()) for user in users]

        return JsonResponse(response, safe=False)