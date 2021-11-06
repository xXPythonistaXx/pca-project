from django.urls import path
from . import views

urlpatterns = [
    path('', views.HardManager, name='hard-manager'),
    path('datacenter/<int:id>', views.DataCenterView, name="datacenter-view"),
    path('newEquip/', views.NewEquip, name="new-equip"),
    path('edit/<int:id>', views.editDataCenter, name="edit-dataCenter"),
    path('delete/<int:id>', views.deleteDataCenter, name="delete-dataCenter"),
]
