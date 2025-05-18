from django import forms


class PostForm(forms.Form):
    status = forms.CharField(max_length=50)
    kind = forms.CharField(max_length=50)
    category = forms.CharField(max_length=50)
    sub_category = forms.CharField(max_length=50)
    amount = forms.FloatField()
    note = forms.CharField(max_length=50)

