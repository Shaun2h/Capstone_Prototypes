from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator
from . import models


class QuestionForm(forms.Form):
    company = forms.CharField(label="Company", min_length=1, max_length=200)
    region = forms.CharField(label="Region",
                             widget=forms.Select(choices=(("NA", "NA"), ("SEA", "SEA"),
                                                          ("EUR", "EUR"), ("ASIA", "ASIA"),
                                                          ("CHINA", "CHINA")))
                             )
    city = forms.IntegerField(label="City", initial=1, validators=[MinValueValidator(1),
                                                                   MaxValueValidator(3)])
    product = forms.CharField(label="Product ID", min_length=1, max_length=200)

    def clean_company(self):
        data = self.cleaned_data["company"]
        if data not in models.allowed:
            raise ValidationError("Incorrect Company", code="Incorrect Value Entered")
        return data

    def clean_region(self):
        data = self.cleaned_data["region"]
        # if data not in models.allowed:
        #     raise ValidationError("Incorrect Region ID", code="Incorrect Value Entered")
        return data

    def clean_city(self):
        data = self.cleaned_data["city"]
        # if data not in models.allowed:
        #     raise ValidationError("Incorrect City ID", code="Incorrect Value Entered")
        return data

    def clean_product(self):
        data = self.cleaned_data["product"]
        return data
        # if data not in models.allowed:
        #     raise ValidationError("Incorrect Product", code="Incorrect Value Entered")


class InsertForm(forms.Form):
    company = forms.CharField(label="Company", min_length=1, max_length=200)
    region = forms.CharField(label="Region",
                             widget=forms.Select(choices=(("NA", "NA"), ("SEA", "SEA"),
                                                          ("EUR", "EUR"), ("ASIA", "ASIA"),
                                                          ("CHINA", "CHINA")))
                             )

    city = forms.IntegerField(label="City", initial=1, validators=[MinValueValidator(1),
                                                                   MaxValueValidator(3)])
    product = forms.CharField(label="Product ID", min_length=1, max_length=200)
    urlline = forms.CharField(label="Product URL", min_length=1, max_length=300)

    def clean_company(self):
        data = self.cleaned_data["company"]
        if data not in models.allowed:
            raise ValidationError("Incorrect Company", code="Incorrect Value Entered")
        return data

    def clean_region(self):
        data = self.cleaned_data["region"]
        # if data not in models.allowed:
        #     raise ValidationError("Incorrect Region ID", code="Incorrect Value Entered")
        return data

    def clean_city(self):
        data = self.cleaned_data["city"]
        # if data not in models.allowed:
        #     raise ValidationError("Incorrect City ID", code="Incorrect Value Entered")
        return data

    def clean_product(self):
        data = self.cleaned_data["product"]
        return data
        # if data not in models.allowed:
        #     raise ValidationError("Incorrect Product", code="Incorrect Value Entered")

    def clean_urlline(self):
        data = self.cleaned_data["urlline"]
        # try:
        #     validate = URLValidator()
        #     validate(data)
        # except ValidationError:
        #     raise ValidationError('Invalid URL')
        return data
