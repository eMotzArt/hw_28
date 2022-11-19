from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
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


    path('locs/', ads.views.LocationsListView.as_view()),
    path('locs/create/', ads.views.LocationCreateView.as_view()),
    path('locs/<int:pk>', ads.views.LocationDetailView.as_view()),
    path('locs/<int:pk>/update/', ads.views.LocationUpdateView.as_view()),
    path('locs/<int:pk>/delete/', ads.views.LocationDeleteView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
