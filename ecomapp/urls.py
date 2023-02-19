from django.urls import path


app_name = "ecomapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]