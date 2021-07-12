from django.urls import path

from .import views
from removalregister.views import RemovalListView,RemovalUpdateView,AddRemovalView,SearchRemoval

urlpatterns = [
    path('', RemovalListView.as_view(), name='index'),
    path('<pk>/update', RemovalUpdateView.as_view()),
    path('add/',AddRemovalView.as_view()),
    path('search/', SearchRemoval.as_view()),
]