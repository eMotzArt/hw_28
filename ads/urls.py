from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers

import ads.views

urlpatterns = [
    path('cat/', ads.views.CategoryListView.as_view()),
    path('cat/create/', ads.views.CategoryCreateView.as_view()),
    path('cat/<int:pk>', ads.views.CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', ads.views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', ads.views.CategoryDeleteView.as_view()),


    path('ads/', ads.views.AdvertisementsListView.as_view()),
    path('ads/create/', ads.views.AdvertisementsCreateView.as_view()),
    path('ads/<int:pk>', ads.views.AdvertisementsDetailView.as_view()),
    path('ads/<int:pk>/update/', ads.views.AdvertisementsUpdateView.as_view()),
    path('ads/<int:pk>/delete/', ads.views.AdvertisementsDeleteView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

locations_router = routers.SimpleRouter()
locations_router.register('locations', ads.views.LocationViewSet)
urlpatterns += locations_router.urls

