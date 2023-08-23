from django.urls import path, re_path

from . import views
from .views import (
    ElectronicsView,
    ElectronicsTemplateView,
    ElectronicsListView,
    EquipmentView
)

urlpatterns = [
    path(route='', view=views.index, name='index'),
    re_path(route=r'^\d+', view=views.detail, name='detail'),
    re_path(route=r'^electronics-function-view$',
            view=views.electronics, name='electronics-function-view'),
    re_path(route=r'^electronics-class-view$',  view=ElectronicsView.as_view(),
            name='electronics-class-view'),
    re_path(route=r'^electronics-mixins-view$',  view=EquipmentView.as_view(),
            name='electronics-mixins-view'),
    re_path(route=r'^electronics-template-view$',
            view=ElectronicsTemplateView.as_view(),
            name='electronics-template-view'),
    re_path(route=r'^electronics-list-view$',
            view=ElectronicsListView.as_view(), name='electronics-list-view'),
]
