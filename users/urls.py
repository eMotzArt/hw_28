from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import users.views

urlpatterns = [
    path('user/', users.views.UsersListView.as_view()),
    path('user/create/', users.views.UserCreateView.as_view()),
    path('user/<int:pk>', users.views.UserDetailView.as_view()),
    path('user/<int:pk>/update/', users.views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', users.views.UserDeleteView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
