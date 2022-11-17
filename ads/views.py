from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
import json

from project import settings
from .models import Category, Advertisement, User, Location

def index(request):
    return JsonResponse({'status': 'ok'})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        locs_page = []
        [locs_page.append(category.get_dict()) for category in page_obj]

        response = {
            'items': locs_page,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }
        return JsonResponse(response, safe=False)

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
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category = Category.objects.create(name=category_data['name'])
        return JsonResponse(category.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        self.object.name = category_data['name']

        self.object.save()
        return JsonResponse(self.object.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)



@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsListView(ListView):
    model = Advertisement


    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads_page = []
        [ads_page.append(ad.get_dict()) for ad in page_obj]

        response = {
            'items': ads_page,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }
        return JsonResponse(response, safe=False)

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
class AdvertisementsCreateView(CreateView):
    model = Advertisement
    fields = ['name', 'author', 'price', 'description', 'category', 'is_published']
    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        author_first_name, author_last_name = ad_data['author'].split()
        try:
            author = get_object_or_404(User, first_name=author_first_name, last_name=author_last_name)
        except Http404:
            return JsonResponse({'status': 'Author not found'}, status=404)

        category_data = ad_data['category']
        category, _ = Category.objects.get_or_create(name=category_data)

        ad = Advertisement.objects.create(name=ad_data['name'],
                                          author=author,
                                          price=ad_data['price'],
                                          description=ad_data['description'],
                                          category=category,
                                          is_published=ad_data['is_published']
                                          )
        return JsonResponse(ad.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsUpdateView(UpdateView):
    model = Advertisement
    fields = ['name', 'author', 'price', 'description', 'category', 'is_published']
    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)

        author_first_name, author_last_name = ad_data['author'].split()
        try:
            author = get_object_or_404(User, first_name=author_first_name, last_name=author_last_name)
        except Http404:
            return JsonResponse({'status': 'Author not found'}, status=404)

        category_data = ad_data['category']
        category, _ = Category.objects.get_or_create(name=category_data)


        self.object.name = ad_data['name']
        self.object.author = author
        self.object.price = ad_data['price']
        self.object.description = ad_data['description']
        self.object.category = category
        self.object.is_published = ad_data['is_published']

        return JsonResponse(self.object.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsDeleteView(DeleteView):
    model = Advertisement
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)



@method_decorator(csrf_exempt, name='dispatch')
class LocationsListView(ListView):
    model = Location

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        locs_page = []
        [locs_page.append(loc.get_dict()) for loc in page_obj]

        response = {
            'items': locs_page,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }
        return JsonResponse(response, safe=False)

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
class LocationUpdateView(UpdateView):
    model = Location
    fields = ['name', 'lat', 'lng']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        location_data = json.loads(request.body)
        self.object.name = location_data['name']
        self.object.lat = location_data['lat']
        self.object.lng = location_data['lng']

        return JsonResponse(self.object.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class LocationDeleteView(DeleteView):
    model = Location
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)



@method_decorator(csrf_exempt, name='dispatch')
class UsersListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


        users_page = []
        [users_page.append(user.get_dict()) for user in page_obj]

        response = {
            'items': users_page,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }
        return JsonResponse(response, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse(user.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']


    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user_loc, _ = Location.objects.get_or_create(name=user_data['location'])

        user = User.objects.create(first_name=user_data['first_name'],
                                   last_name=user_data['last_name'],
                                   username=user_data['username'],
                                   password=user_data['password'],
                                   role=user_data['role'],
                                   age=user_data['age'],
                                   location=user_loc)
        return JsonResponse(user.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']


    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)

        user_loc, _ = Location.objects.get_or_create(name=user_data['location'])

        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data['last_name']
        self.object.username = user_data['username']
        self.object.password = user_data['password']
        self.object.role = user_data['role']
        self.object.age = user_data['age']
        self.object.location = user_loc



        return JsonResponse(self.object.get_dict(), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)
