from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import DetailView
import json

from .models import Category, Advertisement

def index(request):
    return JsonResponse({'status': 'ok'})

@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
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

class AdvertisementsDetailView(DetailView):
    model = Advertisement

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse(ad.get_dict(), safe=False)
