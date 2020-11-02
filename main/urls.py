from django.urls import path 
from . import views 
from .views import EmployeeFormView, EmployeeDataList, EmployeeUpdate, EmployeeDelete, detail_view

urlpatterns = [
    path('', EmployeeFormView.as_view(), name = 'form_view'),
    path('list/', EmployeeDataList.as_view(), name = 'list_view'),
    path('list/<pk>/update', EmployeeUpdate.as_view(), name = 'update_view'),
    path('list/<pk>/delete', EmployeeDelete.as_view(), name = 'delete_view'),
    path('list/<pk>/detail', views.detail_view, name = 'detail_view'),
]
