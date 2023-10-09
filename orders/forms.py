from django import forms


class OrderForm(forms.Form):
    email = forms.EmailField()
    model = forms.CharField(
        max_length=2, min_length=2, required=True, widget=forms.Textarea
    )
    version = forms.CharField(
        max_length=2, min_length=2, required=True, widget=forms.Textarea
    )
