from django import forms
from .models import Item


# ItemForm instance will be passed as context to template 
class ItemForm(forms.ModelForm):
    # inner class 'Meta' provides outer class with
    # information about itself
    class Meta:
        model = Item
        # fields from model to display 
        # (will display all if this is not explicitly defined)
        fields = ['name', 'done'] 