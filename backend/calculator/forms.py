from django import forms

class CalculatorForm(forms.Form):
    real_estate_price = forms.IntegerField(min_value=10000)
    an_initial_fee = forms.IntegerField()
    term = forms.IntegerField()