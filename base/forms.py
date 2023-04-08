from django import forms

# Reoredring Form and View

class PositionForm(forms.Form):
    position = forms.CharField()