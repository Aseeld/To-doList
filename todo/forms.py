from django import forms
from .models import Note

class AddNoteForm(forms.Form):
    
    class Meta:     
        model =Note
        fields = ("title", "description", "due_date")

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['title'].widget.attrs.update({ 
            'class': 'input is-success is-rounded', 
            'required':'', 
            'name':'title', 
            'id':'title', 
            'type':'text',     
            }) 
        self.fields['description'].widget.attrs.update({ 
            'class': 'input is-success is-rounded', 
            'required':'', 
            'name':'description', 
            'id':'description', 
            'type':'text',  
            }) 
        self.fields['due_date'].widget.attrs.update({ 
            'class': 'input is-success is-rounded', 
            'required':'', 
            'name':'due_date', 
            'id':'due_date', 
            'type':'date',  
            }) 
       