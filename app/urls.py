from django.urls import path
from .views import Registration,LoginView,UserListView,UserUpdateView
urlpatterns = [
    path('register/', Registration.as_view(), name='register'),
    path('', LoginView.as_view(), name='login'),
    path('userlist/', UserListView.as_view(), name='userlist'),
    path('update/<int:id>/', UserUpdateView.as_view(), name='update'),
]