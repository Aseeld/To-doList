from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import Type,Note
from .forms import AddNoteForm
from django.views.generic import (
    ListView,
    CreateView,
)

class TypeListView(ListView):
    model = Type
    template_name = "todo/default.html"


class NoteListView(ListView):
    model = Note
    template_name = "todo/List_details.html"

    def get_queryset(self):
        return Note.objects.filter(type_id=self.kwargs["type_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["List_details"] = Type.objects.get(id=self.kwargs["type_id"])
        return context

class TypeCreate(CreateView):
    model = Type
    # template_name = "todo/add_type.html"
    fields = ["title"]

    def get_context_data(self):
        context = super(TypeCreate, self).get_context_data()
        return context

    def get_success_url(self):
        return reverse("default")

class NoteCreate(CreateView):
    model = Note

    fields = [       
        "title",
        "description",
        "due_date",
        "type",
    ]

    def get_initial(self):
        initial_data = super(NoteCreate, self).get_initial()
        todo_type = Type.objects.get(id=self.kwargs["type_id"])
        initial_data["todo_type"] = todo_type
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        todo_type = Type.objects.get(id=self.kwargs["type_id"])
        context["todo_type"] = todo_type
        return context

    def get_success_url(self):
        return reverse("note-add", args=[self.object.type_id])

