
from django.urls import path, register_converter
from . import views
from .views import PostDetailView
from . import converters

app_name = "blog"
register_converter(converters.KoreanSlugConverter, "korslug")

urlpatterns = [
    path("blog/", views.index, name="index"),
    path("blog/<int:pk>", views.post_detail, name="blog_detail"),
    # path("blog/<korslug:slug>", views.post_detail, name="blog_detail"),
    # path("1/", login_required(TemplateView.as_view(template_name="root.html")), name="root"),
]
