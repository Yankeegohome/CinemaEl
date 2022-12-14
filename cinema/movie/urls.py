from django.urls import path
from .views import *
from . import views


urlpatterns = [
    # path('single/', get_single),
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', MovieByCategory.as_view(), name='category'),
    path('genre/<str:slug>', MovieByGenre.as_view(), name='genre'),
    path('movie/<str:slug>', GetMovie.as_view(), name='movie'),
    path('review/<int:pk>', views.AddReview.as_view(), name='add_review'),
]