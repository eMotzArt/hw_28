from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView
import json

from .models import Category, Advertisement, User, Location

def index(request):
    return JsonResponse({'status': 'ok'})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        [response.append(category.get_dict()) for category in self.object_list]

        return JsonResponse(response, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category = Category.objects.create(name=category_data['name'])
        return JsonResponse(category.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse(category.get_dict(), safe=False)



@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsListView(ListView):
    model = Advertisement


    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        [response.append(ad.get_dict()) for ad in self.object_list]

        return JsonResponse(response, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsCreateView(CreateView):
    model = Advertisement
    fields = ['name', 'author', 'price', 'description', 'category', 'is_published']
    def post(self, request, *args, **kwargs):

        ad_data = json.loads(request.body)
        ad = Advertisement.objects.create(name=ad_data['name'],
                                          author=ad_data['author'],
                                          price=ad_data['price'],
                                          description=ad_data['description'],
                                          category=ad_data['category'],
                                          is_published=ad_data['is_published']
                                          )
        return JsonResponse(ad.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
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

        response = []
        [response.append(loc.get_dict()) for loc in self.object_list]

        return JsonResponse(response, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class LocationCreateView(CreateView):
    model = Location
    fields = ['name', 'lat', 'lng']

    def post(self, request, *args, **kwargs):
        location_data = json.loads(request.body)
        location = Location.objects.create(name=location_data['name'],
                                           lat=location_data['lat'],
                                           lng=location_data['lng']
                                           )
        return JsonResponse(location.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class LocationDetailView(DetailView):
    model = Location

    def get(self, request, *args, **kwargs):
        try:
            loc = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse(loc.get_dict(), safe=False)



@method_decorator(csrf_exempt, name='dispatch')
class UsersListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        [response.append(user.get_dict()) for user in self.object_list]

        return JsonResponse(response, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']


    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user = User.objects.create(first_name=user_data['first_name'],
                                   last_name=user_data['last_name'],
                                   username=user_data['username'],
                                   password=user_data['password'],
                                   role=user_data['role'],
                                   age=user_data['age'],
                                   location=user_data['location'])
        return JsonResponse(user.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse(user.get_dict(), safe=False)