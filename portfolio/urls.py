from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("portfolio/", views.index, name="index"),
    path("portfolio/new/", views.new_portfolio, name="new_portfolio"),
]
