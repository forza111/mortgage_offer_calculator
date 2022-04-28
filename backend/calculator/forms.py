from django import forms

class CalculatorForm(forms.Form):
    real_estate_price = forms.IntegerField(label="Стоимость недвижимости", min_value=10000, label_suffix="")
    an_initial_fee = forms.IntegerField(label="Первоначальный взнос", label_suffix="")
    term = forms.IntegerField(label="Срок", min_value=1, max_value=30, label_suffix="")