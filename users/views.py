import json

from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models import Location
from project import settings
from users.models import User


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
