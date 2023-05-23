from django.urls import path

from smarttender.views import TenderListView

urlpatterns = [
    path('', TenderListView.as_view(), name='index')
]
