from django.urls import path
from .views import registerCreateView

urlpatterns = [
    path("", registerCreateView.as_view(), name="register"),
    # path("users/", userListView.as_view(), name="users"),
]
