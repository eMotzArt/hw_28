from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import users.views

urlpatterns = [
    path('users/', users.views.UsersListView.as_view()),
    path('users/create/', users.views.UserCreateView.as_view()),
    path('users/<int:pk>', users.views.UserDetailView.as_view()),
    path('users/<int:pk>/update/', users.views.UserUpdateView.as_view()),
    path('users/<int:pk>/delete/', users.views.UserDeleteView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
