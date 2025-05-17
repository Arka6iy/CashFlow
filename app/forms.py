from wsgiref.validate import validator
from django.core.exceptions import ValidationError

from django import forms

class PostForm(forms.Form):
    # created_at = forms.DateTimeField()
    status = forms.CharField( max_length=50)
    kind = forms.CharField( max_length=50)
    category = forms.CharField( max_length=50)
    sub_category = forms.CharField(max_length=50)
    amount = forms.FloatField()
    note = forms.CharField(max_length=50)




    # def clean_text(self):
    #     x = ["плохое слово", "нет"]
    #     text = self.cleaned_data["kind"]
    #     for i in x:
    #         if i in text:
    #             raise ValidationError("Убери мат")
    #     return text