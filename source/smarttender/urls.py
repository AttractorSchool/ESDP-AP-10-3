from django.urls import path

from smarttender.views import TenderListView, ProductListView

urlpatterns = [
    #path('', TenderListView.as_view(), name='index')
    path('', ProductListView.as_view(), name='index')
]
