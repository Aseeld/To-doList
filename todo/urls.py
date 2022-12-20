from django.urls import path
from . import views

from .views import NoteCreate
urlpatterns = [
    path("", views.TypeListView.as_view(), name="default"),
    path("type/<int:type_id>/",views.NoteListView.as_view(), name="type"),
    path( "add_type/",views.TypeCreate.as_view(),name="type-add"),
    path("type/<int:type_id>/note/add",views.NoteCreate.as_view(), name="note-add"),
]