from django import forms
 
class AddForm(forms.Form):
    id = forms.IntegerField()
    #Todo = forms.CharField(max_length=350)