"""Froms models"""

from django import forms


class ContactForm(forms.Form):
    """Contact form"""

    name = forms.CharField(max_length=32)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "textarea_control"})
    )
    time = forms.DateField(
        widget=forms.DateInput(attrs={"class": "datefield_control"})
    )
